# [JS] JS에서 Garbage Collection이란 무엇이며 어떻게 작동하는가?

Garbage Collection는 메모리 관리 기법중 하나로 동적으로 할당한 메모리에 대해서 필요가 없는 영역을 탐지하여 해제해주는 기능이다. 

js는 기본적으로 도달 가능성(reachability) 이라는 개념을 사용해 메모리 관리를 하게 된다.

접근 가능한(reachable) 값 이란 특정 값에 대해서 어디에서든 쉽게 접근이 가능한 값을 의미한다.

이러한 접근이 가능한 값이 아닌 경우 필요가 없는 영역으로 판단하고 해제 하게 된다.

# [React] 고차컴포넌트(HOC, Higher Order Component)란 무엇이고 언제 사용하는지 설명해주세요.

고차컴포넌트(HOC, higher Order Component)란 React에서 반복적으로 재사용되는 코드에 대한 해결책 이다.

간단하게 설명을 하게 되면 고차 컴포넌트는 컴포넌트를 가져와 새 컴포넌트를 반환하는 함수이다.

특정 컴포넌트를 가져와 새로운 컴포넌트를 반환하기 때문에 중복되는 코드에 대해서 재사용이 가능하게 된다.

# [OS] page fault 란?

요청한 메모리가 현재 물리적 메모리에 존재하지 않는 경우가 존재하는데 이를 page fault라고 한다.

이러한 page fault가 발생을 하면 os는 가상메모리에서 해당 메모리를 찾아 물리적 메모리에 로드를 해준다.

# [PS] Dynamic Programming 의 핵심 개념을 키워드 2개로 말해주세요

Overlapping Subproblems, Memoization
