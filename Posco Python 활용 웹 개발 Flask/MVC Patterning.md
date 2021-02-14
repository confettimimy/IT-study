## MVC Patterning

Model / View / Controller 세 단계로 구성하여 Web Application을 구조화하는 방식

- **Model** : Data Base와 연결, Data를 처리하는 부분. 즉 Data Base와 관련된 작업들을 하는 곳   _(model 폴더)_
- **View** : HTML 화면 구성, 시각화 및 UI를 처리하는 부분   _(statics / templates 폴더)_
- **Controller** : Model과 View를 연결 관리, Protocol 관리(Flask)   _(app.py)_

---

👉🏻👉🏻👉🏻 기본적으로 Flask는 Program에 정해진 구성 요소를 맞춰 폴더를 생성해야함

ㄴ model: **Data Base / Back End를 다룰 수 있는 부분**

ㄴ statics: 정적인 View, image 또는 css 디자인이 들어가는 부분

ㄴ templates: 동적인 View, **HTML**, Java Script, Node js 등

ㄴ app.py: **Front End와 Back End를 연결하는 Controller**

---

### [Flask 실습]

VS Code를 이용해 가상환경 설치 후,

Model과 Controller 부분을 Python으로 작업, View는 HTML 및 Java script로 작업.