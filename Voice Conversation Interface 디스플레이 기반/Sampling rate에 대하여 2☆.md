## Sampling rate에 대하여 2 

[출처](https://m.blog.naver.com/tipsware/220868928930) -> 공부를 위해 여기서 퍼왔다.

​    

**아날로그 형태**의 신호를  ->  **디지털 신호(디지털화된 정수값)**로 변경 or

디지털 형태의 신호를  ->  아날로그 형태로 변경

​    

펄스 형태의 신호를 디지털화한 숫자값으로 변경하려면 샘플링 작업을 수행해야하기 때문에  사운드카드의 입출력을 사용할 때는 필수적으로 샘플링 주기와 샘플링 비율을 명시해야 한다.

​    

<img src="../source/샘플링.PNG">

아날로그 신호는 위와 같다.

​    

위 신호를 디지털 신호로 변경하면 -60, -30, 12, 42, 63, ...과 같이 숫자값으로 변경이 되어야 한다.

사운드 카드는 이 작업을 아래와 같이 일정한 시간 간격으로 신호 세기를 추출하여 처리하는데, 이것을 '샘플링'이라고 한다.

즉 아날로그 형태의 신호에 점을 찍어 숫자 정수값으로 변형시키는 것을 샘플링이라고 한다.

<img src='../source/샘플링 주기.PNG'>

​    

당연한 이야기지만 아날로그 신호를 디지털 신호로 변경할 때 세밀하게 샘플링 할수록 더 정밀한 값을 얻을 수 있다..

그래서 사운드 카드에서는 1초당 몇번이나 샘플링 한 것인지 프로그래머가 정할 수 있는데, 이것을 '샘플링 주기'라 한다. 예를 들어 샘플링 주기가 8khz라고 하면 1초동안 8000번의 샘플링데이터를 추출한다는 뜻이다. 따라서 샘플링주기가 높으면 높을수록 디지털화된 데이터는 더욱더 정밀하게 표현된다.

​    

사실 아날로그 신호를 디지털로 변경해서 얻은 값은 절대값이 아니라 상대적인 값이다. 즉, 어떻게 기준을 정하느냐에 따라서 값이 달라질 수 있다는 뜻이다. +상한선 하한선도 정하기 때문에...

​    

. . .

​    

샘플링 주기와 샘플링 레이트가 클수록 샘플링된 값이 정밀해진다. 따라서 크게 설정하는 것이 좋겠지만, 정밀해지는 만큼 샘플링된 값을 저장할 메모리 공간이 많이 필요로 하게 된다.

결국 샘플링 주기와 샘플링 레이트는 저장 공간을 고려해야 하기 때문에 무조건 크게 설정하는 것이 아니라 자신이 원하는 작업에 맞게 잘 조절해서 사용하는 것이 좋다.



---

## 오류 가설 세우기

1. 라즈베리파이 기본 설정이 44,100 이였을수도.

   ㄴ이게 가장 유력

2. 아니면 오디오 장치마다 지원되는 샘플링 레이트가 달라서.

   (로컬pc에서 파이썬으로 개발을 진행하고 라즈베리파이에서 구동시키려 했는데 이 때 라즈베리파이 usb포트에 맞는 오디오 장치를 찾느라 계속 바꿨었다)

   ㄴ 하지만 이게 아닌듯. 

   ​    **일반 PC : 16,000 / 라즈베리파이 : 44,100 **

   ​    그런 논리라면 라즈베리파이에서가 훨씬더 높은 샘플링레이트를 보여주고 있기 때문에 낮은 품질의 오디오 파일이 깨져서라도 나오긴 했을 것. 

   하지만 cmd창에서 오류가 났기 때문에  장치의 기본 설정값이 달랐었던 것 같다. 그게 가장 유력한 것으로 볼 수 밖에 없다!

​    

**[결론]**; 장치마다 기본 설정값이 다 돼있음. 즉 라즈베리파이 기본 설정값이 44,100이였을 확률이 가장 크다는 뜻. (아래--를 참고하자)

''라즈베리파이'' 아니면  ''연결된 오디오 장치''의 기본설정값! 

연결 가능한 오디오 란에서  연결한 오디오 장치를 택할 수 있고, 그의 샘플링레이트도 조절할 수 있기에. . 그 기본 설정값이 44,100이였던 것이다

아니면 라즈베리파이에는 출력 장치가 기본적으로 내장돼 있는데 그의 기본값이 44,100이였던 것, 

#

**ALSA 라이브러리 오류: Invalid Sample rate ERROR**

https://m.blog.naver.com/tipsware/220868928930

다시 한번 말하자면 ALSA 는 사운드 입출력을 사용하기 위한 라이브러리다.

라즈베리파이에서 사운드 입출력 프로그래밍을 하려면 관련 라이브러리를 설치해야 한다. 사운드 입출력시에 많이 이용하는 ALSA 라이브러리.

*참고로 사운드카드란, 음향을 출력하기 위한 PC 부품의 일종이라 생각하면 된다.

그럼 라즈베리파이 기본 설정 자체라기 보단.. (여기 내장돼있는 출력장치 기본 설정이 그랬다면 그것도 가능성이 있지만)

USB로 연결한 오디오장치일 가능성이 가장 크다. 그 오디오장치의 기본 셋팅이 44,100으로 되어있던 것.

​    

```tex
44.1 kHz
Audio sampling frequency (Hz)
By default, the sampling frequency of ALSA Audio Capture is the same as the sampling frequency of ALSA Audio Playback. This parameter value defaults to 44100 Hz (44.1 kHz). The maximum rate equals the sampling rate of the audio capture device.
```

위를 읽어보면 기본적으로 ALSA 오디오 샘플링 주기는 기본적으로 44100 Hz이다. 

​    

- I can't seem to find a configuration for ALSA to set output sampling rate. How can I configure it?

  -> Alsa by default uses the same sampling rate and format as the source. It is however possible to force the sample rate up (or down).

  Here is one way you could do it. (in **/etc/asound.conf** or **~/.asoundrc**)

  ```
  pcm.device{
          format S24_LE
          rate 96000
          type hw
          card 0
          device 0
  }
  ```


**[최종 결론]**; 사운드 카드의 기본 설정값 rate가 44,100이였을 것으로 최종 결론

alsa 라이브러리 오류였기 때문에 사운드카드의 오류임이 크고, 사운드카드는 따로 연결한 오디오장치나 스피커장치이기 때문에. 그 기본 설정값이 달라서. 라즈베리파이 pc 자체의 샘플레이트 자체가 문제가 아니라.

#

샘플렝레이트가 클수록 찍는 점이 훨씬 많아지기 때문에 정확도나 품질이 더 올라감. 다만 용량 과부하 발생. 

​    

---

## 라즈베리파이에서 usb마이크, 스피커 설정하기

[출처1](https://diy-project.tistory.com/88)  [official 출처2](https://developers.google.com/assistant/sdk/guides/library/python/embed/audio)

라즈베리파이에는 오디오 출력 단자는 있지만 입력단자가 없어 일반적인 마이크를 사용하기에 좀 불편하다. 그래서 USB 형태로 된 마이크가 필요하다. 

​    

- <명령어>  입력: a리코드  /  출력: a플레이 

```
$ arecord -l 🟨
```

우선 위 명령을 실행하여 연결 가능한 **마이크**를 검색🟨한다. 그럼 아래와 같이 출력된다.

```
**** List of CAPTURE Hardware Devices ****
card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

​       

이제 card 1과 device 0라는 점을 잘 기억해둔 뒤 아래 명령을 통해 **스피커**를 검색🟨한다.

```
$ aplay -l 🟨
```

아래와 같이 출력된다.

```
**** List of PLAYBACK Hardware Devices ****
card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
  Subdevices: 7/7
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

​     

여기서 USB 장치는 card 1에 device 0으로 설정되어있다. 이제 나노 편집기로 파일하나를 만든다.

```
$ nano .asoundrc
```

​     

빈파일에 아래의 형식에 맞추어 입력한다.

```
pcm.!default {
  type asym
  capture.pcm "mic"
  playback.pcm "speaker"
}
pcm.mic {
  type plug
  slave {
    pcm "hw:<card number>,<device number>"
  }
}
pcm.speaker {
  type plug
  slave {
    pcm "hw:<card number>,<device number>"
  }
}
```

 

card number와 device number는 위에서 알아냈으므로 필자와 같은 상태라면 아래와 같이 입력하면 된다. 

```
pcm.!default {
    type asym
    capture.pcm "mic"
    playback.pcm "speaker"
}
pcm.mic {
    type plug
    slave {
        pcm "hw:1,0"
    }
}
pcm.speaker {
    type plug
    slave {
        pcm "hw:1,0"
    }
}
```

 

이렇게 입력했다면 저장하고 빠져나온다. 스피커를 테스트 해보고 싶다면 아래와 같이 입력하자.

```
$ speaker-test -t wav
```

 

위 명령을 실행하면 스피커에서 Front, Left가 반복되어 재생된다. 마이크를 테스트 하려면🟨 arecord -> 오디오 입력장치

```
$ arecord🟨 --format=S16_LE --duration=5 --rate=16000🟨 --file-type=raw out.raw
```

를 실행시켜 녹음을 한 뒤에

```
$ aplay --format=S16_LE --rate=16000🟨 out.raw
```

 

를 실행시켜 녹음된 소리를 들어보면 된다. 만약 소리가 너무 작거나 크다면 아래 명령을 통해 조절할 수 있다.

```
$ alsamixer
```

---

stt모듈에는 sample rate 설정하는 부분이 있는데 tts모듈에는 설정하는 부분이 따로 없었다.

---

## + 그리고 aliasing에 대해서... (앨리어싱)

[출처](http://www.alanjshan.com/sampling-01/)

**“우리가 샘플 (sample) 하려는 소리의 가장 높은 주파수보다 (Highest frequency)**

**2배 이상의 샘플링 속도 (Sampling Rate)를 사용하면 정확하게 소리를 다시 만들어 낼 수 있다.** 

**(아날로그에서 디지털로, 디지털에서 아날로그로)”**

​    

사람의 귀로 들을 수 있는 **가청주파수**는 약 20~20,000Hz에 이른다.  2만 헤르츠

​    

즉 우리가 만약에 1kHz 주파수를 녹음하고 싶다면 최소 2kHz Sampling Rate 를 사용해야 한다는 것.

​      

사람의 가청 주파수는 20Hz 부터 20kHz까지 입니다. 최소한 인체학 적으로 귀를 통하여 들을 수 있는 소리의 가청 주파수 입니다. 즉, 사람이 듣기위한 소리를 녹음하기 위해서는 40 kHz sampling rate 이상을 사용하면 됩니다.

---

