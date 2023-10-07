# Directory
📦example
 ┗ 📂myproject
 ┃ ┣ 📂myapp
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📂templates
 ┃ ┣ 📂myproject

# ERROR
10/7 : "return render(request, 'myapp/template/create_book.html', {'form': form}) "


render 함수에서 html을 찾을 수 없다는 오류가 발생하였다. 찾아보니 django 내의 templates 폴더가 따로 있었고, 토이프로젝트를 진행할 때는 해당 DIR을 설정해주어야 함을 알 수 있었다. (출처 : https://iamiet.tistory.com/entry/Django-templates-%ED%8F%B4%EB%8D%94-%EA%B2%BD%EB%A1%9C-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)


myproject/setting.py 에서 tempaltes를 다음과 같이 수정하였다.
```
import os
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "myapp/templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
또한, 추가적으로 myapp 폴더 안에 templates를 만들었으므로 myapp/view.py도 다음과 같이 경로를 수정하였다.
```
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'template/book_list.html', {'books': books})
```



### 참고사항
## render 함수 (https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/)
render(request, template_name, context=None, content_type=None, status=None, using=None)
### Example
```
from django.shortcuts import render
def my_view(request):
    # View code here...
    return render(request,"myapp/index.html",{"foo": "bar",},content_type="application/xhtml+xml",)
```

