# node.js

> 출처: 해당내용은 ''[생활코딩](https://opentutorials.org/course/1)''님의 강의를 듣고 따라해보고 정리한 글입니다.
>
> nodejs는 여러일들을 처리할 수 있는 역량을 가지고 있지만 특히, server쪽에 위치하면서 빠르고 편리하게 serverfh 들어오는 요청을 응답하는 application을 만드는 기반에 초점을 두고있다.


## 설치 및 오리엔테이션

JS라는 언어로 웹 브라우저를 제어하거나 node.js를 제어할 수 있다. 

각자의 기능을 모르면 JS라는 언어로 웹브라우저에서는 웹브라우저 기능을, 노드js에선 노드js의 기능을 효과 적으로 다룰 수 없다

ex) alert가 웹 브라우저에서는 경고창을 띄우지만 nodejs에선 그렇지 않다.

#### command

- 명령프롬프트
  - dir /w : 현재 디렉토리 내에 있는 파일을 볼 수 있음.
  - node [파일명].js : node.js로 해당파일을 실행
  - ctrl + c : 실행중인 것을 종료



## 간단한 웹앱 만들기

- webserver.js

```javascript
// nodjs 공식홈페이지 코드

const http = require('http');
 
const hostname = '127.0.0.1';
const port = 1337;
 
http.createServer((req, res) => {
 res.writeHead(200, { 'Content-Type': 'text/plain' });
 res.end('Hello World\n');
}).listen(port, hostname, () => {
 console.log(`Server running at http://${hostname}:${port}/`);
});
```



#### 인터넷의 동작방법

- 인터넷을 통해 client가 요청하면 server가 응답함(상대적인 관계)
- domain name은 사람이 접속하기 쉽게 나타나는 이름이며 실제로는 domain name에 해당하는 IP address를 통해 접속한다.
- server computer에는 다양한 server application들이 존재하는데(웹, 게임, 데이터베이스 등) 어떻게 필요한 server에 연결할까???
  - 해당 server의 port를 통해 연결된다. 이것을 listening 한다고 한다.
  - ex)http://a.com이라는 주소에  80번 port가 웹 서버라고 하자. 웹 서버에 연결을 하기 위해서는 'http://a.com:80'와 같이 해당 도메인에 80번 포트로 연결을 하고 그러면 웹서버에서 응답을 할 것이다.
  - port는 생략을 할 수 있다. 이유는 http라는 것을 통해 웹 브라우저로 접속했다는 것을 알 수 있어 바로 웹 서버에 해당하는 80번 포트로 연결이 되는 것이다.



## module

> [공식문서]([Documentation | Node.js (nodejs.org)](https://nodejs.org/en/docs/))를 통해 module들의 기능들을 확인할 수 있다.

#### NPM(Node Package Manager)

- node 모듈을 사용자가 설치, 삭제, 업그레이드 의존성 관리를 쉽게 하기위해 해준다.
- npm install [패키지이름] (-g)
  - -g : 전역적으로 실행할 수 있는 독립적인 것으로 설치/ 프로젝의 부품으로 사용하겠다면 -g 사용하지않는다.
- package
  - 다른 sw에서 부품으로 사용되는 모듈 or독립적으로 동작하는 sw 두 종류가 존재

- uglifyjs(모듈)
  - 가독성 높이기 위한 줄바꿈 띄어쓰기 등을 제거
  - 실제 가독성을 높이기 위한 행위들이 전부 데이터이다. 네트워크에서 js파일을 전송할 때 코드 내용이 많아지면 느려지고 비싸지기 마련이다. 그래서 uglify와 같은 프로그램을 실행시키면 실제로 기계가 코드를 처리하기 위한 필수 코드를 제외하고 전부 제거를 하는 역할을 한다.
  - -m : 공백만 없애는 것이 아닌 지역변수처럼 이름을 바꿔도 상관없는 변수이름들을 한글자의 가장 짧은 문자로 바꿔준다.
  - uglifyjs [파일명.js] -o [파일명.min.js] -m : 파일명1의 파일을 파일명2로 간소화시켜 저장(min은 간소화 했다는 것을 파일명에 표기한 것, 규칙과도 같다.)
- 현재 디렉토리를 패키지화 하기(나)
  - npm init
  - entry point - 어떤 js가 패키지를 구동시키는 js를 지정
  - test command - 패키지에서 어떤 명령어를 실행시키면 테스트를 실행시키는 것
  - git repository - git에 올리기 위한 주소.
  - 완성되면 package.json이 생성된다.(생성시 입력한 정보가 기록됨)
- underscore.js - [공식문서](https://underscorejs.org/)
  - Node.js : npm install underscore (--save)
  - --save 는 옵션이다.
  - 일시적으로 사용할 때는 --save를 사용하지 않으며, 프로젝트에 반드시 필요할 땐 --save를 붙여 dependecies안에 포함시킨다.(의존성 명시적으로 표시)


### router
> 사용자의 요청을 어떤  controller에 전달해줄지 정하는 중개자의 역할을 수행

## 정적인 파일을 서비스 하는법
```javacsript
// 정적 파일(public: 정적인 파일이 위치한 dir)
app.use(express.static('public'));
```




