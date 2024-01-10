const express = require('express')
const fs = require("fs")

const jsdom = require("jsdom")
const {JSDOM} = jsdom

const app = express()
const port = 3000

app.get('/', (req, res) => {
    let nomeUtente = req.query.nomeUtente
    let password = req.query.password
    let contenutoFile = fs.readFileSync("./index.html")
    let {document} = new JSDOM(contenutoFile).window
    let div = document.querySelector("#tabella")

    if (nomeUtente == "nicolo" && password == "prova"){
        div.style.backgroundColor = "green"
    } 
    else {
        div.style.backgroundColor = "red"
    }
    res.end(document.documentElement.outerHTML)
})

app.listen(port, () => console.log(`In ascolta sulla porta ${port}!`))