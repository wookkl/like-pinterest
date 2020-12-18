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
