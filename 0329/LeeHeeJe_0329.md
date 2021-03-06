## [Network] TCP와 UDP의 차이점은? 



 ➡️ TCP는 연결형 서비스를 지원하는 전송 계층 프로토콜입니다. 인터넷 환경에서 기본으로 사용합니다. 

반면 UDP는 비연결형 서비스를 지원하는 전송계층 프로토콜로써, 인터넷상에서 TCP와 달리 서로 정보를 주고받을 때 정보를 보낸다는 신호나 받는다는 신호 절차를 

거치지 않고, 보내는 쪽에서 일방적으로 데이터를 전달하는 통신 프로토콜입니다.

또한 UDP는 TCP 보다 속도가 빠르지만 신뢰성있는 데이터 전송을 보장하지 않습니다. 





## [Javascript] Event Loop란 무엇인가요?



➡️ **Event Loop**는 Call Stack과 Callback Queue의 상태를 체크하여, Call Stack이 빈 상태가 되면, Callback Queue의 첫번째 콜백을 Call Stack으로 밀어넣어 줍니다. 이러한 반복적인 행동을 ***틱(tick)*** 이라 부릅니다.

이를 통해 싱글 스레드인 자바스크립트가 비동기 작업을 할 수 있도록합니다. 





## [OS] 프로세스와 스레드의 차이는 무엇인가요?



➡️ 프로세스는 메모리를 할당 받아 현재 실행 중인 프로그램을 의미합니다. 반면 스레드는 프로세스 내에서 실행되는 흐름의 단위로 프로세스가 할당 받은 자원을 이용합니다. 





## [PS] 퀵소트의 최선/최악의 시간 복잡도를 설명하고 개선 방법을 설명하시오 



 ➡️ 퀵소트의 최선의 시간 복잡도는 `O(nlogn)` 이고 최악의 시간 복잡도는 pivot이 최솟값이나 최댓값으로 선택된 경우인 `O(n^2)` 입니다. 또는 이미 배열이 정렬된 경우입니다. 



이를 개선하기 위해서 배열을 랜덤으로 배치하거나 피벗을 랜덤하게 선택한다면 최악의 상황을 줄일 수 있을 것입니다. 또는 특정 값을 몇 개를 뽑아 그 수들 중 중간 값을 pivot으로 선정하는 방법도 있습니다. 





## [React] 컴포넌트 라이프사이클이란 무엇이며, 어떻게 하면 함수 컴포넌트에서 라이프사이클을 유사하게 따라할 수 있는지 말해주세요.



➡️ 컴포넌트 라이프사이클은 컴포넌트의 생성부터 소멸에 이르는 과정 및 이벤트를 뜻합니다. 3가지 카테고리로 나눠서 mounting, updating, unmounting으로 볼 수 있습니다. 



useEffect() 라는 훅을 써서 라이프 사이클을 따라할 수 있습니다. 함수 컴포넌트에서는 특정 데이터에 대해서 라이프 사이클이 진행됩니다. 

