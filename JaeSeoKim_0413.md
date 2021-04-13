# [React] useEffect와 useLayoutEffect의 차이점

useEffect 는  react의 class 생명 주기와 비교를 하였을 때 `componentDidMount`, `componentDidUpdate`, `componentWillUnmount` 가 합쳐진 것으로 생각 할 수 있다.

useEffect 는 화면에 대한 렌더링이 끝난 후  `비 동기적` 으로 실행이 된다.

---

useLayoutEffect는 react의 class 생명 주기와 비교를 하였을 때 `componentDidMount`, `componentDidUpdate` 동일한 단계에서 실행을 하게 된다.

useLayoutEffect는 도든 DOM 변경 후에 `동기적`으로 발생하게 된다.

이때 브라우저가 화면을 그리기 이전 시점에 동기적으로 수행이 되게 된다.

위의 특성 때문에 `SSR` 를 하는 경우에는 자바스크립트 코드를 모두 다운로드 되기 이전까지는 실행이 안되기 때문에 사용에 대하여 주의를 기울어야 한다.



## 결론

useEffect는 화면에 대해 그린 후에 `비 동기적` 으로 동작을 하고 useLayoutEffect는 화면에 대해 그리기 전에 `동기적` 으로 동작 한다.

**useEffect** : Dom과 상호 작용할 필요가 없거나 Dom에 대한 변경 사항을 관찰할 필요가 없는 경우

**useLayout** : Dom에 대하여 변경을 하거나 측정이 필요 할 때



# [Network] CORS란 무엇이고 왜 사용하는 것 일까?

cors란 `Cross-Origin Resource Sharing` 의 줄임말으로 다른 출처의 리소스를 사용하는 경우에는 서버에서 허용하는 출처에서만 자원을 접근할 수 있는 권한을 부여하는 체제 이다.



사용을 하게 되는 가장 큰 이유는 보안을 위해서 이다.

예를 들어서 csrf 공격을 예를 들어본다.

victim이 특정 비트코인 사이트에 로그인 상황이라고 하였을 때 hacker가 만든 특정 사이트에 접근하여 특정한 버튼을 클릭시   client에서 비트코인 사이트에게 hacker의 계좌로 송금하라는 API에게 요청을 하게 된다.

이때 CORS 정책이 * 설정되어 있다면 victim은 공격에 당하는 지도 모르게 돈이 빠져 나가게 되지만 CORS 정책이 올바르게 되어 있다면 출처가 다른 곳에서 요청을 보내기 때문에 브라우저에서 먼저 OPTION 메소드를 이용하여 허용 출처에 대해서 확인을 하고 만약 허용하는 출처 대상이 아니라면 요청을 차단 하기 때문에 피해를 사전에 방지가 가능하다.



CSRF 공격이외에도 XSS 등 여러가지 공격에 노출되게 된다.



CORS는 프론트엔드 개발자가 개발을 하면서 쉽게 만나는 문제점 이지만 CORS에 대해서 자세하게 알고 백엔드 개발자에게 올바른 CORS를 설정하도록 요청을 하여야 한다.



# [JS] Event Bubbling, Capturing에 대해서

브라우저에서 Event에 대해 감지 하는 대표적인 특징 이다.

## Event Bubbling

<img width="457" alt="event-bubble" src="https://user-images.githubusercontent.com/48559454/114552883-01925600-9ca0-11eb-99e0-a82b47cc7ced.png">


위와 같은 형태로 특정 이벤트가 하위부터 상위 body까지 모두 이벤트가 결려 있다고 할 떄 하위 하나에 대해서 이벤트를 발생 시키게 되면 하위 이벤트 발생후 상위 이벤트에게 전달되는 현상을 말한다.

## Event Capturing

<img width="459" alt="event-capture" src="https://user-images.githubusercontent.com/48559454/114552889-035c1980-9ca0-11eb-9d8e-42fc821add4d.png">

Event Capturing은 Bubbling과 달리 반대로 동작을 하는 이벤트 전파 방식이다.

일반적으로는 capture 이벤트는 발생하지 않는데 아래와 같이 `addEventListner()` 에 옵션을 주어 capture에 대해 이벤트를 확인 할 수 있다.

```js
var divs = document.querySelectorAll('div');
divs.forEach(function(div) {
	div.addEventListener('click', logEvent, {
		capture: true // default 값은 false입니다.
	});
});

function logEvent(event) {
	console.log(event.currentTarget.className);
}
```



만약 이러한 이벤트 capture, bubbling 현상을 방지 하고 싶다면 `event.stopPropagation()` 를 이용하여 이벤트 전파를 막을 수 있다.



# [PS] pivotal(대각선이 고정인 행렬) 3x3, 4x4를 뒤집는 로직을 짜보자



일반 적인 반복문을 이용한다고 하면 아래와 같이 2중 반복문을 이용하여 뒤집는 로직을 만들 수 있다.

```c
int main(void)
{
	int map[4][4] = {
		{1, 2, 3, 4},
		{1, 2, 3, 4},
		{1, 2, 3, 4},
		{1, 2, 3, 4}};
	int	result[4][4];

	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			result[j][i] = map[i][j];
		}
	}

	return (0);
}
```


