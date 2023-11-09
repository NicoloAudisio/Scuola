import React from "react";

import {
  Container,
  Row,
  Col,
} from "reactstrap";

function Intro() {
  return (
    <>
      <div className="section section-buttons">
        <Container>
          <div className="title">
            <h2>Uscita sul territorio</h2>
          </div>
          <div>
            <h4>Giovedì 22 dicembre abbiamo assistito ad un incontro su un fenomeno molto interessante, ovvero l'ombra del campanile civico che si allinea perfettamente sul campanile della chiesa di S.Giovanni. Questa visita è stata guidata dal professor Giletta che ha scoperto il fenomeno. Le pagine seguenti tratteranno dell'ombra sul campanile della chiesa di S. Giovanni e del professor Giletta.</h4>
          </div>
          <br/>
          <div>
            <h3>Questo fenomeno dell'ombra si presenta a partire dal solstizio d'inverno all'epifania circa, il fenomeno si verifica alle undici del mattino circa e dura un minuto. Il campanile della chiesa di S. Giovanni è posizionato circa a quarantacinque gradi rispetto al campanile civico e ciò permette a quest'ultimo con la sua ombra di andare a coprire l'intero campanile della chiesa.</h3>
          </div>
          <br/>
          <div id="images">
            <br/>
            <br/>
            <Row>
              <Col className="mr-auto ml-auto" md="3" sm="6">
                <img
                  alt="..."
                  className="img-rounded img-responsive"
                  src='https://maxgiu.github.io/IMG/campanile3.jpeg'
                />
                <p className="text-center">Foto del campanile</p>
              </Col>
              <Col className="mr-auto ml-auto" md="3" sm="6">
              <img
                  alt="..."
                  className="img-rounded img-responsive"
                  src='https://maxgiu.github.io/IMG/campanile4.jpeg'
                />
                <p className="text-center">Foto pochi minuti prima del fenomeno</p>
              </Col>
            </Row>
          </div>
        </Container>
      </div>
    </>
  );
}

export default Intro;
