## Java

​    

출처: https://mangkyu.tistory.com/94   

---

### Java의 장점과 단점 

- 장점
  - JVM 위에서 동작하기 때문에 운영체제에 독립적이다.
  - 가비지컬렉터가 메모리를 관리해주기 때문에 편리하다. (가비지 컬렉터는 jvm 실행엔진의 한 요소!)
- 단점
  - JVM 위에서 동작하기 때문에 실행 속도가 상대적으로 느리다.
  - 다중 상속이나 타입에 업격하는 등 제약이 있는 것이 많다.

---

### Java8 

Java8에서는 함수형 프로그래밍을 위한 stream API와 Lambda, 함수형 인터페이스 등과 Null-safe한 작업을 위한 Optional API, Date와 Time API 등이 추가되었습니다.

---

### 가비지 컬렉터(Garbage Collector)란? 

'더이상 참조되지 않는 메모리'인 가비지를 청소해주는 JVM의 실행 엔진의 한 요소입니다. JVM은 new와 같은 연산에 의해 새롭게 생성된 객체들 중에서 더이상 참조되지 않는 객체를 정리해줍니다. 가비지 컬렉터는 Heap 영역을 위주로 탐색하며 메모리를 정리해줍니다.

---

### synchornized란?

Java에서 지원하는 synchronized 키워드는 **여러 쓰레드가 하나의 자원을 이용하고자 할 때, 한 스레드가 해당 자원을 사용중인 경우, 데이터에 접근할 수 없도록 막는 키워드**입니다. synchronized 키워드를 이용하면 병렬 상황에서 자원의 접근을 안전하게 하지만, 자원을 이용하지 않는 쓰레드는 락에 의한 병목현상이 발생하게 됩니다.

- 메소드 synchronized: 한 시점에 하나의 쓰레드만이 해당 메소드를 실행할 수 있다.
- 변수 synchronized: 한시점에 하나의 쓰레드만이 해당 변수를 참조할 수 있다.

---

### Java의 List, Set, Map 차이 

- List
  - 데이터를 순차적으로 저장한다.
  - 데이터의 중복을 허용한다. 
  - 데이터로 null을 허용한다.
- Set
  - 순서없이 Key로만 데이터를 저장한다.
  - Key의 중복을 허용하지 않는다.
  - Key로 null을 허용하지 않는다.
- Map
  - 순서없이 Key, Value로 데이터를 저장한다.
  - Value는 중복을 허용하지만 Key의 중복을 허용하지 않는다.
  - Key로 null을 허용하지 않는다.

---

### Java의Vector와 ArrayList 차이

- Vector
  - 동기화를 지원한다.
  - 속도가 느리지만 병렬 상황에서 안전하다.
  - 크기가 증가하는 경우, 2배 증가함(10 -> 20)
- ArrayList
  - 동기화를 지원하지 않는다.
  - 속도는 빠르지만 병렬 상황에서 안전하지 않다.
  - 크기가 증가하는 경우, 1.5배 증가함(10 -> 15)

---

### Java의 StringBuffer와 StringBuilder 차이 

- StringBuffer
  - 동기화를 지원한다.
  - 속도가 느리지만 병렬 상황에서 안전하다.
- StringBuilder
  - 동기화를 지원하지 않는다.
  - 속도는 빠르지만 병렬 상황에서 안전하지 않다.

---

### 클래스(Class), 객체(Object), 인스턴스(Instance)의 개념 

- 클래스(Class): 객체를 만들어내기 위한 설계도 혹은 틀
- 객체(Object): 설계도(클래스)를 기반으로 선언된 대상, 클래스의 인스턴스라고도 부름
- 인스턴스(Instance): 객체에 메모리가 할당되어 실제로 활용되는 실체

---

### 오버로딩과 오버라이딩의 차이

오버로딩: 메소드의 이름은 같게 하되, 매개변수의 개수나 타입은 다르게 하는 것

오버라이딩: 부모 클래스로부터 상속받아 자식 클래스를 재정의하는 것

---

### 자바에서 Thread 구현 방법

Runnable 인터페이스를 구현하거나 Thread 클래스를 상속받아 run() 메소드를 오버라이딩한다.

---

## Object Oriented Programming

객체지향 프로그래밍이란 인간 중심적 프로그래밍 패러다임이라고 할 수 있다. 즉, **현실 세계를 프로그래밍으로 옮겨와 프로그래밍하는 것을 말한다.** **현실 세계의 사물들을 객체라고 보고** 그 객체로부터 개발하고자 하는 애플리케이션에 필요한 특징들을 뽑아와 프로그래밍 하는 것이다. 이것을 추상화라한다.

**OOP 로 코드를 작성하면 이미 작성한 코드에 대한 재사용성이 높다.** 자주 사용되는 로직을 라이브러리로 만들어두면 계속해서 사용할 수 있으며 그 신뢰성을 확보 할 수 있다. 또한 라이브러리를 각종 예외상황에 맞게 잘 만들어두면 개발자가 사소한 실수를 하더라도 그 에러를 컴파일 단계에서 잡아낼 수 있으므로 버그 발생이 줄어든다. 또한 내부적으로 어떻게 동작하는지 몰라도 개발자는 라이브러리가 제공하는 기능들을 사용할 수 있기 때문에 생산성이 높아지게 된다. 객체 단위로 코드가 나눠져 작성되기 때문에 디버깅이 쉽고 유지보수에 용이하다. 또한 데이터 모델링을 할 때 객체와 매핑하는 것이 수월하기 때문에 요구사항을 보다 명확하게 파악하여 프로그래밍 할 수 있다.

객체 간의 정보 교환이 모두 메시지 교환을 통해 일어나므로 실행 시스템에 많은 overhead 가 발생하게 된다. 하지만 이것은 하드웨어의 발전으로 많은 부분 보완되었다. 객체 지향 프로그래밍의 치명적인 단점은 함수형 프로그래밍 패러다임의 등장 배경을 통해서 알 수 있다. 바로 객체가 상태를 갖는다는 것이다. 변수가 존재하고 이 변수를 통해 객체가 예측할 수 없는 상태를 갖게 되어 애플리케이션 내부에서 버그를 발생시킨다는 것이다. 이러한 이유로 함수형 패러다임이 주목받고 있다.

---

[출처](https://www.javatpoint.com/corejava-interview-questions)

### 4) What do you understand by Java virtual machine?

[Java Virtual Machine](https://www.javatpoint.com/jvm-java-virtual-machine) is a virtual machine that enables the computer to run the Java program. JVM acts like a run-time engine which calls the main method present in the Java code. JVM is the specification which must be implemented in the computer system. The Java code is compiled by JVM to be a Bytecode which is machine independent and close to the native code.

#

### 5) What is the difference between JDK, JRE, and JVM?

### JVM

JVM is an acronym for Java Virtual Machine; it is an abstract machine which provides the runtime environment in which Java bytecode can be executed. It is a specification which specifies the working of Java Virtual Machine. Its implementation has been provided by Oracle and other companies. Its implementation is known as JRE.

JVMs are available for many hardware and software platforms (so JVM is platform dependent). It is a runtime instance which is created when we run the Java class. There are three notions of the JVM: specification, implementation, and instance.

### JRE

JRE stands for Java Runtime Environment. It is the implementation of JVM. The Java Runtime Environment is a set of software tools which are used for developing Java applications. It is used to provide the runtime environment. It is the implementation of JVM. It physically exists. It contains a set of libraries + other files that JVM uses at runtime.

### JDK

JDK is an acronym for Java Development Kit. It is a software development environment which is used to develop Java applications and applets. It physically exists. It contains JRE + development tools. JDK is an implementation of any one of the below given Java Platforms released by Oracle Corporation:

- Standard Edition Java Platform
- Enterprise Edition Java Platform
- Micro Edition Java Platform

---

