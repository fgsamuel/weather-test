from django.urls import path

from shipwell_test.core.api.v1.views import TemperatureView

urlpatterns = [
    path("api/v1/temperature/", TemperatureView.as_view()),
]
