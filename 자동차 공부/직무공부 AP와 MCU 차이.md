## AP(Application Processor) 기반 

- **라즈베리파이**(작은 pc)가 해당.  처리속도 높음. 
- 스마트폰, 디지털TV등에 사용되는 비메모리 반도체로 일반 컴퓨터의 중앙처리장치(CPU)와 같은 역할로 핵심 기능을 담당.
- CPU기능뿐 아니라 다른 장치를 제어하는 칩셋의 기능을 포함한다. 즉 스마트폰이나 태블릿PC등에 필요한 OS, 어플을 구동(CPU), 여러가지 시스템 장치/인터페이스를 컨트롤하는 기능을 하나의 칩에 모두 포함하는 System-on-Chip.

​    

##  MCU(Micro Controller Unit) 기반

- 아두이노가 해당.  성능과 처리속도는 낮음.

- ★Non OS -> Firmware 필요

- 특정 시스템을 제어하기 위한 전용 프로세서.

- 마이크로프로세서와 입,출력 모듈을 하나의 칩으로 만들어져 정해진 기능을 수행하는 컴퓨터.

- 임베디드 시스템에 널리 사용됨.

  -> 기능을 설정하고 정해진 일을 수행하도록 프로그래밍 되어 장치 등에 장착되어 동작.

---

​    

## CPU vs AP

<IMG src="../source/cpu ap.png">

컴퓨터의 cpu처럼

스마트폰에는 ap(어플리케이션 프로세서)가 들어있음

*출처: 'CPU 시장을 넘보는 시스템 반도체 AP(Application Processor)' 유튜브

​    

---

## Application Processor(컴퓨터 부품)

AP는 단순히 CPU만이 아닌 GPU등 주요 부품들의 집약체이다. APU와 다르다.

자세한 내용은 SoC 참조.

SoC는 ‘시스템 온 어 칩 (**S**ystem **o**n a **C**hip)’의 약자로 한 개의 칩에 완전 구동이 가능한 제품과 시스템이 들어 있는 것을 말한다. 즉, 하나의 칩 내에서 CPU, GPU, RAM, ROM 등의 다양한 역할을 구현하는 체제이다. 통상적으론 **SoC**라고 많이 쓰인다. 하지만 사전적, 표준형으론 So'a'C라고 표현한다.

SoC는 주로 **모바일 기기, 아두이노**와 같은 전력 소비가 적은 즉 **저전력 소비 디바이스**에 효율적으로 사용된다. 

​    

​    

AP (Application Processor)의 정의는 불명확하다. 애플이 아이폰용 프로세서를 만들면서 만든 이름인 것 같다.



임베디드 시스템에서는 전통적으로 프로세서를 MPU (Microprocessor)와 MCU (Microcontroller)로 구분한다. MPU는 마이크로 프로세서이고 MCU는 마이크로 프로세서에 주변장치와 메모리를 결합한 IC이다.



MCU = SoC (Silicon on Chip)라고 볼 수도 있다. MPU와 MCU는 아주 오래 전부터 있던 용어이고 SoC는 최근에 나온 개념이다.



AP를 기존의 관점에서 보면 MCU 또는 SoC이다.



AP를 Mobile Application Processor로 표현하는 경우가 많다. 즉, AP는 **스마트폰에 특화된** MCU 또는 SoC라고 보는 것이 맞는 것 같다.

[출처](https://article2.tistory.com/608)

