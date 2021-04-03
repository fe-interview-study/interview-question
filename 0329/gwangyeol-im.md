## Event Loop란 무엇인가요?

싱글 스레드로 동작하는 자바 스크립트 엔진을 비동기 처리를 관할하는 호스팅 환경과 상호 연동 시키는 매커니즘입니다. 이벤트 루프는 크게 태스크 큐, 마이크로 태스트 큐로 나누어지는 태스크 저장소를 가지고 있는데요, 전자에는 스크립팅, Web API 등이 들어간다면 후자에는 프로미스 관련 콜백이 들어가게 됩니다. 그리고 이벤트 루프는 전체적으로 스크립트 문 - 프로미스 콜백 - Web API 콜백 순으로 태스크를 다루어 동기적으로 실행되는 엔진 내부 호출 스택에 보내주게 됩니다. 이러한 작용으로 인해 결과적으로 해당 환경 내에서 이벤트들이 비동기적으로 처리됨을 확인할 수 있습니다.

## TCP와 UDP의 차이점은?

- TCP

  - 연결성 기반 프로토콜 방식
  - 신뢰성이 높다.
  - UDP보다 비교했을 때 속도가 느리다.

- UDP
  - 비연결성 기반 프로토콜 방식
  - 정보를 주고 받을 때 해당 신호절차를 거치지 않음
  - TCP 방식보다 빠르며 효율적이다.
  - 신뢰성이 낮다.

## 컴포넌트 라이프사이클이란 무엇이며, 어떻게 하면 함수 컴포넌트에서 라이프사이클을 유사하게 따라할 수 있는지 말해주세요.

컴포넌트 라이프사이클이란, 하나의 컴포넌트가 마운트 되고 언마운트 될 때까지 각각의 단계안에서 사용될 수 있는 연속적인 메소드로 정의할 수 있습니다. 두번째의 질문은 리액트로 프로그래밍을 잘 해보질 않아 이론적으로 설명을 해도 스스로 이해하기는 힘들 것 같습니다.

## 퀵소트의 최선/최악의 시간 복잡도를 설명하고 개선 방법을 설명하시오.

평균: nlogn / 최악: n^2 의 시간 복잡도를 가집니다. 이것의 시간 복잡도를 결정하는 기준은 피벗(pivot)의 값이 되는데 피벗의 값이 최소, 최댓값이고 데이터들이 정렬되어 있을 경우 최악의 시간 복잡도를 가지기 때문에 이러한 경우를 피해줄 수 있도록 예외 처리를 해주면 될 것 같습니다.

## 프로세스와 스레드의 차이는 무엇인가요? (단답형)

프로세스란, 컴퓨터에서 연속적으로 실행되고 있는 프로그램입니다. 프로세스는 각각 독립된 메모리 영역을 가지게 되고 이 영역은 Code, Data, Stack, Heap의 구조로 나누어집니다. 그리고 스레드는 하나의 프로세스 내에서 동작되는 여러 실행들의 흐름으로, 프로세스의 하위 단위입니다. 스레드는 Stack 영역만 따로 할당받고 나머지 영역은 공유하게 됩니다.