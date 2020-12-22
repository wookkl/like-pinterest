- 각각의 앱에는 MVT(Model View Template)으로 분리되어 있음
- 따라서 앱안에 templates라는 폴더를 만들고 또 다시 앱 이름의 폴더를 만들어준다. 이렇게 하는 이유는 가독성을 높이기 위함.

### STATIC_ROOT

- frontend단의 모든 static한 파일들을 이 static root path에 모아줌

### STATICFILES_DIRS

- 개발 단계에서 사용되는 정적 파일이 위치한 경로들을 설정하는 항목

### STATIC_URL

- 웹페이지가 사용할 정적 파일의 최상위 URL 경로
- 실제 파일이나 디렉토리가 아니고, URL

### STATIC_ROOT

- 장고 프로젝트에서 사용되느 모든 정적 파일들을 모으는 경로

### decorator

- 함수의 앞 뒤를 꾸며줌

#### Class decorator

- 일반적인 FBV와 다르게 @method_decorater 먼저 클래스 위에 써줘야함
- 그 안에 decorator를 넣어주고 decorating 하고자 하는 메서드를 넣어줌

```python
@method_decorator(login_required, 'get')
class CBV():
    """
    Class Based View CODE Here
    """

    def get(*args, **kwargs):
        pass
```

### form ImageField

- form 태그안에 이미지 필드를 받으려면 enctype속성에 'multipart/form-data'를 명시해줘야함

```html
<form action="" method="POST" enctype="multipart/form-data"></form>
```

### Redirect View

### unique_together

- 두개의 필드의 조합을 가지는 객체가 오직 하나만 존재할 수 있도록 메타 클래스에 정의

```python
class Meta:
        unique_together = ("field1", "field2")
```
