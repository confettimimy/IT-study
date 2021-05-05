## 파이썬(Python) 2.7 공식 지원 종료

2020년 1월 1일부터 파이썬Python 2.7에 대한 지원이 공식적으로 종료되었습니다. **당장 파이썬 2.7로 만든 도구나 서버가 멈춰버리는 일은 일어나지 않지만,** 다음 버전으로 (가급적 3.x의 최신 버전이 좋겠죠) 옮겨가야 할 날이 머지 않았다는 의미입니다.

​    

### 대응 방법

공식 문서인 [파이썬 2 코드를 파이썬 3 코드로 옮기기](https://docs.python.org/3/howto/pyporting.html?fbclid=IwAR0TTKSsT-0V4js_4FaSRkx1ld0eRFi4yp8DEdYUjexyHHgJSOpx6biAkIQ)를 가장 추천합니다. 코드를 자동으로 변환해주는 [2to3](https://docs.python.org/ko/3/library/2to3.html) 같은 도구를 사용할 수도 있습니다.

##### 2to3 - 파이썬 2에서 파이썬 3으로 자동 코드 변환

2to3는 파이썬 2.x 소스 코드를 유효한 파이썬 3.x 코드로 변환하기 위해 일련의 *변환자(fixers)*를 적용하는 프로그램입니다. 표준 라이브러리는 많은 양의 변환자를 제공하고 있어 코드 대부분을 처리할 수 있을 것입니다. 2to3에서 사용하는 모듈인 [`lib2to3`](https://docs.python.org/ko/3/library/2to3.html#module-lib2to3) 는 유연하고 제네릭합니다. 따라서 2to3 프로그램을 위해 당신만의 변환자를 작성할 수 있습니다.

터미널창을 열어

```python
pip install 2to3
```



