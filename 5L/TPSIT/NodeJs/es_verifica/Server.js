let http = require("http")
let url = require("url")
let calcolatrice = require("./Calcolatrice.js")

http.createServer((req, res) => {
    let mioURL = url.parse(req.url, true)
    switch (mioURL.path) {
        case "/":
            res.end("calcolatrice automatica\nNumeri automatici 2, 5\n\nAddizione: /addizione\nSottrazione: /sottrazione\nMoltiplicazione: /moltiplicazione\nDivisione: /divisione\nResto: /resto")
            break;
        
        case "/addizione":
            res.end(calcolatrice.somma(2,5).toString())
            break;

        case "/sottrazione":
            res.end(calcolatrice.sottrazione(2,5).toString())
            break;
        
        case "/moltiplicazione":
            res.end(calcolatrice.moltiplicazione(2,5).toString())
            break;

        case "/divisione":
            res.end(calcolatrice.divisione(2,5).toString())
            break;

        case "/resto":
            res.end(calcolatrice.resto(2,5).toString())
            break;

        default:
            res.end("Errore")
            break;
    }
}).listen("3000")