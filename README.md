# LogXplain
LogXplain은 웹 로그의 유형을 분류하고, 그 근거를 시각화해주는 웹사이트입니다.<br>
기존 ML 기반 탐지는 결과의 신뢰성과 설명 가능성이 부족하다는 한계가 있습니다.
이를 보완하기 위해 LogXplain은 다음과 같은 기능을 제공합니다.

🔍 공격 유형별 확률 제공 → 예측 결과의 신뢰도를 수치로 확인

📝 시그니처 기반 탐지 문자열 시각화 → 어떤 패턴이 탐지되었는지 확인

💬 ChatGPT 기반 설명 제공 → 분류 근거를 자연어로 이해 가능

<br>

## 📅 프로젝트 기간
2023년 08월 ~ 2023년 10월

<br>

## 🛠 기술 스택
### Backend
* Python 3.10
* Django 5.2
* Django REST Framework 3.16

### Machine Learning
* scikit-learn 1.2.2
* CatBoost 1.2.8
* NumPy 1.24.3
* Pandas 2.3.0
* Joblib 1.5.1

### AI / External API
* OpenAI API 0.28.0

### Documentation
* drf-yasg (Swagger)

<br>

## 👤 담당 역할

* 데이터 수집 및 전처리
* 백엔드 API 개발

<br>

## ⚠️ 개발 중 발생한 이슈 및 해결 과정
### 1. 학습 데이터 부족

**문제 상황**

* 머신러닝 모델 학습에 사용할 로그 데이터가 부족
* 100개 이상의 추가 데이터가 필요했으나, 실제 로그를 수작업으로 생성하는 데 한계 존재

**해결 방법**

* Faker 라이브러리를 활용하여 가상의 웹 로그 데이터 생성

```python
def generate_query_body():
    query_params = [
        fake.word(),
        fake.word(),
        fake.word(),
    ]
    query_string = "&".join(query_params)
    return f"?{query_string}"

def generate_ip_address():
    return fake.ipv4()
```

**적용효과**

* 학습 데이터 부족 문제 해결
* 데이터 다양성 증가로 성능 향상

---

### 2. XML 형식 데이터셋 변환
**문제 상황**

* PKDD, CSIC 공개 데이터셋이 XML 형식으로 제공됨
* 머신러닝 학습을 위해 정형 데이터 구조로 변환 필요

**해결 방법**

* BeautifulSoup 라이브러리를 사용하여 XML 파싱 및 데이터프레임 생성

```python
# 데이터프레임을 만들기 위한 리스트 초기화
data6 = []

# 모든 sample 요소를 가져와서 type 값을 저장
sample_elements = soup2.find_all('sample')
for sample in sample_elements:
    type = sample.find('attack').text
    data6.append({'TYPE': type})

# 데이터프레임 생성
df6 = pd.DataFrame(data6)
```

**적용효과**

* 비정형(XML) 데이터를 학습 가능한 데이터로 변환
* 데이터 전처리 자동화로 처리 효율 향상

<br>

## ✨ API 구성
### api/predict

* 공격 유형을 예측합니다.
* 각 유형에 속할 확률을 계산합니다.
* 시그니처 기반 탐지에 사용된 문자열을 시각화합니다.

### api/gpt/response

* 탐지된 공격 유형의 분류 근거를 설명합니다.
* 대처 방안을 제시합니다.

<br>

## 🚀 실행 방법
1. <a href="https://platform.openai.com/api-keys">OpenAI API Keys</a> 에서 API_KEY를 발급받습니다.

2. Docker Desktop을 실행합니다.

3. 저장소를 클론합니다.
```
git clone https://github.com/yeon025/LogXplain.git
```
   
4. `LogXplain/project/.env` 파일을 생성한 뒤, 발급받은 API_KEY를 아래와 같이 입력합니다.
```.env
OPENAI_KEY="YOUR_API_KEY"
```

5. `run.sh`를 실행합니다.
```
cd LogXplain
./run.sh
```

6. 실행이 완료되면 브라우저에서 http://localhost/swagger 에 접속하여 확인할 수 있습니다.
