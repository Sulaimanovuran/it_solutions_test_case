from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def cars_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class CarNotFoundException(APIException):
    status_code = 404
    default_detail = "Автомобиль не найден."
    default_code = "car_not_found"