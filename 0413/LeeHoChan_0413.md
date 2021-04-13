### 1. [JS]  Event Bubbling, Capturing에 대해서 설명해 주세요

현재 event target으로부터 상위 요소로 전파되는 과정을 Event Bubbling이라고 합니다. Event Capturing는 반대로 현재 event target에서 하위 요소로 전파되는 과정입니다. 이런 과정속에서 할당된 Event Handler가 호출됩니다.

### 2. [Network] CORS란 무엇이며 왜 이 스펙을 사용하는 것일까?

origin이 다른 출처의 리소스를, 즉 스킴, 호스트, 포트가 다른 리소스들을 실행중인 웹 애플리케이션이 접근 할 수 있는 권한을 부여받도록 브라우저에게 알려주는 체제입니다.

보안 상의 이유로, 브라우저는 스크립트에서 시작한 교차 출처 HTTP 요청을 제한합니다. 예를 들어, XMLHttpRequest와 Fetch API는 동일 출처 정책을 따릅니다. 즉, 이 API를 사용하는 웹 애플리케이션은 자신의 출처와 동일한 리소스만 불러올 수 있으며, 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 CORS 헤더를 포함한 응답을 반환해야 합니다.

### 3. [React] useEffect 와 useLayoutEffect의 차이점에 대해서 설명해주세요

useLayoutEffect와 useEffect의 가장 큰 차이는 렌더링 시점에 있습니다. useEffect는 화면에 그려진 후 실행되고, useLayoutEffect는 브라우저가 화면을 그리기 이전 시점에 실행됩니다.

다만, 서버 렌더링을 사용하는 경우라면 자바스크립트가 모두 다운로드될 때까지는 useLayoutEffect와 useEffect 어느 것도 실행되지 않는다.

### 4. [PS] pivotal(대각선이 고정인 행렬) 3x3, 4x4를 뒤집는 로직을 짜보자

https://gist.github.com/hochan222/f3407f9db47e3237cbd82539525fce60
