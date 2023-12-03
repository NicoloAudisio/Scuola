// importazione moduli
let http = require('http');
let url = require('url');
let fsHandler = require('./fsHandler');
let tempData = require('./TempData');

http.createServer((req, res) => {
    let parsedUrl = url.parse(req.url, true);
    res.setHeader("Content-Type", "text/html");
    
    // parse url
    if (parsedUrl.pathname === '/temperatures') {
        //tabella
        let table = tempData.getTable();
        res.end(table);
    } else {
        //ritorno index
        let content = fsHandler.readHTMLFile("./index.html");

        if (parsedUrl.query.city && parsedUrl.query.max && parsedUrl.query.min) {
            tempData.addData(parsedUrl.query);
        }

        res.end(content);
    }
}).listen(3000);
