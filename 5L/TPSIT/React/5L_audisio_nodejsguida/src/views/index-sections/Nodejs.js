import React from "react";

// reactstrap components
import { 
  Button,
  Container,
  Row,
  Col,
  Badge,
  Carousel,
  CarouselItem,
  CarouselIndicators,
} from "reactstrap";

// core components

function Nodejs() {
  const copiahttp = () => {
    navigator.clipboard.writeText('let http = require("http")');
  };

  const copiainit = () => {
    navigator.clipboard.writeText('npm init');
  };

  const copiaurl = () => {
    navigator.clipboard.writeText('let url = require("url")');
  };

  const copiainstallejs = () => {
    navigator.clipboard.writeText('npm install ejs');
  };

  const copiainstallexpress = () => {
    navigator.clipboard.writeText('npm install express');
  };

  const copiafs = () => {
    navigator.clipboard.writeText('let fs = require("fs")');
  };

  const copiacreatehttp = () => {
    navigator.clipboard.writeText(`
      http.createServer((req, resp) => {
        // Qua si scrivere il codice che il nostro servizio deve eseguire
      }).listen(3000);
    `);
  };

  const copiastampa = () => {
    navigator.clipboard.writeText(`
      http.createServer((req, resp) =>{
        resp.write("Benvenuto!")
        resp.end()
      }).listen(3000)
    `);
  };

  const copiamodulo = () => {
    navigator.clipboard.writeText(`
      exports.somma =(a,b)=> {
        return (a+b)
      }
      
      exports.sottrazione =(a,b)=> {
          return (a-b)
      }
      
      exports.moltiplicazione =(a,b)=> {
          return (a*b)
      }
      
      exports.divisione =(a,b)=> {
          return (a/b)
      }
      
      exports.resto =(a,b)=> {
          return (a%b)
      }
    `);
  };

  const copiamoduloEs = () => {
    navigator.clipboard.writeText(`
      export const somma =(a,b)=> {
        return (a+b)
      }
      
      export const sottrazione =(a,b)=> {
          return (a-b)
      }
      
      export const moltiplicazione =(a,b)=> {
          return (a*b)
      }
      
      export const divisione =(a,b)=> {
          return (a/b)
      }
      
      export const resto =(a,b)=> {
          return (a%b)
      }
    `);
  };

  const copiastart = () => {
    navigator.clipboard.writeText(`
      nodemon Server.js
    `);
  };

  const copiaesempio1 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")  

      // Creazione del server
      http.createServer((req, resp) =>{
          resp.write("<div style='justify-content:center; display:flex; color: red;'><strong>Ciao<br>Benvenuto</strong></div>")
          resp.end()
      }).listen(3000)
    `);
  };

  const copiamodulo1 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let calcolatrice = require("./mioModulo")
      
      http.createServer((req, res) => {

      }).listen("3000")
    `);
  };

  const copiaasync = () => {
    navigator.clipboard.writeText(`
      const somma = async()=>{
        await fetch('https://v2.jokeapi.dev/joke/Programming?type=single')
        .then(res => res.json())
        .then(json => console.log(json.joke))
      }
    `);
  };

  const copiafs1 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
        resp.end()
      }).listen(3000)
    `);
  };

  const copiaurl1 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      let url = require("url")
      
      http.createServer((req, resp) =>{
        
      }).listen(3000)
    `);
  };

  const copiaimportexpress = () => {
    navigator.clipboard.writeText(`
      const express = require('express');
      const app = express();
    `);
  };

  const copiasetejs = () => {
    navigator.clipboard.writeText(`
      app.set('view engine', 'ejs');
    `);
  };

  const copiagetejs = () => {
    navigator.clipboard.writeText(`
      app.get('/', function(req, res) {
        res.render('index', { nome: 'Mario' });
      });
    `);
  };

  const copialistenejs = () => {
    navigator.clipboard.writeText(`
      app.listen(3000, function() {
        console.log('App in ascolto sulla porta 3000');
      });
    `);
  };

  const copiaejs = () => {
    navigator.clipboard.writeText(`
    <!DOCTYPE html>
    <html>
    <head>
        <title>Esempio EJS</title>
    </head>
    <body>
        <h1>Ciao, <%= nome %>!</h1>
        <p>Benvenuto nel nostro sito web.</p>
    </body>
    </html>
    `);
  };

  const copiaexpress = () => {
    navigator.clipboard.writeText(`
    const express = require('express');
    const app = express();
    
    app.set('view engine', 'ejs');
    
    app.get('/', function(req, res) {
        res.render('index', { nome: 'Mario' });
    });
    
    app.listen(3000, function() {
        console.log('App in ascolto sulla porta 3000');
    });
    
    `);
  };

  const copiafs2 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
        resp.setHeader('Content-Type', 'text/html')
        resp.end()
      }).listen(3000)
    `);
  };

  const copiamoduloEs2 = () => {
    navigator.clipboard.writeText(`
      import http from "http"
      import {somma, sottrazione} from "./mioModulo.js"
      
      http.createServer((req, res) => {
          res.end(somma(7,5).toString())
      }).listen("3000")
    `);
  };

  const copiamodulo2 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let calcolatrice = require("./mioModulo")
      http.createServer((req, res) => {
        res.end(calcolatrice.somma(5,7).toString())
      }).listen("3000")
    `);
  };

  const copiaurl2 = () => {
    navigator.clipboard.writeText(`
      const { readSync } = require("fs")
      let http = require("http")
      let url = require("url")
      
      http.createServer((req, res) => {
          let mioURL = url.parse(req.url, true)
      }).listen("3000")
    `);
  };

  const copiafs3 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
        resp.setHeader('Content-Type', 'text/html')
        let contenutoFile = fs.readFileSync("./index.html")
        resp.end()
      }).listen(3000)
    `);
  };

  const copiaurl3 = () => {
    navigator.clipboard.writeText(`
      const { readSync } = require("fs")
      let http = require("http")
      let url = require("url")
      
      http.createServer((req, res) => {
          let mioURL = url.parse(req.url, true)
          switch (mioURL.path) {
              case "/":
                  res.end("HOME PAGE")
                  break;
              
              case "/stella":
                  res.end("Cane")
                  break;
      
              case "/maia":
                  res.end("Gatto")
                  break;
      
              default:
                  res.end("Errore")
                  break;
          }
      }).listen("3000")
    `);
  };

  const copiafs4 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
        resp.setHeader('Content-Type', 'text/html')
        let contenutoFile = fs.readFileSync("./index.html")
        resp.end(contenutoFile)
      }).listen(3000)
    `);
  };

  const copiafs5 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
          resp.setHeader('Content-Type', 'text/html')
          let contenutoFile = fs.readFileSync("./index.html")
          resp.end(contenutoFile)
      }).listen(3000)
    `);
  };

  const copiapackage = () => {
    navigator.clipboard.writeText(`
      {
        "name": "audisio",
        "version": "1.0.0",
        "description": "",
        "type": "module",
        "main": "server.js",
        "scripts": {
          "test": "echo \"Error: no test specified\" && exit 1",
          "start": "node server.js"
        },
        "author": "",
        "license": "ISC"
      }
    `);
  };

  const copiafs6 = () => {
    navigator.clipboard.writeText(`
      <!DOCTYPE html>
      <html lang="it">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Prova</title>
      </head>
      <body>
          <div class="container">
              <div class="title">
                  <h1>Campo Minato e le sue leggende</h1>
              </div>
              <div class="subtitle">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil, voluptate unde quaerat velit quod deleniti debitis nobis laborum molestias nemo distinctio numquam doloremque? Officia, accusamus eveniet libero minima doloribus quis.
              </div>
              <div class="footer">
                  <a href="https://www.google.com">Link utili</a>
              </div>
          </div>
      </body>
      </html>
    `);
  };

  const items = [
    {
      src: require("assets/img/screenshot_parseHome.png"),
      altText: "localhost:3000/",
      caption: "localhost:3000/"
    },
    {
      src: require("assets/img/screenshot_parseCane.png"),
      altText: "localhost:3000/cane",
      caption: "localhost:3000/cane"
    },
    {
      src: require("assets/img/screenshot_parsegatto.png"),
      altText: "localhost:3000/gatto",
      caption: "localhost:3000/gatto"
    }
  ];
  
    const [activeIndex, setActiveIndex] = React.useState(0);
    const [animating, setAnimating] = React.useState(false);
    const onExiting = () => {
      setAnimating(true);
    };
    const onExited = () => {
      setAnimating(false);
    };
    const next = () => {
      if (animating) return;
      const nextIndex = activeIndex === items.length - 1 ? 0 : activeIndex + 1;
      setActiveIndex(nextIndex);
    };
    const previous = () => {
      if (animating) return;
      const nextIndex = activeIndex === 0 ? items.length - 1 : activeIndex - 1;
      setActiveIndex(nextIndex);
    };
    const goToIndex = (newIndex) => {
      if (animating) return;
      setActiveIndex(newIndex);
    };


  return (
    <>
      <div
        className="section section-download"
        data-background-color="black"
        id="download-section"
      >
        <Container>
          <Row className="justify-content-md-center">
            <Col className="text-center" lg="8" md="12">
              <h3 className="title">Progetto NodeJS</h3>
              <h5 className="description">
                Nella seguente guida si affrontano i seguenti argomenti:<br/>
              </h5>
              <Badge color="info" className="mr-3 mt-4">
                Primo progetto
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                FS
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
               Parse URL
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                CommonJS
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                EsModules
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                Async / Await
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                Ejs
              </Badge>
            </Col>
          </Row>
          {/* Creazione primo progetto NodeJS */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">Creazione del primo progetto</h4>
              <h5 className="description">
                Per creare un progetto NodeJS bisogna seguire i seguenti passaggi:<br/>
              </h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li>
                  <h5>Importare il modulo http<br/></h5>
                  <Button color="info" type="button" onClick={copiahttp} size="lg">
                    let http = require("http")
                  </Button>
                </li>
                <br/>
                <li>
                  <h5>Creare il server e metterlo in ascolto sulla porta che si preferisce, in questo caso viene messo in ascolto sulla porta 3000</h5>
                  <Button color="info" type="button" onClick={copiacreatehttp} size="lg">
                    http.createServer((req, resp) =&gt;&#123; <br/>
                      &#47;&#47;Insere qua il codice da eseguire<br/>
                    &#125;).listen(3000)
                  </Button>
                </li>
                <br/>
                Per scrivere comandi al server si utilizzano due parametri: il <i>Request (req)</i> e il <i>Respons (resp)</i>
                <ul>
                  <li>Request (req): il client invia i parametri al server</li>
                  <li>Respons (resp): il server invia le informazioni al server</li>
                </ul>
                <br/>
                <br/>
                <li><h5>Stampa a video di un messaggio</h5></li>
                <Button color="info" type="button" onClick={copiastampa} size="lg">
                  http.createServer((req, resp) =&gt;&#123;<br/>
                      resp.write("Benvenuto!")<br/>
                      resp.end()<br/>
                    &#125;).listen(3000)<br/>
                </Button>
                <br/>
                <br/>
                <li><h5>Avviare il file <i>Server.js</i> tramite il comando da terminale:</h5></li>
                <Button color="info" type="button" onClick={copiastart} size="lg">
                  nodemon Server.js
                </Button>
              </ul>
              <br/>
              <br/>
              <h5>Esempio completo:</h5>
              <Button color="info" type="button" onClick={copiaesempio1} size="lg">
                let http = require("http")<br/>

                http.createServer((req, resp) =&gt;&#123;<br/>
                    resp.write("&lt;div style='justify-content:center; display:flex; color: red;'&gt;&lt;strong&gt;Ciao&lt;br&gt;Benvenuto&lt;/strong&gt;&lt;/div&gt;")<br/>
                    resp.end()<br/>
                  &#125;).listen(4000)<br/>
              </Button>
              <br/>
              <br/>
              <Col sm="12">
                <img
                  alt="..."
                  className="rounded"
                  src={require("assets/img/screenshot_benvenuto.png")}
                ></img>
              </Col>
            </Col>
          </Row>
          {/* FS */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">FS</h4>
              <h5 className="description">
              Il modulo fs (File System) di Node.js è una funzionalità integrata che permette di interagire con il file system del tuo computer. Questo modulo fornisce tutte le funzioni necessarie per leggere, scrivere e cancellare file sulla macchina locale.<br/>
              Ecco alcuni punti chiave sul modulo fs di Node.js:<br/>
              
              <ul>
                <li>Lavorare con file e directory: Questa è una delle esigenze fondamentali di un’applicazione full-stack. Gli utenti dell’app potrebbero voler caricare immagini, curriculum o altri file su un server. Allo stesso tempo, l’applicazione potrebbe aver bisogno di leggere i file di configurazione, spostare i file o addirittura modificarne i permessi in modo programmatico.</li> 
                <li>API sincrone e asincrone: Il modulo fs fornisce diverse API per interagire con i file system senza problemi. La maggior parte delle API sono personalizzabili con opzioni e flag. È anche possibile utilizzarle per eseguire operazioni sia sincrone che asincrone sui file.</li>
                <li>Moduli di Node.js: I moduli di Node.js sono un insieme di funzionalità disponibili come API che possono essere utilizzate da un programma utente. Ad esempio, esiste il modulo fs per interagire con il file system.</li>
              </ul>
              </h5>
              <h5>Per utilizzare il modulo <i>FS </i>si devono seguire i seguenti passaggi:</h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>index.html</i>”</h5></li>
                <li>
                  <h5>Importare il modulo http<br/></h5>
                  <Button color="info" type="button" onClick={copiahttp} size="lg">
                    let http = require("http")
                  </Button>
                </li>
                <br/>
                <br/>
                <li>
                  <h5>Importare il modulo fs<br/></h5>
                  <Button color="info" type="button" onClick={copiafs} size="lg">
                    let fs = require("fs")
                  </Button>
                </li>
                <br/>
                <li>
                  <h5>Si ricrea la struttura base vista in precedenza, aggiungendo l'importazione del modulo <i>fs</i>:</h5>
                  <Button color="info" type="button" onClick={copiafs1} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    resp.end()<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                </li>
                <br/>
                <br/>
                <li><h5>Bisogna impostare il <i>setHeader</i> che permette di specificare l'estensione del file e come deve essere trattato dal nostro Server:</h5></li>
                <Button color="info" type="button" onClick={copiafs2} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    resp.setHeader('Content-Type', 'text/html')<br/>
                    resp.end()<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
                <li><h5>Si deve salvare all'interno di una variabile il file, tramite la funzione <i>readFileSync</i>:</h5></li>
                <Button color="info" type="button" onClick={copiafs3} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    resp.setHeader('Content-Type', 'text/html')<br/>
                    let contenutoFile = fs.readFileSync("./index.html")<br/>
                    resp.end()<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
                <li><h5>Infine si imposta nell'end la variabile contenente il file inserito in precedenza:</h5></li>
                <Button color="info" type="button" onClick={copiafs4} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    resp.setHeader('Content-Type', 'text/html')<br/>
                    let contenutoFile = fs.readFileSync("./index.html")<br/>
                    resp.end(contenutoFile)<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
                <br/>
                <h5>Esempio completo</h5>
                <h5 className="description">Server.js</h5>
                <Button color="info" type="button" onClick={copiafs5} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>
                  <br/>
                  http.createServer((req, resp) =&gt;&#123;<br/>
                      resp.setHeader('Content-Type', 'text/html')<br/>
                      let contenutoFile = fs.readFileSync("./index.html")<br/>
                      resp.end(contenutoFile)<br/>
                  &#125;).listen(3000)
                </Button>
                <br/>
                <br/>
                <h5 className="description">index.html</h5>
                <Button color="info" type="button" onClick={copiafs6} size="lg">
                &lt;!DOCTYPE html&gt;<br/>
                &lt;html lang="it"&gt;<br/>
                &lt;head&gt;<br/>
                  &lt;meta charset="UTF-8"&gt;<br/>
                  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;<br/>
                  &lt;title&gt;;Prova&lt;/title&gt;<br/>
                &lt;/head&gt;<br/>
                &lt;body&gt;<br/>
                  &lt;div class="container"&gt;<br/>
                    &lt;div class="title"&gt;<br/>
                      &lt;h1&gt;Campo Minato e le sue leggende&lt;/h1&gt;<br/>
                        &lt;/div&gt;<br/>
                        &lt;div class="subtitle"&gt;<br/>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Nihil, voluptate unde quaerat velit quod deleniti debitis nobis laborum molestias nemo distinctio numquam doloremque? Officia, accusamus eveniet libero minima doloribus quis.<br/>
                        &lt;/div&gt;<br/>
                        &lt;div class="footer"&gt;<br/>
                          &lt;a href="https://www.google.com"&gt;Link utili&lt;/a&gt;<br/>
                        &lt;/div&gt;<br/>
                    &lt;/div&gt;<br/>
                  &lt;/body&gt;<br/>
                &lt;/html&gt;<br/>
                </Button>
              </ul>
              <br/>
              <br/>
              <Col sm="12">
                <img
                  alt="..."
                  className="rounded"
                  src={require("assets/img/screenshot_fs.png")}
                ></img>
              </Col>
            </Col>
          </Row>
          {/* Parse URL */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">Parse URL</h4>
              <h5 className="description">
                Il parsing di un URL (Uniform Resource Locator) è un processo che analizza una stringa di URL e la suddivide in componenti specifici1. Questo è utile quando si desidera estrarre informazioni specifiche da un URL, come il protocollo, l’host, il percorso, i parametri di query, ecc.
              </h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li>
                  <h5>Importare il modulo http<br/></h5>
                  <Button color="info" type="button" onClick={copiahttp} size="lg">
                    let http = require("http")
                  </Button>
                </li>
                <br/>
                <br/>
                <li>
                  <h5>Importare il modulo fs<br/></h5>
                  <Button color="info" type="button" onClick={copiafs} size="lg">
                    let fs = require("fs")
                  </Button>
                </li>
                <br/>
                <br/>
                <li>
                  <h5>Importare il modulo url<br/></h5>
                  <Button color="info" type="button" onClick={copiaurl} size="lg">
                    let url = require("url")
                  </Button>
                </li>
                <li>
                  <h5>Si ricrea la struttura base vista in precedenza, aggiungendo l'importazione del modulo <i>url</i>:</h5>
                  <Button color="info" type="button" onClick={copiaurl1} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>
                  let url = require("url")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                  <br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                </li>
                <br/>
                <br/>
                <li><h5>Si deve salvare all'interno di una variabile l'url, tramite la funzione <i>parse</i>:</h5></li>
                <Button color="info" type="button" onClick={copiaurl2} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>
                  let url = require("url")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    let mioURL = url.parse(req.url, true)<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
                <li><h5>Infine mediante uno switch si inseriscono i casi possibile del parse:</h5></li>
                <Button color="info" type="button" onClick={copiaurl3} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>
                  let url = require("url")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    let mioURL = url.parse(req.url, true)<br/>
                    switch (mioURL.path) &#123;<br/>
                      case "/":<br/>
                          res.end("HOME PAGE")<br/>
                          break;<br/>
                          <br/>
                      case "/stella":<br/>
                          res.end("Cane")<br/>
                          break;<br/>
                          <br/>
                      case "/maia":<br/>
                          res.end("gatto")<br/>
                          break;<br/>
                          <br/>
                      default:<br/>
                          res.end("Errore")<br/>
                          break;<br/>
                    &#125;<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
                <br/>
                <h5>Esempio completo</h5>
                <h5 className="description">Server.js</h5>
                <Button color="info" type="button" onClick={copiaurl3} size="lg">
                  let http = require("http")<br/>
                  let fs = require("fs")<br/>
                  let url = require("url")<br/>

                  http.createServer((req, resp) =&gt;&#123;<br/>
                    let mioURL = url.parse(req.url, true)<br/>
                    switch (mioURL.path) &#123;<br/>
                      case "/":<br/>
                          res.end("HOME PAGE")<br/>
                          break;<br/>
                          <br/>
                      case "/stella":<br/>
                          res.end("Cane")<br/>
                          break;<br/>
                          <br/>
                      case "/maia":<br/>
                          res.end("gatto")<br/>
                          break;<br/>
                          <br/>
                      default:<br/>
                          res.end("Errore")<br/>
                          break;<br/>
                    &#125;<br/>
                  &#125;).listen(3000)<br/>
                  </Button>
                <br/>
                <br/>
              </ul>
              <br/>
              <br/>
              <Row className="justify-content-center">
                <Col lg="12" md="12">
                  <Carousel
                    activeIndex={activeIndex}
                    next={next}
                    previous={previous}
                  >
                    <CarouselIndicators
                      items={items}
                      activeIndex={activeIndex}
                      onClickHandler={goToIndex}
                    />
                    {items.map((item) => {
                      return (
                        <CarouselItem
                          onExiting={onExiting}
                          onExited={onExited}
                          key={item.src}
                        >
                          <img src={item.src} alt={item.altText} />
                          <div className="carousel-caption d-none d-md-block">
                            <h5>{item.caption}</h5>
                          </div>
                        </CarouselItem>
                      );
                    })}
                    <a
                      className="carousel-control-prev"
                      data-slide="prev"
                      href="#pablo"
                      onClick={(e) => {
                        e.preventDefault();
                        previous();
                      }}
                      role="button"
                    >
                      <i className="now-ui-icons arrows-1_minimal-left"></i>
                    </a>
                    <a
                      className="carousel-control-next"
                      data-slide="next"
                      href="#pablo"
                      onClick={(e) => {
                        e.preventDefault();
                        next();
                      }}
                      role="button"
                    >
                      <i className="now-ui-icons arrows-1_minimal-right"></i>
                    </a>
                  </Carousel>
                </Col>
              </Row>
            </Col>
          </Row>
          {/* CommonJS */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">CommonJs</h4>
              <h5 className="description">
                CommonJS è un formato di modulo popolare utilizzato in Node.js. È stato uno dei primi tentativi di standardizzare un sistema di moduli JavaScript sul lato server. Ecco alcuni punti chiave su CommonJS:
                <ul>
                  <li>require() e module.exports: CommonJS introduce le funzioni <i>require()</i> e <i>module.exports</i> per importare ed esportare moduli1. Ad esempio, per importare un modulo in CommonJS, si utilizza <i>require()</i>, e per esportare funzioni o oggetti da un modulo, si utilizza <i>module.exports</i>.</li>
                  <li>Sincrono: CommonJS carica i moduli in modo sincrono, il che significa che quando si utilizza <i>require()</i>, l’esecuzione del codice si blocca fino a quando il modulo non viene caricato. Questo è ideale per lo scripting lato server, dove le operazioni I/O sono più veloci e non c’è bisogno di preoccuparsi del blocco dell’interfaccia utente.</li>
                  <li>Compatibilità con ES Modules: Node.js supporta sia <i>CommonJS</i> che <i>ES Modules (ESM)</i>. Tuttavia, ci sono alcune differenze tra i due. Ad esempio, <i>require()</i> non è supportato in <i>ESM</i>, e viceversa, import e export non sono supportati in <i>CommonJS</i>. Inoltre, <i>Node.js</i> interpreta i file .js come <i>CommonJS</i> a meno che non siano specificati diversamente nel campo type del file package.json.</li>
                </ul>
              </h5>
              <h5>Per utilizzare i moduli tramite <i>CommonJs</i> bisogna seguire i seguenti passaggi:</h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>mioModulo.js</i>”</h5></li>
                <li>
                  <h5>Creazione del modulo sul file <i>mioModulo.js</i><br/></h5>
                  <Button color="info" type="button" onClick={copiamodulo} size="lg">
                    exports.somma =(a,b)=&gt;&#123;<br/>
                        return (a+b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.sottrazione =(a,b)=&gt;&#123;<br/>
                        return (a-b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.moltiplicazione =(a,b)=&gt;&#123;<br/>
                        return (a*b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.divisione =(a,b)=&gt;&#123;<br/>
                        return (a/b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.resto =(a,b)=&gt;&#123;<br/>
                        return (a%b)<br/>
                    &#125;<br/>
                  </Button>
                </li>
                <li>
                  <h5>Importare del modulo creato all'interno del file <i>Server.js</i><br/></h5>
                  <Button color="info" type="button" onClick={copiamodulo1} size="lg">
                    let http = require("http")<br/>
                    let calcolatrice = require("./mioModulo")<br/>
                    <br/>
                    http.createServer((req, res) =&gt;&#123;<br/>
                    &#125;).listen("3000")<br/>
                  </Button>
                </li>
                <br/>
                <li><h5>Si eseguono le funzioni appena create nel modulo, per esempio la somma:</h5></li>
                <Button color="info" type="button" onClick={copiamodulo2} size="lg">
                    let http = require("http")<br/>
                    let calcolatrice = require("./mioModulo")<br/>
                    <br/>
                    http.createServer((req, res) =&gt;&#123;<br/>
                    res.end(minni.somma(5,7).toString())<br/>
                    &#125;).listen("3000")<br/>
                </Button>
                <br/>
                <br/>
                <br/>
                <h5>Esempio completo</h5>
                <h5 className="description">Server.js</h5>
                <Button color="info" type="button" onClick={copiamodulo2} size="lg">
                    let http = require("http")<br/>
                    let calcolatrice = require("./mioModulo")<br/>
                    <br/>
                    http.createServer((req, res) =&gt;&#123;<br/>
                    res.end(minni.somma(5,7).toString())<br/>
                    &#125;).listen("3000")<br/>
                </Button>
                <br/>
                <br/>
                <h5 className="description">mioModulo.js</h5>
                <Button color="info" type="button" onClick={copiamodulo} size="lg">
                    exports.somma =(a,b)=&gt;&#123;<br/>
                        return (a+b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.sottrazione =(a,b)=&gt;&#123;<br/>
                        return (a-b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.moltiplicazione =(a,b)=&gt;&#123;<br/>
                        return (a*b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.divisione =(a,b)=&gt;&#123;<br/>
                        return (a/b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.resto =(a,b)=&gt;&#123;<br/>
                        return (a%b)<br/>
                    &#125;<br/>
                  </Button>
              </ul>
              <br/>
              <br/>
              <Col sm="12">
                <img
                  alt="..."
                  className="rounded"
                  src={require("assets/img/screenshot_modulo.png")}
                ></img>
              </Col>
            </Col>
          </Row>
          {/* EsModules */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">EsModules</h4>
              <h5 className="description">
              I moduli ECMAScript (ES modules) sono il formato standard ufficiale per impacchettare il codice JavaScript per la riutilizzazione1. Ecco alcuni punti chiave su ES modules:
                <ul>
                  <li>Import ed export: I moduli ES sono definiti utilizzando una varietà di dichiarazioni di importazione ed esportazione. Ad esempio, per esportare una funzione da un modulo ES, si utilizza <i>export</i>, e per importare funzioni o oggetti da un modulo, si utilizza <i>import</i>.</li>
                  <li>Asincrono: A differenza di CommonJS, i moduli ES caricano i moduli in modo asincrono, il che significa che l’esecuzione del codice non si blocca quando si utilizza <i>import</i>.</li>
                  <li>Compatibilità con CommonJS: Node.js supporta sia CommonJS che ES Modules (ESM). Tuttavia, ci sono alcune differenze tra i due. Ad esempio, <i>import</i> e <i>export</i> non sono supportati in CommonJS, e viceversa, <i>require()</i> non è supportato in ESM. Inoltre, Node.js interpreta i file <i>.mjs</i> come ES modules.</li>
                </ul>
              </h5>
              <h5>Per utilizzare i moduli tramite <i>EsModules</i> bisogna seguire i seguenti passaggi:</h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>mioModulo.js</i>”</h5></li>
                <li>
                  <h5>Creazione del modulo sul file <i>mioModulo.js</i><br/></h5>
                  <Button color="info" type="button" onClick={copiamodulo} size="lg">
                    exports.somma =(a,b)=&gt;&#123;<br/>
                        return (a+b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.sottrazione =(a,b)=&gt;&#123;<br/>
                        return (a-b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.moltiplicazione =(a,b)=&gt;&#123;<br/>
                        return (a*b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.divisione =(a,b)=&gt;&#123;<br/>
                        return (a/b)<br/>
                    &#125;<br/>
                    <br/>
                    exports.resto =(a,b)=&gt;&#123;<br/>
                        return (a%b)<br/>
                    &#125;<br/>
                  </Button>
                </li>
                <br/>
                <li><h5>Si eseguono le funzioni appena create nel modulo, per esempio la somma:</h5></li>
                <Button color="info" type="button" onClick={copiamoduloEs2} size="lg">
                    import http from "http"<br/>
                    import &#123;somma, sottrazione&#125; from "./mioModulo.js"<br/>

                    http.createServer((req, res) =&gt;&#123;<br/>
                        res.end(somma(7,5).toString())<br/>
                    &#125;).listen("3000")<br/>
                </Button>
                <br/>
                <br/>
                <li>
                  <h5>Creazione del file <i>package.json</i>.<br/></h5>
                  <Button color="info" type="button" onClick={copiainit} size="lg">
                    npm init
                  </Button>
                </li>
                <br/>
                <br/>
                <li><h5>Modifica al file <i>package.json</i><br/>Si aggiunge tramite il tag <i>"type: "module";</i></h5></li>
                <Button color="info" type="button" onClick={copiapackage} size="lg">
                  &#123;
                    "name": "audisio",<br/>
                    "version": "1.0.0",<br/>
                    "description": "",<br/>
                    "type": "module",<br/>
                    "main": "server.js", <br/>
                    "scripts": &#123;<br/>
                      "test": "echo \"Error: no test specified\" && exit 1",<br/>
                      "start": "node server.js"<br/>
                    &#125;,<br/>
                    "author": "",<br/>
                    "license": "ISC"
                  &#125;
                </Button>
                <br/>
                <br/>
                <br/>
                <h5>Esempio completo</h5>
                <h5 className="description">Server.js</h5>
                <Button color="info" type="button" onClick={copiamoduloEs2} size="lg">
                    import http from "http"<br/>
                    import &#123;somma, sottrazione&#125; from "./mioModulo.js"<br/>

                    http.createServer((req, res) =&gt;&#123;<br/>
                        res.end(somma(7,5).toString())<br/>
                    &#125;).listen("3000")<br/>
                </Button>
                <br/>
                <br/>
                <h5 className="description">mioModulo.js</h5>
                <Button color="info" type="button" onClick={copiamoduloEs} size="lg">
                    export const somma =(a,b)=&gt;&#123;<br/>
                        return (a+b)<br/>
                    &#125;<br/>
                    <br/>
                    export const sottrazione =(a,b)=&gt;&#123;<br/>
                        return (a-b)<br/>
                    &#125;<br/>
                    <br/>
                    export const moltiplicazione =(a,b)=&gt;&#123;<br/>
                        return (a*b)<br/>
                    &#125;<br/>
                    <br/>
                    export const divisione =(a,b)=&gt;&#123;<br/>
                        return (a/b)<br/>
                    &#125;<br/>
                    <br/>
                    export const resto =(a,b)=&gt;&#123;<br/>
                        return (a%b)<br/>
                    &#125;<br/>
                  </Button>
                <br/>
                <br/>
                <h5 className="description">package.json</h5>
                <Button color="info" type="button" onClick={copiapackage} size="lg">
                  &#123;
                      "name": "audisio",<br/>
                      "version": "1.0.0",<br/>
                      "description": "",<br/>
                      "type": "module",<br/>
                      "main": "server.js", <br/>
                      "scripts": &#123;<br/>
                        "test": "echo \"Error: no test specified\" && exit 1",<br/>
                        "start": "node server.js"<br/>
                      &#125;,<br/>
                      "author": "",<br/>
                      "license": "ISC"
                    &#125;
                </Button>
              </ul>
              <br/>
              <br/>
              <Col sm="12">
                <img
                  alt="..."
                  className="rounded"
                  src={require("assets/img/screenshot_modulo.png")}
                ></img>
              </Col>
            </Col>
          </Row>
          {/* Async / Await */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">Async / Await</h4>
              <h5 className="description">
                In Node.js, <i>async</i> e <i>await</i> sono utilizzati per gestire le operazioni asincrone. Sono un modo più pulito e leggibile per gestire le promesse.
                <ul>
                <li>
                  Async: La parola chiave <i>async</i> viene utilizzata per dichiarare una funzione come asincrona. Le funzioni asincrone restituiscono sempre una promessa, anche se non si scrive esplicitamente per farlo. Questo significa che è possibile utilizzare il metodo <i>.then()</i> o <i>.catch()</i> con una funzione asincrona.
                </li>
                <li>
                  Await: La parola chiave <i>await</i> viene utilizzata all’interno di una funzione asincrona per attendere che una promessa sia risolta o rifiutataawait blocca l’esecuzione del codice fino a quando la promessa non è risolta.
                </li>
                </ul>
              </h5>
              <ul>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>Server.js</i>”</h5></li>
                <li>
                  <h5>Esempio:<br/></h5>
                  <Button color="info" type="button" onClick={copiaasync} size="lg">
                    const somma = async()=&gt;&#123;<br/>
                        await fetch('https://v2.jokeapi.dev/joke/Programming?type=single')<br/>
                        .then(res =&gt; res.json())<br/>
                        .then(json =&gt; console.log(json.joke))<br/>
                    &#125;<br/>
                  </Button>
                </li>
                <br/>
                <br/>
              </ul>
              <br/>
              <br/>
            </Col>
          </Row>
          {/* EJS */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">EJS</h4>
              <h5 className="description">
              EJS, che sta per “Embedded JavaScript”, è un semplice linguaggio di templating che ti permette di generare markup HTML con JavaScript puro. Ecco alcune delle sue caratteristiche principali:
              <ul>
                <li>Sintassi semplice: Il codice JavaScript viene scritto in semplici tag scriptlet. Basta scrivere il codice JavaScript che emette l’HTML che desideri.</li>
                <li>Esecuzione veloce: EJS mette in cache le funzioni JS intermedie per un’esecuzione rapida.</li>
                <li>Debugging facile: È facile risolvere gli errori di EJS: i tuoi errori sono eccezioni JavaScript semplici, con i numeri di riga del template inclusi.</li>
                <li>Sviluppo attivo: EJS ha una grande comunità di utenti attivi, e la libreria è in continuo sviluppo.</li>
                <li>Supporto per il browser: EJS supporta sia il server JS che il browser</li>
              </ul>
              </h5>
              <h5>Per utilizzare <i>EJS</i> bisogna seguire i seguenti passaggi:</h5>
              <ul>
                <li><h5>Installare ejs da terminale tramite il comando:</h5><br/>
                  <Button color="info" type="button" onClick={copiainstallejs} size="lg">
                      npm install ejs
                    </Button>
                </li>
                <li><h5>Installare express da terminale tramite il comando:</h5><br/>
                  <Button color="info" type="button" onClick={copiainstallexpress} size="lg">
                      npm install express
                    </Button>
                </li>
                <br/>
                <li><h5>Creare una cartella</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>app.js</i>”</h5></li>
                <li><h5>Creare un file all’interno della cartella chiamato “<i>index.ejs</i>” all'interno di una cartella chiamata <i>"views"</i></h5></li>
                <li><h5>Si inizia a lavorare sul file <i>app.js</i> andando a importare express:</h5></li>
                <Button color="info" type="button" onClick={copiaimportexpress} size="lg">
                  const express = require('express');<br/>
                  const app = express();
                </Button>
                <br/>
                <br/>
                <li>
                  <h5>Si va a impostare <i>view engine, ejs</i> sulla variabile app appena creata<br/></h5>
                  <Button color="info" type="button" onClick={copiasetejs} size="lg">
                    app.set('view engine', 'ejs');
                  </Button>
                </li>
                <br/>
                <br/>
                <li><h5>Mediante il comando <i>.get</i> si imposta il file di riferimento ed eventuali variabili, come in questo caso il nome: <i>Mario</i></h5></li>
                <Button color="info" type="button" onClick={copiagetejs} size="lg">
                  app.get('/', function(req, res) &#123;<br/>
                      res.render('index', &#123; nome: 'Mario' &#125;);<br/>
                  &#125;);
                </Button>
                <br/>
                <br/>
                <li><h5>Mediante il comando <i>.listen</i> si imposta la porta dove mettere in ascolto in server</h5></li>
                <Button color="info" type="button" onClick={copialistenejs} size="lg">
                  app.listen(3000, function() &#123;<br/>
                      console.log('App in ascolto sulla porta 3000');<br/>
                  &#125;);
                </Button>
                <br/>
                <br/>
                <li><h5>Si modifica il file <i>index.ejs</i> andando a impostare mediante il comando <i>&lt;%= variabile %&gt;</i> le variabile impostate nel file <i>app.js</i></h5></li>
                <Button color="info" type="button" onClick={copiaejs} size="lg">
                  &lt;!DOCTYPE html&gt;<br/>
                  &lt;html&gt;<br/>
                    &lt;head&gt;<br/>
                      &lt;title&gt;Esempio EJS&lt;/title&gt;<br/>
                    &lt;/head&gt;<br/>
                  &lt;body&gt;<br/>
                  &lt;h1&gt;Ciao, &lt;%= nome %&gt;!&lt;/h1&gt;<br/>
                    &lt;p&gt;Benvenuto nel nostro sito web.&lt;/p&gt;<br/>
                  &lt;/body&gt;<br/>
                  &lt;/html&gt;<br/>
                </Button>
                <br/>
                <br/>
                <li><h5>Per avviare il progetto, si utilizza il comando da terminale <i>node app.js</i></h5></li>
                <br/>
                <br/>
                <br/>
                <h5>Esempio completo</h5>
                <h5 className="description">app.js</h5>
                <Button color="info" type="button" onClick={copiaexpress} size="lg">
                  const express = require('express');<br/>
                  const app = express();<br/>
                  <br/>
                  app.set('view engine', 'ejs');<br/>
                  <br/>
                  app.get('/', function(req, res) &#123;<br/>
                      res.render('index', &#123; nome: 'Mario' &#125;);<br/>
                  &#125;);<br/>
                  <br/>
                  app.listen(3000, function() &#123;<br/>
                      console.log('App in ascolto sulla porta 3000');<br/>
                  &#125;);<br/>

                </Button>
                <br/>
                <br/>
                <h5 className="description">index.ejs</h5>
                <Button color="info" type="button" onClick={copiaejs} size="lg">
                  &lt;!DOCTYPE html&gt;<br/>
                  &lt;html&gt;<br/>
                    &lt;head&gt;<br/>
                      &lt;title&gt;Esempio EJS&lt;/title&gt;<br/>
                    &lt;/head&gt;<br/>
                  &lt;body&gt;<br/>
                  &lt;h1&gt;Ciao, &lt;%= nome %&gt;!&lt;/h1&gt;<br/>
                    &lt;p&gt;Benvenuto nel nostro sito web.&lt;/p&gt;<br/>
                  &lt;/body&gt;<br/>
                  &lt;/html&gt;<br/>
                </Button>
              </ul>
              <br/>
              <br/>
              <Col sm="12">
                <img
                  alt="..."
                  className="rounded"
                  src={require("assets/img/screenshot_ejs.png")}
                ></img>
              </Col>
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}

export default Nodejs;