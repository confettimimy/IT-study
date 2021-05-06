## Eye Tracker Manager (캘리브레이션 단계)

In addition to being a graphical application in which you can browse eye trackers and work with selected eye tracker, **you can also launch Eye Tracker Manager with command line arguments to directly trigger its features.** This allows you to reuse some of the features of Eye Tracker Manager instead of implementing your own version (using the Tobii Pro SDK).

​    

*[command line 참고](http://developer.tobiipro.com/eyetrackermanager/etm-sdk-integration.html)

​    

| OS      | Path                                                         |
| :------ | :----------------------------------------------------------- |
| Windows | `%localappdata%\Programs\TobiiProEyeTrackerManager\TobiiProEyeTrackerManager.exe` * |
| Linux   | `/opt/TobiiProEyeTrackerManager/TobiiProEyeTrackerManager` (can be called by alias `TobiiProEyeTrackerManager`) |
| MacOS   | `/Applications/TobiiProEyeTrackerManager.app/Contents/MacOS/TobiiProEyeTrackerManager` |

#

###### Tobii Pro Eye Tracker Manager

거치형 아이트래커를 관리할 수 있는 무료 소프트웨어입니다. 아이트래커와 모니터 등의 시각적 자극을 설정하고 캘리브레이션 및 트러블슈팅을 할 수 있습니다. 아이트래커 모델에 따라서는 펌웨어 업데이트도 가능합니다.

---

## Calibrating with Eye Tracker Manager

As an alternative to implementing your own calibration stimuli presentation software, you can use Eye Tracker Manager's calibration feature to perform calibrations. Eye Tracker Manager is a stand-alone application and you need to manually start it, select eye tracker, and click on start calibration to initiate the calibration procedure. Hence, using Eye Tracker Manager for calibration may not suit your intended workflow, but it is very handy during development.

​    

캘리브레이션을 수행하기 위해 자체 캘리브레이션 프레젠테이션 소프트웨어를 직접 구현하는 것 대신

Eye Tracker Manager의 보정 기능을 사용하여 보정을 수행할 수 있다.

Eye Tracker Manager는 독립 실행형 응용 프로그램이며 수동으로 시작하고 아이 트래커를 선택한 다음 보정 시작을 클릭하여 보정 절차를 시작해야 한다. (그때 거쳤던 과정)

(따라서 보정을 위해 Eye Tracker Manager를 사용하면 의도한 워크 플로에 적합하지 않을 수 있지만 개발 중에는 매우 편리하다)

---

