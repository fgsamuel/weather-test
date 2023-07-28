import logging

from shipwell_test.core.services.base_service import BaseService

logger = logging.getLogger(__name__)


class NoaaService(BaseService):
    url = "http://fake-weather.shipwell.com/noaa"
    request_method = "get"

    def _generate_data_and_parameters(self, lat, lng, temp_unit):
        return {"params": {"latlon": f"{lat},{lng}"}, "data": None}

    def _prepare_response(self, response, temp_unit):
        try:
            data = response.json()["today"]["current"]
            temperature = data["fahrenheit"]
            if temp_unit.lower() == "c":
                temperature = data["celsius"]
        except Exception as e:
            logger.exception(e)
            temperature = None
        return temperature
