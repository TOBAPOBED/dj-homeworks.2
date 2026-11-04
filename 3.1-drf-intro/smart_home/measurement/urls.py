from django.urls import path
from .views import SensorListView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]