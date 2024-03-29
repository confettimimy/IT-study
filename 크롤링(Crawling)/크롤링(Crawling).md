## 크롤링(Crawling)이란

크롤링(Crawling) = 파싱(Parsing) = 스크래핑(Scraping) = 스파이더링(Spidering)



일일히 검색하여 하나씩 다운받으려면 엄청난 시간이 걸림

-> 크롤링을 사용하자



크롤링이란 인터넷에 있는 정보 중 우리가 원하는 것만 골라서 자동으로 수집해주는 기술을 말한다.



예를 들어 학교/회사의 식당표를 크롤링하면 오늘의 식단을 볼 수 있는 서비스를 만들 수 있고, 다양한 뉴스 사이트에서 원하는 주제의 뉴스만 골라서 모아 볼 수 있는 서비스도 만들 수 있다.



<hr></hr>

## 크롤링을 위한 환경설정

Python과 Beautifulsoup, Requests와 같은 관련 라이브러리들을 설치해야함.

이 모든걸 쌩으로 내 컴퓨터에 설치하게 되면 나중에 다른 작업을 할 때 버전 간 충돌이 발생하는 등의 문제가 있을 수 있다.  따라서 보통 가상환경을 구성해서 (venv, virtualenv, conda 등) 거기에 설치하는 굉장히 귀찮고 복잡한 과정을 거치게 된다. (아주 공감)



**그래서 이번에는 <<구름IDE>>를 이용해볼 것이다.**

구름IDE에서는 개발 환경이 갖춰진 가상의 컴퓨터를 제공해주는 것이라 별도의 언어 설치 과정이 필요하지 않고, 또 다른 작업을 할 때는 가상컴퓨터를 새롭게 만들어서 거기서 작업하면 되므로 버전 간의 충돌도 일어날 일이 없다. (wow)

이런 클라우드 기반 IDE 서비스를 이용하면 그런 시간(로컬 개발환경을 구성하는 데 굉장히 오래걸리고 귀찮음)이 많이 단축되고 편리하게 개발에만 집중할 수 있다.

[구름 IDE 주소](ide.goorm.io)



<hr></hr>

## 크롤링에 필요한 라이브러리 설치

크롤링 작업을 하기 위해 Beautiful Soup 패키지(라이브러리)를 이용한다.

- Beautiful Soup: 크롤링용 라이브러리
- Pandas: 데이터분석용 라이브러리

pip install bs4(패키지명)

---

##### + 크롤러의 저작권 침해 문제

‘크롤러(Crawler)’라고 불리는 웹상에 흩어진 데이터를 수집하는 프로그램을 자동으로 실행하는 과정에서 일부 저작물이 포함된 경우의 위법성 여부를 달리 판단해야 할 지이다. (논문출처)

