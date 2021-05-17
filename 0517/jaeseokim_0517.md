# OAuth란 무엇이며 어떤 과정으로 작동되나요?

OAuth란 Open Standard Protocol 입니다. API 접근 위임 방식을 통하여 각기 다른 어플리케이션에서 Oauth를 이용한 다른 어플리케이션의 기능을 사용 가능하게 합니다.

과정에 대해서 간단하게 예시로 설명을 하면 Facebook으로 로그인 하기를 구현 할려고 할 때 서버 개발자는 해당 Facebook에게 API Public Key 와 Secret Key를 할당을 받고 login과 같은 인증 작업을 진행 할때 Redirect 되어야 하는 사이트 주소등을 미리 알려줍니다.

해당 하는 기능들로 구현이 완료 되었다고 하였을 때 사용자가 로그인을 시도하게 되면 facebook에서 제공하는 login 페이지로 가게 되고 이때 API Public key와 redirect url 등의 정보를 가지고 시도하게 됩니다.

Facebook에서 인증을 진행하면서 발급 받은 key와 redirect url등의 정보가 일치하면 인증 성공후 redirect url로 redirect 시키게 되는데 이때 서버단에서 검증 가능한 코드 하나를 포함하여서 전송합니다.

리다이렉트를 통해 응답을 받게 되면 서버단에서 받은 code와 secret key를 이용하여 facebook API로 인증 요청을 보내게 되고 이때 성공을 하게 되면 사용자의 정보 등이 들어와 인증을 성공하게 됩니다.

그리고 해당하는 정보를 통해 서버에서는 로그인이 되었다고 처리를 하게되고 해당 사이트에서는 유저에게 로그인 되었다고 알립니다.

# [PS] sequence container와 associative container 차이를 설명해주세요.

sequence container와 associative container는 같은 타입의 여러 객체를 저장하는 일종의 집합 입니다.

각각의 차이는 저장하는 방식과 관리하는 방식에 따른 차이가 발생합니다.

sequence container는 직선순서대로 나열되어 있으며 명확한 순서를 가집니다. 하지만 associative container는 저장되는 순서에 대해서 지정할 수 없습니다. 또한 associative container는 key와 value를 사용하여 저장을 합니다.

# [JS] new Function에 대해서 설명해 주세요

eval과 같이 문자열로 들어온 값에 대해서 javascript parser를 동작시켜 javascript로 만들어줍니다.

차이점으로는 eval은 바로 실행을 하게 되지만 new Function은 인자와 바디 형태로 문자열을 받게 되어서 새로운 함수를 만들게 되고 해당 함수는 외부 변수에 대해서 접근을 못한다는 점이 있습니다.
