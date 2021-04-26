- call, apply, bind란 무엇이며 이들의 공통점과 차이점은 무엇인가요?

- `this` 가 참조할 컨텍스트를 명시적으로 바인딩해주기 위해 필요한 메소드입니다. 이들의 공통점은 앞서 말했다시피, 특정한 객체를 바인딩해줄 수 있다는 것이고 차이점은 다음과 같습니다.

1. `call` - `apply`: 매개 변수를 보내는 방식이 다릅니다. 전자는 오직 하나, 후자는 배열로 여러 인자를 보낼 수 있습니다.
2. `bind`: `apply`의 하드 바인딩 버전으로, 바인딩된 새로운 함수를 반환하고 해당 함수에 여러 인자를 보낼 수 있습니다.

- 왜 state를 직접 변경하지 않고 setState를 이용하나요? (단답형)

- 리액트의 콘셉트 내에서 상태 객체는 불변성을 유지해야하며, 그 이유는 다음과 같습니다.

1. 상태의 변화를 쉽게 tracking 하고, 참조값으로 인한 의도치 않은 렌더링 오류를 방지하기 위해서
2. 렌더링 시 이전 상태와 현재 상태 객체의 얕은 비교(only 주소값)를 위해서

- Asynchronous, Synchronous, Blocking, NonBlocking 각각을 설명하고 synchronous 와 blocking이 어떻게 다른지 설명하시오.

1. Blocking / Non-blocking ; 호출된 함수가 바로 `return` 을 하는가, 안하는가가 관심사입니다.
   - Blocking - 호출된 함수가 자신이 할 일을 모두 마칠 때까지 제어권을 가지는 것
   - Non-blocking - 호출된 함수가 자신이 할 일을 마치지 않더라도 `return` 해서 제어권을 건네주는 것
2. Synchronous / Asynchronous ; 호출된 함수의 작업 완료 여부를 누가 신경쓰는 지가 관심사입니다.
   - Synchronous - 스스로 계속 작업 완료 여부를 확인하며 신경 쓴다.
   - Asynchronous - 호출된 함수가 callback function 을 받아 작업이 완료되면 전달받은 callback을 실행하여 호출된 함수가 작업 완료 여부를 신경 쓰지 않는다.

- HTTP 를 설명해주세요.

- Hyper Text Transfer Protocol 의 줄임말로, 클라이언트 - 서버 간 리소스를 주고 받기 위해 존재하는 프로토콜입니다.
