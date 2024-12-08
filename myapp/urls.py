from django.urls import path
from .views import *

urlpatterns = [
    path('api/hourly-average-summary/', hourly_average_summary, name='hourly_average_summary'),
    path('execute_code/', execute_code, name="execute_code"),
    path('api/current-weather/', current_weather, name='current-weather'),
]