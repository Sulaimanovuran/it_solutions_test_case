from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import NotFound



class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['brand', 'model', 'year', 'fuel_type', 'transmission']
    ordering_fields = ['mileage', 'price']


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Car.DoesNotExist:
            raise NotFound("Автомобиль не найден.")
    