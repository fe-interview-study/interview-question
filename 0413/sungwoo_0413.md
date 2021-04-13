## React

### 질문
useEffect 와 useLayoutEffect의 차이점

### 답변
useEffect과 useLayoutEffect는 작업이 동기적인지 비동기적인지에 따라 나눠집니다.

흔히 사용되는 useEffect의 경우 화면이 랜더링이 된 이후 비동기적으로 작업이 진행되지만, useLayoutEffect의 경우 화면 랜더링 이후에 동기적으로 작업이 진행됩니다. 이 차이점은 사용자의 스크롤 바 위치나 노출된 DOM 결과물을 가지고 작업을 진행할 때 useLayoutEffect같이 동기적으로 처리해야하고, 사용자에게 최종 결과물을 던저줄 때 모든 작업을 처리해야 하는 경우 useEffect가 아닌 useLayoutEffect를 사용해야 한다.

(자세한 useEffect는 [이전 질문](https://github.com/fe-interview-study/interview-question/blob/main/0329/sungwoo_0329.md#react)에서 다뤄봄)

## Network

### 질문
CORS란 무엇이며 왜 이 스펙을 사용하는 것일까?

### 답변
CORS란 Cross Origin Resource Sharing의 약자입니다.

브라우저의 SOP 정책으로 현재 사이트와 다른 Origin에서 데이터를 요청하는 경우 블락 처리가 되는데, CORS 설정을 response 헤더에 설정해놓으면 브라우저에서 SOP 정책을 해제하면서 데이터를 받을 수 있다.

## JS

### 질문
Event Bubbling, Capturing에 대해서 설명해 주세요

### 답변
HTML DOM에서 Event를 다룰 때 그 이벤트를 처리하는 과정의 흐름으로 Event Bubbling과 Event Capturing가 있습니다.

Event Bubbling은 하위 엘레멘츠의 이벤트부터 상위 엘러멘츠까지 순차적으로 실행되는 흐름이고, Event Capturing은 상위 엘러멘츠의 이벤트부터 하위 엘레멘츠까지 순차적으로 실행되는 흐름입니다. 기본적으로 이벤트를 설정하면 Event Bubbling의 흐름으로 처리되지만 addEventListener에 capture를 true로 설정하면 Event Capture 방식으로 처리된다.

## PS

### 질문
pivotal(대각선이 고정인 행렬) 3x3, 4x4를 뒤집는 로직을 짜보자

### 답변
n = 3 or 4?
arr[n][n] <- def
for i (0 ~ n-1)
	for j (0 ~ n-1)
		if i != j
			swap arr[i][j], arr[j][i]
????
