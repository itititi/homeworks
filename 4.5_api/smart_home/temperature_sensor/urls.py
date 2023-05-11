from django.urls import path
from .views import SensorList, SensorDetail, MeasurementList, MeasurementDetail


urlpatterns = [
    path('sensors/', SensorList.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', SensorDetail.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementList.as_view(), name='measurement-list'),
    path('measurements/<int:pk>/', MeasurementDetail.as_view(), name='measurement-detail'),
]
