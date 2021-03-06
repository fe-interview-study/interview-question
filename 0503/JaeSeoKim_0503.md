# [JS] prototype에 대해서 아시는대로 설명해주세요

javascript는 객체를 상속하는 것이 아닌 prototype를 통해 참조를 하여 객체를 생성합니다.

이러한 특성을 통해서 상속된 정보는 각 객체가 아닌 prototype 속성에 정의가 되어 있습니다.

# [OS] 기아 상태(Starvation)와 원인에 대해서 설명해주세요.

특정 프로세스의 우선 순위가 낮아서 원하는 자원을 할당 받지 못하는 상태를 기아상태라고 합니다.

원인으로는 스케줄링이나 상호 배제 알고리즘의 오류에 기인하지만 자원 누수에 의해 일어날 수 있습니다.

# [PS] BFS vs DFS

공통적으로 조건내의 모든 node를 검색하는 부분은 동일하나, DFS는 하나의 경우에서 들어갈 수 있는 최대 깊이 까지 들어가서 탐색을 하고, DFS는 모든 노드를 공통으로 같은 깊이 까지 들어간 후 더 들어갈 수 있는 경우에만 추가로 들어갑니다.

즉 BFS는 재귀적으로 호출을 해야 하는 문제에서 유용하게 사용을 하고 DFS는 최단 경로에 대해서 탐색을 할 때 사용하게 됩니다.

# [React] React를 왜 써야하나요? (답변 후) 정말 그렇게 생각하나요? 다른 대체물은 없나요?

React는 Facebook에서 개발 및 지원을 하고 있는 SPA 라이브러리 입니다.

React를 사용하는 이유는 SPA를 쉽게 구현을 할 수 있는 라이브러리 이기때문입니다.

SPA를 사용하게 되면 사용자는 긴 페이지 로딩시간을 경험하는 것이 아니라 일반 적인 네이티브 프로그램을 사용하는 것과 같은 경험을 가질 수 있기 때문에 사용을 합니다.

또한 2021년 기준 SPA 관련 라이브러리, 프레임 워크 중 커뮤니티 크기가 가장 크기 때문에 사용합니다.

대체물로는 Vue, Angular, Svelte, Vanila JS로 직접 구현 등이 있지만 커뮤니티의 지원 등의 힘을 빌려서 빠른 개발 결과물을 도출 해내기에는 React가 현 시점으로는 가장 적합하다고 생각합니다.
