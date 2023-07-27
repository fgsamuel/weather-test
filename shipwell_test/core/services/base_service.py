import logging

from shipwell_test.core.services.client import ClientBase

logger = logging.getLogger(__name__)


class BaseService:
    url = ""
    request_method = "get"

    def __init__(self, *args, **kwargs):
        self.client = ClientBase(self.url)

    def _generate_data_and_parameters(self, lat, lng, temp_unit):
        return {
            "params": None,
            "data": None,
            "json": None,
        }

    def get_weather(self, lat, lng, temp_unit="F"):
        print("iniciou o servico")
        request_data = self._generate_data_and_parameters(lat, lng, temp_unit)
        try:
            response = self.client.request(self.request_method, **request_data)
        except Exception as e:
            logger.exception(e)
            return None
        print("finalizou o servico")
        return self._prepare_response(response, temp_unit)

    @staticmethod
    def _prepare_response(response, temp_unit):
        return None
