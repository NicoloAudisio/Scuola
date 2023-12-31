import React from "react";

// reactstrap components
import {
  Button,
  Container,
  Col,
} from "reactstrap";

// core components
function Introduzione() {

  const copiaControlloVersione = () => {
      navigator.clipboard.writeText('node -v');
  };

  const copiaInstallanpm = () => {
    navigator.clipboard.writeText('npm install -g npm');
  };

  const copiaInstallnodemon = () => {
    navigator.clipboard.writeText('npm install -g nodemon');
  };

  return (
    <>
      <div className="section section-basic" id="basic-elements">
        <Container>
          <br/>
          <br/>
          <Col className="text-center" lg="15" md="15">
              <h1 className="title">NodeJs</h1>
              <h5 className="description">
              Node.js è un ambiente di runtime JavaScript open-source e multipiattaforma che esegue il motore JavaScript V8. È noto per le sue prestazioni e viene utilizzato in vari tipi di progetti. Node.js gestisce le operazioni di I/O in modo asincrono, evitando il blocco del codice. Questo permette a Node.js di gestire molte connessioni simultanee senza la necessità di gestire la concorrenza dei thread. Inoltre, Node.js ha reso possibile per gli sviluppatori frontend scrivere codice lato server. Infine, Node.js supporta i nuovi standard ECMAScript senza dover attendere l’aggiornamento dei browser da parte degli utenti.
              </h5>
          </Col>
          <br/>
          <br/>
          <h3>Controllo della versione</h3>
          <h5>Prima di iniziare a programmare, bisogna controllare se si ha installato Node JS e che versione si ha.<br/>
          Questa operazione si fa, aprendo il terminale digitando:</h5>
          <Button color="info" type="button" onClick={copiaControlloVersione} size="lg">
            node -v
          </Button>
          <br/>
          <br/>
          <h5>Il terminale dovrebbe riportare:</h5>
          <Button color="info" type="button"size="lg">
            ~ % node -v<br/>
            v18.17.
          </Button>
          <br/>
          <h5>Questo significa che sul nostro dispositivo è presente la verso 18.17.0</h5>
          <h4 className="text-danger">Se il terminale non ritorna niente, si vede installare NodeJs</h4>
          <Button color="info" type="button" onClick={copiaInstallanpm} size="lg">
          npm install -g npm
          </Button>
          <br/>
          <br/>
          <h5>Installare nodemon.<br/>
          Nodemon permette l'aggiornamento del file che andremo a usare come server senza doverlo fermare e farlo ripartire.<br/>
          Si installa tramite il comando:</h5>
          <Button color="info" type="button" onClick={copiaInstallnodemon} size="lg">
            npm install -g nodemon
          </Button>
        </Container>
      </div>
    </>
  );
}

export default Introduzione;