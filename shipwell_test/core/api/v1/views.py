from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shipwell_test.core.api.v1.serializers import TemperatureSerializer
from shipwell_test.core.services.accuweather_service import AccuweatherService
from shipwell_test.core.services.noaa_service import NoaaService
from shipwell_test.core.services.weatherdotcom_service import WeatherdotcomService


class TemperatureView(APIView):
    @swagger_auto_schema(
        request_body=TemperatureSerializer,
        operation_summary="Get average temperature from multiple services",
        operation_description="Get average temperature from multiple services",
    )
    def post(self, request, *args, **kwargs):
        data = TemperatureSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        service_classes = {
            "accuweather": AccuweatherService,
            "noaa": NoaaService,
            "weatherdotcom": WeatherdotcomService,
        }

        services = data.validated_data["services"]
        service_data = {
            "lat": data.validated_data["latitude"],
            "lng": data.validated_data["longitude"],
            "temp_unit": data.validated_data["temperature_unit"],
        }

        results = []
        for service in services:
            service_instance = service_classes[service]()
            results.append(service_instance.get_weather(**service_data))

        valid_results = [float(result) for result in results if result is not None]

        if valid_results:
            average_temperature = sum(valid_results) / len(valid_results)
        else:
            average_temperature = None

        return Response({"temperature": average_temperature}, status=status.HTTP_200_OK)
