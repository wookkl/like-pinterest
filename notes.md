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

- 주어진 url로 redirect 시키는 뷰

### unique_together

- 두개의 필드의 조합을 가지는 객체가 오직 하나만 존재할 수 있도록 메타 클래스에 정의

```python
class Meta:
        unique_together = ("field1", "field2")
```

### values_list

- key, value의 형태가 아닌 tuple 형태로 가져올 수 있음

```python
# Subsription 객체들중  user가 self.request.user인 객체들의 project필드만 tuple형태로 가져옴
projects = Subscription.objects.filter(user=self.request.user).values_list(
            "project"
)
```

### WYSIWYG

- What you See Is What You Get 너가 보는대로 글이 써진다
- 게시판 기능중 하나
- 게시판의 폰트 크기나 형태들을 자유롭게 할 수 있는 기능
- medium-editor라는 오픈 소스로 사용할 수 있음

# 배포 단계

- VULTR라는 가상 서버를 빌려서 서비스 배포할 것임

### 도커 사용하는 이유?

- docker는 꼭 필요한 시스템 사용되는 이유는 빠르고 어디서나 같은 환경으로 사용가능
- 규격화되고 표준화된 컨테이너. 같은 환경!
- 이미지형태로 환경등을 구축해 놓으면 재사용이 가능함

### VPS란?

- Virtual Private Server(가상 사설 서버) Ex) aws, azure, VULTR

### docker hub?

- 전세게에서 모든 도커 이미지들을 업로드하고 가져올 수 있는 플랫폼

### portainer.io

- docker을 gui방식으로 바꿔줌

### django container 이미지를 올리기 위해서는?

1. Upload Source to Github
2. Write Dockerfile
3. Build Image
4. Run Container

### Dockerfile의 commands

- BASE : 기본이 되는 이미지를 고르는 작업
- RUN : COMMAND를 실행 시켜줌 pip list.. , git clone.. 이런 명령어들
- WORKDIR : cd랑 비슷,
- EXPOSE : 포트들이 존재하는데 장고 컨테이너에서의 포트를 사용할 수 있도록 EXPOSE해준다는 느낌, VULTR의 포트와 연결..
- CMD: 기본 커맨드를 설정 해놓는 것 항상 실행할때 사용해야하는 커맨드를 적어두는 것 ex python manage.py runserver...

### pip install -r requirements.txt

- requirements.txt안에 있는 패키지들을 모두 설치하겠다!

### Django container로써의 문제점

- `python managet.py runserver` 는 배포용이 아니라 개발용임
- 이런 문제점을 없애기 위해 Gunicorn이라는 라이브러리를 설치해줌 django안에,

### Gunicorn이란?

- Nginx와 Django를 연결시켜주는 interface
