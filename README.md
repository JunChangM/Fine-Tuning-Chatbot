# Fine-Tuning-Chatbot

9/26 : https://wikidocs.net/198481

9/27 : https://wikidocs.net/197549 Django 깊이 파고 들기
Django Model에 관하여 읽음. 간단히 Author 과 Book class 로 Data를 생성하고 저장해보는 예제를 봄.

View
Django의 뷰(Views)는 웹 요청을 받아 처리하고 웹 응답을 반환하는 Python 함수
뷰는 애플리케이션의 데이터와 사용자 인터페이스를 연결하는 역할
뷰는 데이터베이스로부터 데이터를 가져오고(모델을 통해), 필요한 작업을 수행한 후 데이터를 템플릿에 전달하여 렌더링
1. 함수 기반 뷰(Function-Based Views, FBVs)
2. 클래스 기반 뷰(Class-Based Views, CBVs)
Django 뷰는 HTTP 요청을 처리하고 HTTP 응답을 반환하는 역할을 담당
Django REST Framework의 맥락에서 뷰는 API 엔드포인트를 정의하고 데이터를 검색, 생성, 업데이트 또는 삭제하는 방법을 정의하는 데 사용