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
              NodeJS è un framwork che permette la programmazione lato server, che può essere utile per unificare la stessa pagina web su più dispositivi, per esempio se si parla di Amazon, tutte le pagine che vengono aperte vedere vedere la quantità disponibile aggiornata in automatica in base agli acquisti che vengono fatti.
              La funzione di PHP è quella di inviare una pagina HTML, CSS e JS al computer che effettua la richiesta, mentre Node JS serve per realizzare un servizio.
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