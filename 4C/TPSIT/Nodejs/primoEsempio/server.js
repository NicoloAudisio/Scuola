let mioServer = require("http")
mioServer.createServer((req, res)=>{
    res.write("<form action='https://google.it' method='get'><input type='text' name='q'><input type='submit' value='INVIA'></form>")
    res.end()
}).listen(3000)