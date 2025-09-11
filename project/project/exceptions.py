from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class UnreliablePredictionError(APIException):
    status_code = 422
    default_detail = "모델의 학습이 충분하지 않아 예측 결과를 신뢰할 수 없습니다. 따라서 해당 결과는 무시되었습니다."


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data = {
            "status_code": response.status_code,
            "detail": str(response.data.get("detail", str(exc))),
        }

    return response
