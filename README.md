# Fine-Tuning-Chatbot

## 9/26 : https://wikidocs.net/198481

## 9/27 : https://wikidocs.net/197549 Django 깊이 파고 들기

Django Model에 관하여 읽음. 간단히 Author 과 Book class 로 Data를 생성하고 저장해보는 예제를 봄.

View

Django의 뷰(Views)는 웹 요청을 받아 처리하고 웹 응답을 반환하는 Python 함수
뷰는 애플리케이션의 데이터와 사용자 인터페이스를 연결하는 역할
뷰는 데이터베이스로부터 데이터를 가져오고(모델을 통해), 필요한 작업을 수행한 후 데이터를 템플릿에 전달하여 렌더링

1. 함수 기반 뷰(Function-Based Views, FBVs)
2. 클래스 기반 뷰(Class-Based Views, CBVs)

Django 뷰는 HTTP 요청을 처리하고 HTTP 응답을 반환하는 역할을 담당
Django REST Framework의 맥락에서 뷰는 API 엔드포인트를 정의하고 데이터를 검색, 생성, 업데이트 또는 삭제하는 방법을 정의하는 데 사용

## 10/17

### Django의 템플릿
Django는 자체 템플릿 언어를 사용합니다. Django 프로젝트에서 각 Django 앱에는 기본적으로 templates 디렉터리가 포함됩니다.


Django 템플릿 시스템의 가장 강력한 측면 중 하나는 템플릿 상속입니다. 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하는 기본 "스켈레톤" 템플릿을 만들고, 이를 자식 템플릿이 오버라이드할 수 있는 블록을 정의할 수 있습니다.


{% extends %} 태그는 템플릿 상속에서 부모 템플릿을 지정하는 데 사용됩니다. 


자주 사용되는 다른 태그로는 반복을 위한 {% for %}, 조건문을 위한 {% if %}, 자식 템플릿에서 오버라이드할 블록을 정의하기 위한 {% block %} 등이 있습니다.


뷰에서 템플릿으로 데이터를 렌더링하기 위해 변수를 사용합니다. 템플릿에 컨텍스트를 전달할 때 (일반적으로 딕셔너리 형태로), 템플릿은 컨텍스트 변수에 접근하여 렌더링할 수 있습니다. 예를 들어, 뷰에서 'book' 변수를 전달하면 템플릿에서 {{ book.title }}과 같이 책의 제목을 표시할 수 있습니다.

### [폼 및 사용자 입력](https://wikidocs.net/197553)
example/myproject에서 진행

### [06) 프론트엔드 자산 통합](https://wikidocs.net/197554)
Django는 각 애플리케이션에서 (및 지정한 기타 위치에서) 정적 파일을 하나의 위치로 수집하여 제품으로 서비스할 수 있게 합니다. 이를 위해 설정 파일에 STATIC_URL, STATIC_ROOT 및 STATICFILES_DIRS를 설정해야 합니다.

미디어 파일은 조금 다릅니다. 사용자가 파일을 업로드하면 Django는 MEDIA_ROOT 설정에서 지정한 디렉터리에 파일을 저장합니다. 개발 중에는 MEDIA_URL 설정을 사용하여 파일을 제공하지만 제품 환경에서는 웹 서버나 클라우드 저장소 서비스에서 처리합니다.

### [관리자 인터페이스 활성화] (https://wikidocs.net/197555)

## [04. Django REST 프레임워크: 전문가처럼 API 구축](https://wikidocs.net/197558) 10월 중...