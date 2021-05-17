## JS

### 질문
New function이란?

### 답변

함수 표현식과 함수 선언문 이외에 함수를 만들 수도 있는 방법이 하나 더 있습니다. `new Function`이라는 문법을 사용하면 어떤 문자열도 함수로 바꿀 수 있다.

서버에서 코드를 받거나 템플릿을 사용해 함수를 동적으로 컴파일해야 하는 경우나 복잡한 웹 애플리케이션을 구현할 때 사용한다.

## PS

### 질문
sequence container와 associative container의 차이를 설명해주세요.

### 답변

### 시퀀스 컨테이너(sequence container)
배열 처럼 객체들을 순차적으로 보관하는 컨테이너이다.

- vector
- list
- deque

### 연관 컨테이너 (associative container)
키를 바탕으로 대응되는 값을 찾아주는 컨테이너이다.

- set
- map
- multiset
- multimap
- unordered_set
- unordered_map

## Network

### 질문
OAuth란 무엇이며 어떤 과정으로 작동되나요?

### 답변

OAuth는 인증을 위한 오픈 스탠더드 프로토콜로, 사용자가 Facebook이나 트위터 같은 인터넷 서비스의 기능을 다른 애플리케이션(데스크톱, 웹, 모바일 등)에서도 사용할 수 있게 한 것입니다.

OAuth에서 'Auth'는 'Authentication'(인증)뿐만 아니라 'Authorization'(허가) 또한 포함하고 있다.

과정은 
1. Request Token의 요청과 발급
2. 사용자 인증 페이지 호출
3. 사용자 로그인 완료
4. 사용자의 권한 요청 수락
5. Access Token 발급
6. Access Token 을 이용해 서비스 정보 요청
