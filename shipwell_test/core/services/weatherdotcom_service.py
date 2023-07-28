import logging

from shipwell_test.core.services.base_service import BaseService

logger = logging.getLogger(__name__)


class WeatherdotcomService(BaseService):
    url = "http://fake-weather.shipwell.com/weatherdotcom"
    request_method = "post"

    def _generate_data_and_parameters(self, lat, lng, temp_unit):
        return {
            "params": None,
            "json": {
                "lat": lat,
                "lon": lng,
            },
        }

    def _prepare_response(self, response, temp_unit):
        try:
            temperature = response.json()["query"]["results"]["channel"]["condition"]["temp"]
            if temp_unit.lower() == "c":
                temperature = self._convert_f_to_c(temperature)
        except Exception as e:
            logger.exception(e)
            temperature = None
        return temperature

    @staticmethod
    def _convert_f_to_c(temperature):
        return (float(temperature) - 32) * 5 / 9
