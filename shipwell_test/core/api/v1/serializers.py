from rest_framework import serializers


class TemperatureSerializer(serializers.Serializer):
    SERVICE_CHOICES = ["accuweather", "noaa", "weatherdotcom"]
    UNIT_CHOICES = ["c", "f"]

    services = serializers.ListField(child=serializers.ChoiceField(choices=SERVICE_CHOICES))
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    temperature_unit = serializers.ChoiceField(choices=UNIT_CHOICES, required=False)

    def to_internal_value(self, data):
        data["services"] = [service.lower() for service in data["services"]]
        if "temperature_unit" in data:
            data["temperature_unit"] = data["temperature_unit"].lower()
        return super().to_internal_value(data)
