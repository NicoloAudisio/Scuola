import React from "react";

// reactstrap components
import { 
  Button,
  Container,
  Row,
  Col,
  Badge,
} from "reactstrap";

// core components

function Nodejs() {
  const copiahttp = () => {
    navigator.clipboard.writeText('let http = require("http")');
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

  const copiafs1 = () => {
    navigator.clipboard.writeText(`
      let http = require("http")
      let fs = require("fs")
      
      http.createServer((req, resp) =>{
        resp.end()
      }).listen(3000)
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
                Creazione del primo progetto
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                Passaggio di una pagina HTML
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
               Parse URL
              </Badge>
              <Badge color="info" className="mr-3 mt-4">
                Importazione dei moduli
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
                Express
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
          {/* Passaggio di una pagina HTML */}
          <Row className="justify-content-md-center">
            <Col className="text-left" lg="8" md="12">
              <br/>
              <br/>
              <h4 className="title">Passaggio di una pagina HTML</h4>
              <h5 className="description">
                Per rendere più dinamici le pagine web che si realizzano, si può utilizzare il modulo <i>fs</i> per collegare più pagine tra loro.<br/>
              </h5>
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





          {/* <br></br>
          <br></br>
          <br></br>
          <Row className="text-center mt-5">
            <Col className="ml-auto mr-auto" md="8">
              <h2>Want more?</h2>
              <h5 className="description">
                We're going to launch{" "}
                <a
                  href="http://demos.creative-tim.com/now-ui-kit-pro-react/#/presentation?ref=nukr-index-page"
                  onClick={(e) => e.preventDefault()}
                >
                  Now UI Kit PRO React
                </a>
                . It will have huge number of components, sections and example
                pages so you can start your development with a badass Bootstrap
                4 UI Kit.
              </h5>
            </Col>
            <Col md="12">
              <Button
                className="btn-neutral btn-round"
                color="default"
                href="http://creative-tim.com/product/now-ui-kit-pro-react?ref=nukr-index-page"
                size="lg"
                target="_blank"
              >
                <i className="now-ui-icons arrows-1_share-66 mr-1"></i>
                Upgrade to PRO
              </Button>
            </Col>
          </Row>
          <br></br>
          <br></br>
          <Row className="justify-content-md-center sharing-area text-center">
            <Col className="text-center" lg="8" md="12">
              <h3>Thank you for supporting us!</h3>
            </Col>
            <Col className="text-center" lg="8" md="12">
              <Button
                className="btn-neutral btn-icon btn-round"
                color="twitter"
                href="https://www.twitter.com/creativetim?ref=creativetim"
                id="tooltip86114138"
                size="lg"
                target="_blank"
              >
                <i className="fab fa-twitter"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip86114138">
                Follow us
              </UncontrolledTooltip>
              <Button
                className="btn-neutral btn-icon btn-round"
                color="facebook"
                href="https://www.facebook.com/creativetim?ref=creativetim"
                id="tooltip735272548"
                size="lg"
                target="_blank"
              >
                <i className="fab fa-facebook-square"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip735272548">
                Like us
              </UncontrolledTooltip>
              <Button
                className="btn-neutral btn-icon btn-round"
                color="linkedin"
                href="https://www.linkedin.com/company-beta/9430489/?ref=creativetim"
                id="tooltip647117716"
                size="lg"
                target="_blank"
              >
                <i className="fab fa-linkedin"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip647117716">
                Follow us
              </UncontrolledTooltip>
              <Button
                className="btn-neutral btn-icon btn-round"
                color="github"
                href="https://github.com/creativetimofficial/now-ui-kit-react?ref=creativetim"
                id="tooltip331904895"
                size="lg"
                target="_blank"
              >
                <i className="fab fa-github"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip331904895">
                Star on Github
              </UncontrolledTooltip>
            </Col>
          </Row> */}
        </Container>
      </div>
    </>
  );
}

export default Nodejs;
