## PS

### Hash

하나의 해시 테이블이 존재합니다. 해시 테이블에 계속해서 데이터를 넣게 되고 이렇게 넣게 되면 충돌이 일어날 것입니다.

충돌을 해결하기 위해서는 opening addressing 과 chaining 기법을 사용할 수 있지만 bucket은 한정되어 있어 opening addressing 방법을 사용할 수 없습니다.

또한 계속해서 데이터가 들어오기 때문에 chaining 기법을 사용하면 해시 테이블의 효율성이 줄어들게 됩니다.

그렇다면 이 상황에서 어떻게 해시 테이블을 설계를 해야 해시 자료구조가 가진 효율성을 높일 수 있을까요?

**[참고 그림]**

![https://user-images.githubusercontent.com/48006103/111300432-6acc7c80-8694-11eb-9313-a1ee6ec91f8e.png](https://user-images.githubusercontent.com/48006103/111300432-6acc7c80-8694-11eb-9313-a1ee6ec91f8e.png)

이중 해싱을 만든다.

## network

Q. holee는 검색을 하기 위해 브라우저 주소창에 다음과 같은 URL([https://www.google.com](https://www.google.com/)) 을 입력했다. 어떤 일이 발생할까?

문제를 낸 이유: 아래 과정을 상세히 말하면 하루로도 부족하다. 흐름제어부터 커널 버퍼, user space, 동기 비동기 블록킹, call stack, 브라우저 렌더링 과정 모든 지식이 다 나올 수 있는 질문이라고 생각합니다. 저는 이 스터디가 끝나는 날에 1시간 동안 이 질문에 대해서 답해보겠습니다.. 지금은 지식이 없으므로 패스..

1. 주소표시줄에 URL을 입력하고 Enter를 입력한다.
2. 웹 브라우저가 URL을 해석한다.

```
scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
```

3. 만약, URL이 문법에 맞지 않는다면 입력을 웹 브라우저의 기본 검색엔진으로 검색을 요청한다.
4. URL이 문법에 맞으면 Punycode encoding을 url의 host부분에 적용한다.
5. HSTS (HTTP Strict Transport Security)목록을 로드해서 확인한다.
6. DNS(Domain Name Server) 조회한다.
7. ARP(Address Resolution Protocol)로 대상의 IP와 MAC address를 알아낸다.
8. 대상과 TCP 통신을 통해 Socket을 연다.
9. TLS(Transport Layer Security) handshake
10. HTTP 프로토콜로 요청한다.
11. HTTP 서버가 응답한다.
12. 웹 브라우저가 그린다. 

Q. HTTP 를 설명해주세요.

The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems.

HTTP(Hypertext Transfer Protocol)는 분산, 협업, 하이퍼 텍스트 정보 시스템을 위한 비상태 애플리케이션 레벨 프로토콜이다.

[RFC 7230](https://hochan049.gitbook.io/cs-interview/web/rfc-7320)에 명시되어 있다.

## React

Q. 왜 state를 직접 변경하지 않고 setState를 이용하나요? (단답형)

this.state는 컴포넌트를 다시 렌더링 하지 않기 때문입니다. (this.state를 지정할 수 있는 유일한 공간은 바로 constructor입니다.)

---

컴포넌트를 다시 렌더링 하지않는 이유는 다음과 같습니다.

- 일괄적으로 처리하기 위함입니다.

  모든 컴포넌트가 자신의 이벤트 핸들러에서 setState()를 호출할 때까지 React는 다시 렌더링을 하지 않고 내부적으로 기다리게 만들기 위함인데, 이를 통해 불필요한 렌더링을 방지하면서 성능을 향상시킵니다. 즉, setStat()를 동기식으로 다시 렌더링하는 것이 대부분의 경우 비효율적일지라도 일괄 업데이트하는 것이 좋습니다.

  하지만, 항상 일괄적으로 처리되지는 않습니다. React는 현재 React가 관리하는 이벤트 핸들러 내부에서 업데이트를 일괄 처리합니다. React는 최상위 호출 스택 프레임에서 모든 React 이벤트 핸들러가 언제 실행되었는지 알고 있기 때문입니다. 이 시점에서 업데이트를 플러시합니다. 이벤트 핸들러가 React에 의해 설정되지 않은 경우 현재 업데이트를 동기화합니다. 기다리는 것이 안전한지 여부와 다른 업데이트가 곧 발생할지 여부를 알 수 없기 때문입니다.

  향후 React 버전에서는이 동작이 변경 될 것이며, 계획은 기본적으로 업데이트를 낮은 우선 순위로 처리하여 통합 및 일괄 처리 (예 : 1 초 이내에)하고 즉시 플러시하도록 선택하는 것입니다.

- props 와 state 사이의 일관성을 해칠 수 있기 때문이며, 이는  디버깅하기 매우 힘든 이슈를 일으킬 수 있고, 현재 작업중인 새로운 기능들을 구현하기 힘들게 만들 수 있습니다.

- setState를 사용하면 업데이트를 항상 발생하는 순서대로 효율적으로 얕게 병합할 수 있습니다.

```# 참고```
- https://ko.reactjs.org/docs/faq-state.html
- https://github.com/facebook/react/issues/11527#issuecomment-360199710 

## OS

Q. Asynchronous, Synchronous, Blocking, NonBlocking

각각을 설명하고 synchronous 와 blocking이 어떻게 다른지 설명하시오.

> Everything is a File.

Linux/Unix에서는 socket도 하나의 파일(File), 더 정확히는 File Descriptor(FD, 파일 디스크립터)입니다. 이처럼 Low Level File Handling 기반으로 socket 기반의 데이터 송수신이 가능합니다. I/O 작업은 단순히 단일 server 내에서 일어나는 읽기/쓰기 뿐만 아니라 Server-Client 간 네트워크 통신에도 적용되는 개념입니다.

I/O 작업은 user space에서 직접 수행할 수 없기 때문에 user process가 kernel에 I/O 작업을 '요청'하고 '응답'을 받는 구조입니다. 응답을 어떤 순서로 받는지(synchronous/asynchronous), 어떤 타이밍에 받는지(blocking/non-blocking)에 따라 여러 모델로 분류됩니다.

### Synchronous, 동기 

- 모든 I/O 요청-응답 작업이 일련의 순서를 따릅니다. 즉, 작업의 순서가 보장됩니다.
- 작업 완료를 user space에서 판단하고 다음 작업을 언제 요청할지 결정하게 됩니다.
- 일련의 Pipeline을 준수하는 구조에서 효율적입니다.

<img src="https://user-images.githubusercontent.com/22424891/111920168-e6815b80-8ad0-11eb-98f5-6a95bcf5deca.png" height="150px" />

### Asynchronous, 비동기 

- kernel에 I/O 작업을 요청해두고 다른 작업 처리가 가능하나, 작업의 순서는 보장되지 않습니다.
- 작업 완료를 kernel space에서 통보해 줍니다.
- 각 작업들이 독립적이거나, 작업 별 지연이 큰 경우 효율적입니다.

<img src="https://user-images.githubusercontent.com/22424891/111920210-1cbedb00-8ad1-11eb-93e3-63d68621decb.png" height="150px" />

### Blocking, 블로킹 

- 요청한 작업이 모두 완료될 때까지 기다렸다가 완료될 때 응답과 결과를 반환받습니다. [대기 有]
- 요청한 작업 결과를 기다립니다.

### Non-Blocking, 넌-블로킹 

- 작업 요청 이후 결과는 나중에 필요할 때 전달받습니다. [대기 無]
- 요청한 작업 결과를 기다리지 않습니다.
- 중간중간 필요하면 상태 확인은 해볼 수 있습니다. (polling)

OS 환경에 따라서 세부적인 기법 차이가 있지만 Linux 기반의 I/O 모델을 우선으로 살펴보았을때, 아래는 IBM Developer의 I/O 모델 분류표입니다.

<img src="https://user-images.githubusercontent.com/22424891/111920507-be92f780-8ad2-11eb-8654-575fb42fe650.png" height="300px" />

- Synchronous Blocking I/O → Blocking I/O
- Synchronous Non-Blocking I/O → Non-Blocking I/O
- Asynchronous Blocking I/O → I/O Multiplexing
- Asynchronous Non-Blocking I/O → Asynchronous I/O

> I/O Multiplexing이 Asynchronous Blocking 방식인지에 대해 다양한 의견이 있다. 구현 방식에 따라 차이가 있지만 관점 주체에 따라 Blocking/Non-Blocking이 갈리기도 하며, 실제 I/O 동작은 Synchronous 방식으로 동작한다. 심지어 각 기법에 따라 세부적인 로직 및 알림 방식도 달라지기 때문에 Multiplexing을 단순히 Asynchronous Blocking 방식이라고 딱 잘라 정의하기엔 무리가 있다. 따라서 각 기본 개념만 숙지한 채 I/O Mutliplexing은 큰 분류가 아닌 세부 기법을 위주로 이해해야한다.

### Blocking I/O (Synchronous Blocking I/O)

<img src="https://user-images.githubusercontent.com/22424891/111920684-ab345c00-8ad3-11eb-89bc-e6b99afbc6cd.png" height="300px" />

가장 흔하게 생각할 수 있는 I/O 모델로 user space에 존재하는 process는 kernel에게 I/O를 요청하는 함수를 호출(system call) 한 뒤 kernel이 작업 결과를 반환하기까지 중단된 채 대기(block) 합니다. 이때 user process는 CPU를 점유하지 않고 kernel의 응답만 기다립니다.

이 과정에서 signal에 의해 system call이 중지될 순 있으나, 그렇지 않다면 kernel의 응답이 되돌아옴과 동시에 반환된 데이터가 user space의 buffer로 돌아오게 되고(synchronous) 그제서야 user process는 unblocking되어 반환받은 데이터를 처리할 수 있게 됩니다.

호출할 때마다 요청 thread를 생성하므로 I/O 요청이 적은 서비스엔 적합하지만, 만약 요청 수가 많아진다면 한 작업 당 한 번의 context switching이 발생하기에 비효율적입니다. 또한 block 된 user process는 CPU를 사용하지 않고 kernel 응답만 기다리게 되는 것인데, I/O 작업은 CPU 자원을 거의 쓰지 않기 때문에 리소스 사용 효율이 좋지 못합니다.

### Non-Blocking I/O (Synchronous Non-Blocking I/O)

<img src="https://user-images.githubusercontent.com/22424891/111920788-4b8a8080-8ad4-11eb-9188-6f4782fa1d41.png" height="300px" />

Non-block 하게 동작하게끔 구성할 땐 socket 생성 시 O_NONBLOCK 옵션을 줘서 구성합니다. 해당 socket으로 I/O system call을 하게 되면 block 되는 것이 아닌 즉시 결과를 반환받습니다. 아직 읽을 데이터가 없다면 바로 -1을 반환하며 그 실패의 유형은 오류 코드(errno)로 구분합니다. 일반적으로 EAGAIN 또는 EWOULDBLOCK을 반환받게 됩니다.

수행 결과와 errno를 즉시 받아보고 더 물어볼지 말지를 결정하기 때문에 I/O 작업이 완료되지 않아도 user process는 block 되지 않습니다. 요청한 system call에 대해 kernel이 user process를 무한정 기다리게 하는 게 아니라 아직 덜됐으면 덜됐다고 물어볼 때마다 알려주는 것이기 때문입니다.

Non-Blocking 기반인 경우엔 적정한 polling 주기가 필요한데 주기가 너무 길 경우엔 실제 데이터는 다 준비되었음에도 후속 처리가 늦어질 수 있고, 주기가 너무 짧다면 kernel 입장에선 의미 없는 return을 자주 해줘야 하니 오히려 I/O 작업의 지연을 초래할 수 있습니다.

앞서 살펴본 Synchronous 모델은 Blocking이든 Non-Blocking이든 결국 요청한 순서대로 작업을 완료시킵니다. 이런 방식은 직관적이긴 하지만 2개 이상의 파일을 동시에 처리할 때는 multi-process 또는 multi-thread로 동작해야 합니다. 하지만 multi-process 환경에선 IPC나 동기화(Semaphore, Mutex 등)를 고려해야만 하기 때문에 복잡한 이슈가 생기기 마련입니다. 그 때문에 Multiplexing, 즉 다중화 기법이 각광받게 됩니다.

### I/O Multiplexing (멀티플렉싱, 다중화 Asynchronous Blocking I/O)

'다중화'의 의미가 뭔지부터 생각해 봅시다. 간단하게 '하나'를 '여러 개'처럼 보이게 동작하게 한다는 뜻입니다. 이를 I/O 관점에서 해석하면 '한 프로세스가 여러 파일(file)을 관리'하는 기법이라 볼 수 있습니다. 파일은 프로세스가 kernel에 진입할 수 있도록 다리 역할을 하는 인터페이스입니다. server-client 환경이라면 하나의 server에서 여러 socket 즉, 파일을 관리하여 여러 client가 접속할 수 있게 구성됩니다. socket 또한 IP/Port를 가진 파일일 뿐입니다.

프로세스에서 특정 파일에 접근할 때는 파일 디스크립터(이하 FD, File Descriptor)라는 추상적인 값을 사용하게 되는데, 이 FD들을 어떻게 감시하냐는 게 I/O Multiplexing의 주요 맹점이라 할 수 있겠습니다. 여기서 어떤 상태로 대기하냐에 따라 select, poll, epoll(linux), kqueue(bsd), iocp(windows) 등 다양한 기법들이 등장합니다.

우선 앞선 IBM 분류 기준에서 Asynchronous blocking I/O로 제시된 모델을 살펴보고 세부 기법으로 들어가 보면,
위 구조는 kernel은 I/O 요청을 받으며 처리를 시작함과 동시에 user process에게 미완료 상태를 반환하고 user process는 데이터가 준비됐다는 알람이 올 때까지 대기하는 모습을 보여주고 있습니다. 여기서 blocking 인지 non-blocking 인지부터 헷갈리는데 명확히 구분하자면 user process에서의 read, write 같은 I/O 작업 자체가 block 되는 것이 아니라 select, poll 같은 mutliplexing 관련 system call에 대한 kernel의 응답이 block 된다고 봐야 합니다. I/O Multiplexing을 마냥 Asynchronous Blocking 기법으로 분류하기엔 혼동 여지가 있는 이유 중 하나입니다. 여기선 첫 read 요청에 대해 즉각 미완료 상태를 반환받는 Non-blocking socket의 동작을 보여주는데, select의 결과에 따라 read/write system call을 수행하게끔 구현하면 위 그림에서 Non-Blocking 요소를 없앨 순 있습니다. 다만, 데이터가 checksum 실패로 폐기되는 등의 일부 상황에선 select()가 어떤 FD에 데이터 있으니 읽으라고 알려와서 읽었다가 socket이 Block 되는 상황이 발생할 수 있습니다. 이런 상황에선 데이터를 받는 socket을 Non-Blocking으로 구성하여 EWOULDBLOCK error만 return 하고 넘어가게끔 설계하여 안전성을 높일 수 있습니다.

이어서, kernel의 응답을 기다리다 보면 kernel에서 결과 값이 준비되었다는 callback 신호가 오고 user process는 자신의 buffer로 데이터를 복사해오는 모습을 보여주는데, 사실 select 방식의 실제 구현으로 들어가면 select 호출 결과가 유의미한 값으로 나올 때까지 user process에서 loop를 돌리며 대기하는 방식입니다. 결국 select를 요청한 user process가 return 받은 값을 보고 후속 작업 유무를 판단하는 것입니다. 예측할 수 없게 인입되는 여러 I/O 요청을 한 번에 관리할 수 있어 Asynchronous 하다고 보는 경우도 있지만 결국 실제 I/O 동작은 Synchronous 한 동작을 보입니다.

이 부분 또한 혼동 여지가 있기에 I/O Multiplexing 모델에 대한 개념적 구분은 여기서 줄이도록 합니다. 해당 그림은 I/O Multiplexing을 적용할 수 있는 하나의 예시이며, select 같은 기법으로 여러 I/O 작업을 독립적으로 관리할 수 있다고만 이해하고 넘어가도록 합니다.

- select (Level-Triggered)
- pselect
- poll
- ppoll
- epoll (Edge-Triggered)

### Asynchronous I/O (AIO, Asynchronous Non-Blocking I/O)

<img src="https://user-images.githubusercontent.com/22424891/111921633-f0a75800-8ad8-11eb-9fc4-94385b78fae7.png" height="300px" />

Asynchronous I/O 환경에서 user process는 system call 이후 I/O 처리에 신경 쓰지 않고 있다가 작업이 완료되면 kernel로부터 signal, thread 기반 callback 등으로 결과를 마치 event처럼 전달받게 됩니다. 그렇기에 응답이 오기 전까지 user process는 I/O와 독립적인 다른 processing이 가능한 구조입니다.

## JS

Q. call, apply, bind란 무엇이며 이들의 공통점과 차이점은 무엇인가요?

- 공통점
  - call,apply,bind는 함수의 메서드(프로퍼티)입니다.
  - call,apply,bind 메서드는 사용자가 직접 외부 this를 넣음으로써 실행영역을 지정하며 작동합니다.

- 차이점
  - call은 보통함수와 똑같이 인자를 넣고 apply는 인자를 하나로 묶어 배열로 만들어 넣습니다.
  ```js
  var example = function (a, b, c) {
    return a + b + c;
  };
  example(1, 2, 3);
  example.call(null, 1, 2, 3);
  example.apply(null, [1, 2, 3]);
  ``` 
  - call,apply는 인수가 없을 경우, 자동적으로 전역객체를 가리키게 된다.
  - call, apply는 그냥 함수가 실행되도록 호출하지만 bind 는 호출은 하지않고 새로운 함수를 반환합니다.
