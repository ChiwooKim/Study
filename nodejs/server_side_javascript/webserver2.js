const http = require('http');
 
const hostname = '127.0.0.1';
const port = 1337;

// server 생성
// req:요청, res: 응답
const server = http.createServer(function(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World!\n');
});
// 어떤 포트로 host경로로 타고 바라보게하는가? listen에 실행시간이 걸릴수도 있어서 callback으로 비동기적으로 처리
server.listen(port, hostname), function() {
 console.log(`Server running at http://${hostname}:${port}/`);
};