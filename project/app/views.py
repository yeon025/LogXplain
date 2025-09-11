from rest_framework.decorators import api_view
from rest_framework.response import Response
from service.convert_to_dataframe import convert_string
from service.preprocessing import preprocessing
from service.predict import predict, detect_attack_string, checkIfAttack
from service.openai import gpt
from .serializers import (
    PredictionRequestSerializer,
    PredictionResponseSerializer,
    GptRequestSerializer,
    GptResponseSerializer,
)
from drf_yasg.utils import swagger_auto_schema


# 공격 유형 예측
@swagger_auto_schema(
    method="post",
    request_body=PredictionRequestSerializer,
    responses={200: PredictionResponseSerializer},
)
@api_view(["POST"])
def predict_type(request):
    payload = request.data.get("payload")

    # payload를 데이터프레임으로 변환
    converted_payload = convert_string(payload)

    # 전처리
    preprocessed_data = preprocessing(converted_payload)

    # 공격 유형 예측과 공격 유형에 속할 확률을 계산
    predicted_type, probs = predict(preprocessed_data)

    detected_string = None
    if checkIfAttack(predicted_type):
        # 문자열 탐지
        detected_string = detect_attack_string(predicted_type, preprocessed_data)

    # 직렬화
    result = {
        "predictedType": predicted_type,
        "ldapInjection": round(probs[0][0], 2),
        "osCommanding": round(probs[0][1], 2),
        "pathTraversal": round(probs[0][2], 2),
        "ssi": round(probs[0][3], 2),
        "shellShock": round(probs[0][4], 2),
        "sqlInjection": round(probs[0][5], 2),
        "xpathInjection": round(probs[0][6], 2),
        "xss": round(probs[0][7], 2),
        "normal": round(probs[0][8], 2),
        "detectedString": detected_string,
        "payload": payload,
    }
    result_serializer = PredictionResponseSerializer(result)

    return Response(result_serializer.data)


# GPT 응답 생성
@swagger_auto_schema(
    method="post",
    request_body=GptRequestSerializer,
    responses={200: GptResponseSerializer},
)
@api_view(["POST"])
def generate_gpt_response(request):
    payload = request.data.get("payload")
    predicted_type = request.data.get("predictedType")

    # Gpt 응답
    gpt_response, assistant_response = gpt(payload, predicted_type)

    # 직렬화
    result = {
        "gptResponse": gpt_response,
        "assistantResponse": assistant_response,
    }
    result_serializer = GptResponseSerializer(result)

    return Response(result_serializer.data)
