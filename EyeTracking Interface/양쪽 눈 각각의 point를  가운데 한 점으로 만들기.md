### 양쪽 눈 각각의 point를  가운데 한 점으로 만드는 과정

양쪽 눈은 두 개인데, 마우스 포인터 점은 하나니까

​    

​                         gaze_left_eye                                    gaze_right_eye

​                               (x, y)                        ⚫️                        (x, y)

​                                                최종적으로 정제된 x, y

xs = (왼쪽x값, 오른쪽x값)

ys = (왼쪽y값, 오른쪽y값)

​    

x = int(np.nanmean(xs) * 1920) = xs 평균값

y = int(np.nanmean(ys) * 1080) = ys(튜플) 평균값

(내가 보기엔 알 수 없는 형태로 돼있다 -> 숫자형으로 바꿔준다.)

​    

즉, 위 한 점⚫️은 최종적으로 정제된 x, y를 뜻한다.

​    

#

