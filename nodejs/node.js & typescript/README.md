# typescript in node
> node에서는 직접 typescript를 실행할 수 없다.
> javascript로 컴파일한 후 실생된다.

```typescript
// app.ts
let age: number;
age = 30;
console.log(age);
```

```javascript
//app.js
var age;
age = 30;
console.log(age);
```

- app.ts를 tsc app.ts로 실행을 하면 app.js라는 형태의 파일이 javascript로 compile 되어 생성이 된다.

- tsc command는 compile을 해준다. 실행은 compile 된 파일을 node command를 이용해서 실행한다.



```typescript
const express = require('express'); 
const app = express();
app.listen(3000);
```

- ts에서 js에서 쓰던 함수를 사용할 수 없어 require에 에러가 발생.
  - npm install --save-dev @types/node  를 설치하면 해결.
- tsc watch모드
  - tsc -w



