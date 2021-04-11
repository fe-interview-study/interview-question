### 1. [JS]  Event Bubbling, Capturing에 대해서 설명해 주세요



이벤트 버블링은 이벤트가 발생 했을 때 그 이벤트가 상위 요소들로 전달되는 것을 말합니다.

이벤트 캡쳐링은 반대로 상위 요소에 이벤트가 발생하면 하위 요소들로 이 이벤트가 전달되는 것을 말합니다.

![event](https://blueshw.github.io/static/137b0f890dd0d1d21a6c40b0aeafe49a/fcda8/event.png)



### 2. [Network] CORS란 무엇이며 왜 이 스펙을 사용하는 것일까?



CORS 는 Cross Origin Resource Sharing 의 약자로 교차 출처 리소스 공유를 말합니다. 

기본적으로 XMLHttpRequest 와 fetch api 는 same origin policy 정책을 따르기 때문에 서로 다른 출저 간에 리소스를 주고 받을 수 없습니다.

따라서 다른 출처(origin) 간에 리소스를 공유할 수 있도록 해주는 CORS 설정을 http 헤더에 추가할 수 있습니다.



### 3. [React] useEffect 와 useLayoutEffect의 차이점에 대해서 설명해주세요

`useEffect`와 `useLayoutEffect`의 차이점은 실행 시점에 있습니다. 

`useEffect` 는 렌더가 화면에 그려진 후 비동기적으로 실행되지만, `useLayoutEffect` 는 화면이 렌더가 화면에 반영 되기 전에 실행됩니다.

useEffect 훅을 사용할 경우 **DOM의 레이아웃 배치와 페인트가 끝난 후** 이펙트 함수를 호출 



useEffect를 쓰면 깜빡이는 문제가 발생할 수 있다. 



참고링크 : https://merrily-code.tistory.com/46 

### 4. [PS] pivotal(대각선이 고정인 행렬) 3x3, 4x4를 뒤집는 로직을 짜보자





![IMG_110AF624A7FD-1](/Users/heeje/Downloads/IMG_110AF624A7FD-1.jpeg)

