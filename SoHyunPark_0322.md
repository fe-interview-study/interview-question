## PS

### Hash

하나의 해시 테이블이 존재합니다. 해시 테이블에 계속해서 데이터를 넣게 되고 이렇게 넣게 되면 충돌이 일어날 것입니다.

충돌을 해결하기 위해서는 opening addressing 과 chaining 기법을 사용할 수 있지만 bucket은 한정되어 있어 opening addressing 방법을 사용할 수 없습니다.

또한 계속해서 데이터가 들어오기 때문에 chaining 기법을 사용하면 해시 테이블의 효율성이 줄어들게 됩니다.

그렇다면 이 상황에서 어떻게 해시 테이블을 설계를 해야 해시 자료구조가 가진 효율성을 높일 수 있을까요?

**[참고 그림]**

![https://user-images.githubusercontent.com/48006103/111300432-6acc7c80-8694-11eb-9313-a1ee6ec91f8e.png](https://user-images.githubusercontent.com/48006103/111300432-6acc7c80-8694-11eb-9313-a1ee6ec91f8e.png)

- 이건 정말 모르겠습니다....

## network

Q. holee는 검색을 하기 위해 브라우저 주소창에 다음과 같은 URL([https://www.google.com](https://www.google.com/)) 을 입력했다. 어떤 일이 발생할까?

입력된 url에 해당하는 ip 주소가 있는지 조회하기 위해 먼저 DNS 서버에 접근한다. 해당 ip 주소의 서버가 존재하면 그곳에 요청을 보내 소스 코드를 전달 받는다. 소스 코드를 전달 받으면 브라우저에서 먼저 html 을 DOM 트리로 파싱하고, css가 있다면 CSSOM 트리로 파싱한다. 이후 이 둘을 기반으로 렌더 트리를 생성하고, 스크립트가 존재하면 JS 엔진이 스크립트를 로드하고 실행한다. 

### 상세 답안

- URL을 웹 브라우저의 주소창에 입력한다.
- 웹 브라우저가 URL을 해석하고, 문법에 맞지 않으면 기본 검색엔진으로 검색한다.
- 문법에 맞으면 URL의 호스트 부분을 인코딩한다.
- HSTS(HTTP Strict Transport Security) 목록을 확인하고 있으면 HTTPS로, 없으면 HTTP로 요청한다.
- DNS(Domain Name Server) 조회
    - 브라우저/로컬 캐시 확인해서 도메인에 해당하는 IP가 있는지 확인한다.
    - 없으면 OS에게 DNS 서버에 요청하라고 지시한다.
    - DNS 서버는 해당 도메인에 해당하는 IP를 돌려준다.
- TCP 소켓을 열고 3-way handshake로 연결을 설정한다.
- HTTPS 요청이라면 TLS(Transport Layer Security) handshake 과정을 통해 세션키를 생성한다.
- 세션이 유지되는 동안 서버에게 요청하고 응답을 받는 과정을 반복한다.
    - 응답 상태코드에 따라 다르게 처리한다.
    - 응답을 디코딩(Decoding)하고 캐싱 가능하다면 캐싱한다.
- 웹브라우저는 응답받은 HTML/CSS/JS 및 이미지,폰트 등의 리소스를 사용하여 렌더링 한다.
- 서버와의 세션이 종료되면 4-way handshake로 연결을 종료한다.

브라우저 주소창에 [www.naver.com](http://www.naver.com/) 치면 -> 네이버 서버를 찾아간다. -> DNS(실제 서버가 어디에있는지 알고 있는 서버)가 연결해줄 곳을 찾음 -> (여기서 주소 앞에 https가 붙었다면 https방식으로 통신하겠다.) -> 서버의 기본설정이 대부분 index.html되어 있어 서버에서 이파일을 클라이언트로 보냄 -> 브라우저는 텍스트로 이루어진 index.html 파일을 파싱한다. -> 한줄한줄 읽으면서 DOM트리를 만들어나감. -> 중간에 link태그를 만나 css요청이 발생하면, 요청과 응답과정을 거치고 css를 파싱함 -> CSS파싱이 끝나면 중단된 html을 다시읽고 DOM트리를 완성 -> 완성된 DOM트리와 CSSOM트리를 합쳐 Render Tree를 만들고 그린다.javascript는? -> 중간에 HTML파서는 Script태그를 만나게 되면 javascript 코드를 실행하기 위해 파싱을 중단 -> 제어권한을 자바스크립트 엔진에게 넘기고, 자바스크립트 코드 또는 파일을 로드해서 파싱하고 실행

[출처1](https://github.com/baeharam/Must-Know-About-Frontend/blob/master/Notes/network/type-url-process.md)

[출처2](https://sunnykim91.tistory.com/121)

Q. HTTP 를 설명해주세요.

클라이언트와 서버가 데이터를 서로 주고 받기 위해 필요한 방식을 정의해둔 프로토콜. 특징은 아래와 같은 것들이 있다. 

- request, response 기반으로 동작한다. 각각은 헤더를 포함하는데, 이 헤더는 보내는 데이터에 대한 다양한 성질과 메타 데이터를 내포한다.
- 서버와 클라이언트 사이에는 다양한 엔티티와 계층이 존재할 수 있는데 이를 통칭 프록시라고 부른다.
- 기본적으로 stateless하다. 모든 요청은 독립적이며 서버 또한 누가 보내었는지를 반드시 특정해야 할 필요는 없다. 단 쿠키와 헤더를 이용하여 세션에 대한 명시를 하는 것은 가능하며, 이를 이용하여 연결성과 연관성 있는 요청들을 만들 수 있다.
- 주고받는 데이터는 평문이고, 이를 암호화하기 위해 https가 탄생했다.

## React

Q. 왜 state를 직접 변경하지 않고 setState를 이용하나요? (단답형)

우선 immutable하게 값이 바뀌어야 변화를 감지할 수 있고, 단순히 상태가 바뀌는 것만으로 리렌더링 되는 것이 아니라, setState를 통해 변화에 대한 신호가 있어야 reconciliation과정이 발생하기 때문. 

## OS

Q. Asynchronous, Synchronous, Blocking, NonBlocking

각각을 설명하고 synchronous 와 blocking이 어떻게 다른지 설명하시오.

- asynchronous vs synchronous: 작업이 종료되기 전 다른 작업을 진행할 수 있는지 없는지에 대한 차이. 
- non-blocking vs blocking: 하나의 함수나 흐름이 완료된 뒤에 다음 흐름으로 넘어가는지 아닌지에 대한 차이. 간단하게는 blocking 코드라면 하나의 함수가 종료되어 리턴이 된 뒤 그 다음 동작으로 넘어가겠지만, non-blocking 코드는 작업의 완료를 기다리지 않고 다른 작업을 진행할 수 있다. 
- 운영체제의 I/O 처리와 관련하여 쓰이는 용어로 자바스크립트에서는 경계가 모호하지만 POSIX에선 Asynchronous, Blocking, NonBlocking 이 함수로 구분되어 있다고 한다.
- Asynchronous 가 동시성을 갖는 작업에 대한 처리를 이야기하는 맥락이라면, non-blocking은 제어의 흐름을 막지 않는 맥락이라 중점을 두는 부분이 살짝 다를 수 있다. 
**조언을 구해본 내용**
- asynchronous blocking I/O - blocking I/O를 쓰지만 multi-threaded 방식을 통해 여러 입출력을 처리. 즉, 각 I/O를 담당하는 각 스레드의 제어 흐름은 중단되지만 스레드가 여러 개이기 때문에 여러 입출력을 처리 가능
- asynchronous non-blocking I/O - 운영체제 수준에서의 non-blocking I/O 또는 asynchronous I/O를 써서 구현. 즉, 스레드가 하나이더라도 각 I/O를 실행하는 운영체제 수준의 API가 제어 흐름을 중단시키지 않기 때문에 여러 입출력을 처리할 수 있다. 노드JS에서 여러 입출력을 처리하려면 이 방식을 써야 한다. 


## JS

Q. call, apply, bind란 무엇이며 이들의 공통점과 차이점은 무엇인가요?

- call: 특정 함수의 this객체를 변경하고 필요한 인자를 개별필요한 인자를 개별로 받는다.
- apply: 특정 함수의 this객체를 변경하고 필요한 인자를 배열로 받는다.
- bind: 인자로 넘겨받은 객체를 this로 하는 새로운 함수를 반환