# LogXplain
LogXplain은 웹 로그의 유형을 분류하고, 그 근거를 시각화해주는 웹사이트입니다.<br>
기존 ML 기반 탐지는 결과의 신뢰성과 설명 가능성이 부족하다는 한계가 있습니다.
이를 보완하기 위해 LogXplain은 다음과 같은 기능을 제공합니다.

🔍 공격 유형별 확률 제공 → 예측 결과의 신뢰도를 수치로 확인

📝 시그니처 기반 탐지 문자열 시각화 → 어떤 패턴이 탐지되었는지 확인

💬 ChatGPT 기반 설명 제공 → 분류 근거를 자연어로 이해 가능

⚠️ **탐지 가능한 공격 유형**
| 공격 유형                   | 설명                          |
| ----------------------- | --------------------------- |
| LDAP Injection      | LDAP 쿼리를 조작하여 인증 우회 및 정보 탈취 |
| OS Command Injection | 시스템 명령어 실행을 통한 권한 탈취        |
| Path Traversal       | 디렉토리 경로 조작으로 민감한 파일 접근      |
| SQL Injection       | SQL 쿼리 변조를 통한 데이터베이스 공격     |
| SSI Injection        | 서버사이드 인클루드(SSI) 조작          |
| XPath Injection      | XML 데이터 질의 조작               |
| XSS                  | 악성 스크립트를 삽입하여 클라이언트 공격      |
| ShellShock           | Bash 취약점을 악용한 원격 명령 실행      |

<br>

## ✨ Key Features
### api/predict

* 공격 유형을 예측합니다.
* 각 유형에 속할 확률을 계산합니다.
* 시그니처 기반 탐지에 사용된 문자열을 시각화합니다.

### api/gpt/response

* 탐지된 공격 유형의 분류 근거를 설명합니다.
* 대처 방안을 제시합니다.

<br>

## 🚀 Usage
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
