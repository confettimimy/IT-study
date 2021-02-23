## A quick guide to a functional application

Most eye tracking applications follow the same pattern in terms of in which order functionality is used. The order is usually as follows:

1. Browsing for eye trackers or selecting an eye tracker with known address.
2. Establishing a connection with the eye tracker.
3. Running a calibration procedure in which the eye tracker is calibrated to the user.
4. Setting up a subscription to gaze data, and collecting and saving the data on the computer running the application. In some cases, the data is also shown live by the application.

​    

To do this with the Pro SDK is very simple:

### Step 1: Browsing

Start with importing `tobii_research`, and use either the `tobii_research.find_all_eyetrackers` function to get a list of available eye trackers, or create a `tobii_research.EyeTracker` object from an address (URI).

### Step 2: Connecting to an eye tracker

The objects returned from `find_all_eyetrackers` are instances of `tobii_research.EyeTracker`. Through those objects you can interact with the eye trackers.

### Step 3: Performing a calibration

To calibrate the eye tracker, use either a `tobii_research.ScreenBasedCalibration` or a `tobii_research.HMDBasedCalibration` object (depending on the type of eye tracker). The `tobii_research.ScreenBasedCalibration` / `tobii_research.HMDBasedCalibration` class requires a `tobii_research.EyeTracker` object to be passed to the constructor. More information about how a calibration works can be found in the section [Calibration](http://developer.tobiipro.com/commonconcepts/calibration.html).

### Step 4: Subscribing to data

When you have the an `EyeTracker` object and want to subscribe to gaze data, subscribe to either `EYETRACKER_GAZE_DATA` or `EYETRACKER_HMD_GAZE_DATA` (depending on the type of eye tracker). The data will be available as `GazeData` or `HMDGazeData` respectively. You can also get the data as a dictionary if you send `True` for `as_dictionary` to `EyeTracker.subscribe_to`.

[출처](http://developer.tobiipro.com/python/python-getting-started.html)

---

```markdown
Pro SDK 수행하기

1 단계 : 찾아보기
**tobii_research 가져 오기부터 시작하고 tobii_research.find_all_eyetrackers 함수를 사용하여 사용 가능한 시선 추적기 목록을 가져 오거나** 주소 (URI)에서 tobii_research.EyeTracker 개체를 만듭니다.

2 단계 : 아이 트래커에 연결
find_all_eyetrackers에서 반환 된 객체는 tobii_research.EyeTracker의 인스턴스입니다. 이러한 개체를 통해 시선 추적기와 상호 작용할 수 있습니다.

3 단계 : 보정 수행
시선 추적기를 보정하려면 tobii_research.ScreenBasedCalibration 또는 tobii_research.HMDBasedCalibration 개체 (시선 추적기 유형에 따라 다름)를 사용합니다. tobii_research.ScreenBasedCalibration / tobii_research.HMDBasedCalibration 클래스에는 생성자에 전달되는 tobii_research.EyeTracker 객체가 필요합니다. 보정 작동 방식에 대한 자세한 내용은 보정 섹션에서 찾을 수 있습니다.

4 단계 : 데이터 구독
EyeTracker 개체가 있고 시선 데이터를 구독하려면 EYETRACKER_GAZE_DATA 또는 EYETRACKER_HMD_GAZE_DATA (시선 추적기 유형에 따라 다름)를 구독하십시오. 데이터는 각각 GazeData 또는 HMDGazeData로 사용할 수 있습니다. as_dictionary에 대해 True를 EyeTracker.subscribe_to로 보내면 데이터를 사전으로 가져올 수도 있습니다.
```

​    

*SDK란?

소프트웨어 개발 키트(Software Development Kit).

소프트웨어 개발자가 특정 운영체제용 응용프로그램을 만들 수 있게 해주는 소스(Source)와 도구 패키지이다.

---



