import React from "react";

// reactstrap components
import { Container, Row, Col } from "reactstrap";

// core components

function SectionDark() {
  return (
    <>
      <div className="section section-dark">
        <Container>
        <h2 className="title">Chiesa di San Giovanni</h2>
        <br/>
          <Row>
              <Col className="mr-auto ml-auto" md="6" sm="6">
                <img
                  alt="..."
                  className="img-rounded img-responsive"
                  src='https://maxgiu.github.io/IMG/campanile4.jpeg'
                />
                <p className="text-center">Foto del campanile</p>
              </Col>
              <Col className="mr-auto ml-auto" md="3" sm="6">
                <p className="description">
                  La chiesa di San Giovanni, la protagonista di questo fenomeno, è uno splendido esempio di architettura gotica. Consacrata a San Giovanni Battista, fu la chiesa principale della città fino al 1501. Fu eretta nel 1281 in sostituzione di una cappella dedicata a Santa Maria nel 1230. Il grande affresco raffigurante San Cristoforo presente sulla facciata principale della chiesa è invece un noto falso storico, poiché dipinto soltanto nel 1929 da Ovidio Fonti; sfortunatamente durante la nostra visita l’affresco era coperto dai ponteggi per dei lavori di ristrutturazione, però a scaglioni siamo riusciti ad ammirare così tanta bellezza.
                  L'interno della chiesa è suddiviso in tre navate con volte a crociera ed è accessibile dopo aver sceso il suggestivo scalone in pietra, che separa il portale dalla navata centrale. L'inconsueta collocazione di questo elemento architettonico è anch'essa frutto dell'ultimo rimaneggiamento del 1376 e conferisce alla chiesa una caratteristica di unicità nel suo genere. Lungo le navate laterali sono dislocate varie cappelle fra le quali quella dedicata ai santi Crispino e Crispiniano e quella decorata dal ciclo di affreschi riguardanti le Storie della passione di Cristo, risalente al XV secolo. Degna di nota è anche la cappella del Rosario, dove è custodito un bellissimo esemplare di trittico ad opera di Oddone Pascale del 1535.
                  In essa si trova la cappella funeraria dei Marchesi di Saluzzo, una delle testimonianze di gotico fiammeggiante più importanti del Piemonte. Gli scranni del coro ligneo provengono invece dall'Abbazia di Sant'Antonio di Ranverso e risalgono al XV secolo. Sul lato opposto si trova la cappella Cavassa, che ospita il monumento funebre del vicario generale del marchesato Galeazzo Cavassa. È dotata di portale in marmo bianco, opera dello scultore Matteo Sanmicheli e contiene affreschi risalenti al XVI secolo.
                  Dal chiostro si può accedere al refettorio dove, oltre al pregevole soffitto a cassettoni, si può ammirare il grande Affresco della Crocifissione, risalente ai primi del XVI secolo. I domenicani officiarono la chiesa fino al 1802, quando fu soppressa dalle autorità napoleoniche.
                </p>
              </Col>
            </Row>
        </Container>
      </div>
    </>
  );
}

export default SectionDark;
