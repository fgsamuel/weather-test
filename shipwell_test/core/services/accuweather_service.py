import logging

from shipwell_test.core.services.base_service import BaseService

logger = logging.getLogger(__name__)


class AccuweatherService(BaseService):
    url = "http://fake-weather.shipwell.com/accuweather"
    request_method = "get"

    def _generate_data_and_parameters(self, lat, lng, temp_unit):
        return {"params": {"latitude": lat, "longitude": lng}, "data": None}

    def _prepare_response(self, response, temp_unit):
        try:
            data = response.json()["simpleforecast"]["forecastday"][0]["current"]
            temperature = data["fahrenheit"]
            if temp_unit.lower() == "c":
                temperature = data["celsius"]
        except Exception as e:
            logger.exception(e)
            temperature = None
        return temperature
