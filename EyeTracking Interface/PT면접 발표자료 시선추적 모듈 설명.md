첫 번째 프로젝트에서 알고리즘을 통해 기술 구현 능력을 얻었고,

두 번째 프로젝트에서  (직무관련 얻은 역량 생각해보기)

---

**1.**  **아이트래커 장치 검색** 

find_all_eyetrackers()

**2.**  **Calibration** **조정 작업**

정확한 시점의 산출을 위해 사용자 얼굴과 눈을 인식해 Calibration 수행

![텍스트, 전자기기이(가) 표시된 사진  자동 생성된 설명](file:///C:/Users/gggc8/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

**3.**  **시선 데이터 획득, 변환, 출력**

gaze_data_callback(gaze_data) <- 콜백 함수

(소스코드 …이하 모니터 좌표로 변환)

얻은 시선 데이터 -> 모니터 좌표로 변환 + -> 화면에 출력까지!( SetCursor() 를 통해 마우스 포인터 맵핑)

얻은 시선 데이터로 여기 콜백함수에서 원하는 작업 수행

 

**4.**  **새로운 시선 데이터가 들어올 때마다 반복 수행**

= 새로운 시선 데이터가 들어올 때마다 위 정의한 콜백함수 호출됨 = 반복!

subscribe_to(gaze_data_callback) 한 번 호출


 my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

아이 트래커 개체의 subscribe_to 함수를 한 번만 호출하면됩니다.

매개 변수는 방금 정의한 콜백 함수

---



## pt발표 시선추적 모듈 설명

시선 추적기를 검색하려면 find_all_eyetrackers ()를 호출하고 출력을 새 변수에 할당하면 됩니다.

시선 데이터를 보다 더 정확하게 수집하기 위해 캘리브레이션을 수행  Calibration 수행



새로운 시선 데이터가 들어올 때마다 gaze_data_callback(gaze_data) 함수가 호출됨. (사용자가 직접 호출x)

콜백 함수는 사용자가 직접 호출 할 필요가 없다는 점만 유일하게 다른 점.



**대신 새로운 시선 데이터 샘플이있을 때마다 호출됩니다.** 따라서이 콜백 함수에서 시선 데이터로 원하는 작업을 수행합니다 (예 : 일부 인쇄).





```-
my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
```

첫 번째 입력 매개 변수는 SDK에 우리가 원하는 * 시선 데이터 *임을 알려주는 상수입니다. 아이 트래커에서 얻을 수있는 다른 유형의 데이터에 대한 다른 상수가 있습니다. 

두 번째 매개 변수는 방금 정의한 콜백 함수

세 번째 매개 변수는 SDK에 데이터를 딕셔너리 자료형으로 원한다고 알려줍니다.