## JS

### 질문
JS에서 Garbage Collection이란 무엇이며 어떻게 작동하는가?

### 답변
JS에서 Garbage Collection은 실행 과정 중에서 불필요한 메모리가 사용되는것을 방지하기 위해 엔진에서 메모리를 정리하는 것을 말합니다.

Garbage Collection은 현제 엔진이 있는 스코프 기준으로 그 스코프에 사용하지 않는 변수나 객체가 존재하는 경우 그 메모리를 해제하는 방식으로 메모리를 최적화합니다.

[참고](https://ko.javascript.info/garbage-collection)


## React

### 질문
HoC란 무엇이고 언제 사용하는가?

### 답변
HoC는 컴포넌트를 만들어주는 함수인데, 매개변수로 컴포넌트를 받습니다. HoC의 핵심은 기존 컴포넌트를 조합, 재사용해 새로운 컴포넌트를 만든다는 점에 있습니다. HoC를 사용하게 된다면 여러 컴포넌트에서 반복되는 코드를 재사용해 하나의 함수로 정리해 사용하게 되고, 이를 더 가독성 있게 표현할수 있게 됩니다.

## OS

### 질문
Page Fault란?

### 답변
OS에서 사용하는 물리적 메모리가 부족한 상황을 페이지 폴트라고 한다. 이를 위해 OS에서는 가상 메모리를 준비해 물리적 메모리를 대체하는 작업을 진행하는데, 이를 요구 페이징이라고 한다.

## PS

### 질문
DP의 핵심 개념을 키워드 2개로 말해주세요

### 답변
DP의 두 키워드는 memoization과 decoupling입니다. DP로 문제를 풀게 되면 하나의 큰 문제를 서로 영향받지 않는 여러 작은 문제로 쪼개야 하며(decoupling), 이 문제의 결과를 저장해 재사용할수 있어야 합니다(memoization).

[참고](https://hyunw.kim/blog/2018/09/18/Algorithm_Analysis03_DynamicProgramming1.html)
