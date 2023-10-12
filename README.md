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

## [04. Django REST 프레임워크: 전문가처럼 API 구축](https://wikidocs.net/197558)
RESTful API (Representational State Transfer Application Programming Interfaces)는 서로 다른 소프트웨어 응용 프로그램 간에 데이터와 기능을 공유할 수 있도록 하는 커뮤니케이션 브릿지 역할을 합니다. 시스템이 표준 HTTP 메서드(GET, POST, PUT, DELETE 등)를 사용하여 HTTP를 통해 통신하고 데이터를 교환할 수 있습니다.


Django REST Framework (DRF)은 RESTful API를 구축하기 위한 강력한 도구로써 다양한 기능을 제공합니다.

### [04-04 라우터](https://wikidocs.net/197564)
URL 라우팅 소개


Django REST Framework (DRF)에서 "Router"는 RESTful API를 구축하기 위한 자동 URL 라우팅과 뷰셋 바인딩을 돕는 편리한 기능입니다. 이 기능은 URL 패턴을 정의하고 뷰셋과 연결하는 과정을 단순화하여 제공된 뷰셋을 기반으로 필요한 URL을 자동으로 생성합니다. DRF의 Router 클래스는 뷰셋을 등록하고 해당 뷰셋에 대한 표준 CRUD (Create, Retrieve, Update, Delete) 작업에 대한 URL 패턴을 자동으로 생성하는 일련의 메서드를 제공합니다. 


Postman 설치 및 사용 : url을 이용한 DB CRUD를 편히 볼 수 있다.

### 04-05 프레임워크에서 인증과 권한
### 04-06 페이지네이션, 필터링, 그리고 정렬
Django REST Framework에서 페이지네이션, 필터링, 그리고 정렬을 지원하는 API를 만드는 것은 매우 쉽습니다. 이러한 기능은 대량의 데이터를 반환하는 API에 있어서 중요합니다. 페이지네이션을 사용하지 않으면 API가 한 번에 너무 많은 데이터를 반환하려고 하여 응답 시간이 느려지고 서버 부하가 증가할 수 있습니다. 필터링과 정렬은 클라이언트가 원하는 특정 데이터를 쉽게 찾을 수 있도록 도와줍니다.