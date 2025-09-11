from django.urls import path
from app.views import predict_type, generate_gpt_response

urlpatterns = [
    path("predict", predict_type),  # 공격 유형 예측
    path("gpt/response", generate_gpt_response),  # gpt 응답 생성
]
