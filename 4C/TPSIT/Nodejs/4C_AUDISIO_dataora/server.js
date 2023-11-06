const mioServer = require('http');
mioServer.createServer((req, res) => {
    res.write(`Data e ora corrente: ${Date()}`);
    res.end()
  }).listen(3000)
