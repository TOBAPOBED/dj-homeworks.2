from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListView(generics.ListCreateAPIView):
    """GET — список датчиков, POST — создать датчик"""
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SensorListSerializer
        return SensorListSerializer


class SensorDetailView(generics.RetrieveUpdateAPIView):
    """GET — полная информация, PATCH — обновить датчик"""
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        return SensorListSerializer


class MeasurementCreateView(generics.CreateAPIView):
    """POST — добавить измерение"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer