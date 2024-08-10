from rest_framework import serializers
from datetime import datetime
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Год выпуска не может быть больше текущего года.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value

    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError("Пробег не может быть отрицательным.")
        return value

    def validate_transmission(self, value):
        valid_choices = [choice[0] for choice in Car.TRANSMISSION_CHOICES]
        if value not in valid_choices:
            raise serializers.ValidationError("Недопустимое значение для типа КПП.")
        return value

    def validate_fuel_type(self, value):
        valid_choices = [choice[0] for choice in Car.FUEL_CHOICES]
        if value not in valid_choices:
            raise serializers.ValidationError("Недопустимое значение для типа топлива.")
        return value

    def validate(self, data):
        brand = data.get('brand')
        model = data.get('model')
        if Car.objects.filter(brand=brand, model=model).exists():
            raise serializers.ValidationError(f"Автомобиль {brand} {model} уже существует.")
        return data