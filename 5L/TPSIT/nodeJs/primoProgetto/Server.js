// Importazione dell'http
let http = require("http")
let querystring = require('url')
let fs = require("fs")

// Creazione del server
http.createServer((req, resp) =>{
    resp.setHeader('Content-Type', 'text/html')
    resp.write("<div style='justify-content:center; display:flex; color: black;'><strong>Brigata Paracadutisti \"Folgore\" - Esercito Italiano</strong></div>")
    let contenutoFile = fs.readFileSync("./index.html")
    let mioParametro = querystring.parse(req, true);
    switch (mioParametro.query.cognome) {
        case "GIORDANO":
            resp.end("Andrea")
            break;
        case "AUDISIO":
            resp.end("Nicolò")
        default:
            break;
    }
    resp.end(mioParametro.query.cognome)
    resp.end(contenutoFile)
    resp.end(req.url)
}).listen(3000)