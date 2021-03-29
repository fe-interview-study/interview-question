## JS
### 질문
Event Loop란?

### 답

![](https://miro.medium.com/max/2048/1*4lHHyfEhVB0LnQ3HlhSs8g.png)
자바스크립트는 싱글 스레드 프로그래밍 언어인데, 상식적으로 싱글 스레드 안에서 비동기 작업을 할수 없을 것이다. 이때 JS에선 이벤트 루프를 적용해 이를 해결한다. JS 엔진은 메모리힙과 콜스택으로 이루어져있는데, 함수가 호출되는 내용은 콜스택에 쌓여 처리된다. 일반적인 함수 호출과 다르게, setTimeout, Promise와 같이 비동기 작업이 필요한 내용은 JS 엔진 내부가 아닌 외부 Web API를 통해 비동기 작업을 요청합니다. 비동기 작업이 끝나게 되면, 비동기 작업떄 같이 전달된 콜백함수를 콜백큐에 넣게 됩니다. 이때 이벤트루프는 콜백큐에 전달받은 함수를 처리하게 되는데, 가장 먼저 JS 엔진 내부의 콜스택을 수시로 확인하면서 만약 콜스택이 비게 된다면, 콜백큐에 있는 함수들을 콜스택에 넣게 됩니다.

정리하자면, 이벤트 루프는 비동기 처리가 완료된 콜백함수들을 조건에 맞게 콜스택에 넣어주는 역활을 해준다.

## React
### 질문
컴포넌트 라이프사이클이란 무엇이며, 어떻게 하면 함수 컴포넌트에서 라이프사이클을 유사하게 따라할 수 있는지 말해주세요.

## 답
![](https://cdn.filestackcontent.com/ApNH7030SAG1wAycdj3H)
컴포넌트 라이프사이클이란 클래스 컴포넌트에서 컴포넌트가 마운트될때부터 언마운트 될 때 까지 컴포넌트의 이벤트를 정의할 수 있는 함수이다.

대표적인 메소드로는 componentDidMount, shouldComponentUpdate, componentDidUpdate, componentWillUnmount가 있다.
- componentDidMount: 컴포넌트가 처음으로 마운트 된 이후 호출되는 메소드
- shouldComponentUpdate: 컴포넌트가 리랜더링될 상황(props, states등이 바뀔때)이 나온 이후에, 렌더링 할지 안할지 결정하는 메소드. 리턴값으로 bool을 받아서 true일때 리랜더링 된다.
- componentDidUpdate: 컴포넌트가 리랜더링된 이후에 호출되는 메소드
- componentWillUnmount: 컴포넌트가 언마운드 되기 직전에 호출되는 메소드

함수 컴포넌트에서는 컴포넌트 라이프사이클이 없다. 이를 대체하기 위해 useEffect 훅을 사용한다.

```javascript
useEffect(function callback() {
  // some works
  return function cleanup() {
	  // before next useEffect or Unmount
  }
}, [/* optional */])
```

- useEffect는 첫번째 매개변수로 콜백함수를 무조건 받고, 선택으로 두번째 매개변수에 배열을 받게 된다.
- useEffect의 콜백함수가 호출되는 조건은 두번째 매개변수에 따라 달라진다.
  - 두번째 매개변수가 없는 경우에, 컴포넌트가 랜더링 할 때 마다 (최초 랜더링 & 리랜더링) 호출된다.
  - 두번쨰 매개변수가 있는 경우에는, 컴포넌트가 최초로 렌더링되거나, 배열 안에 있는 state나 props가 변경될 때 호출된다. 이 배열을 의존성 배열이라고 한다.
- useEffect가 리턴값으로 함수를 가지게 된다면, 다음으로 useEffect가 실행되기 전이나 컴포넌트가 최종적으로 언마운트 되기 전에 리턴한 함수를 호출한다.

이를 통해 리엑트의 클래스 라이프사이클을 다음과 같이 대체할 수 있다.

- componentDidMount: useEffect(componentDidMount, [])
- componentDidUpdate: useEffect(componentDidUpdate) 또는 useEffect(componentDidUpdate, [(all states, props)])
- componentWillUnmount: useEffect(() => (componentWillUnmount), [])

## Operating System
### 질문
프로세스와 스레드의 차이는 무엇인가요?

### 답
프로세스 안에 스레드가 있다. 프로세스는 프로그램을 실행하는 단위이고, 그 안에 여러 스레드가 있다. 프로그램 단위는 코드, 데이터, 스택, 힙이 있는데 프로세스는 이를 각각 가지게 된다. 반대로 스레드는 한 프로세스 안에 있는 여러 스레드끼리 코드, 데이터, 힙은 공유하게 되고, 스레드별 개별적인 스택을 가지게 된다.

## PS
### 질문
퀵소트의 최선/최악의 시간 복잡도를 설명하고 개선 방법을 설명하시오

### 답
퀵소트의 최선 시간 복잡도는 O(nlgn)이고 최악의 시간 복잡도는 O(n^2)이다. 최악의 경우에는 원래 정렬하려는 차순의 역순일 경우에 나오는 시간복잡도이기때문에 이를 미리 확인하는 로직을 만들어 역순일 경우 이를 뒤집어주는 로직을 추가하면 이를 해결할 수 있다.

## Network
### 질문
TCP와 UDP를 어떻게 다른지 차이점을 중심으로 각각 설명해주세요. (단답형)

### 답
![](https://mblogthumb-phinf.pstatic.net/MjAyMDAzMjdfMTQx/MDAxNTg1MzIwMjE2MzQw.O-YCmFb9LYtnUHM7XPaiJT0aSjj-NUkgziW5-lHKT6Eg.UGiKtljYYepbBDVfikJRl70qsknkCiZebfS4t2NCGp4g.PNG.ijoos/image.png?type=w800)


