import React from "react";

// reactstrap components
import {
  Container,
  Row,
  Col,
} from "reactstrap";

// core components

function Giletta() {
  return (
    <>
      <Container>
      <h2 className="title">Franco Giletta</h2>
        <Col className="mr-auto ml-auto" md="3" sm="6">
            <img
              alt="..."
              className="img-circle img-no-padding img-responsive"
              src="https://www.lavalsusa.it/wp-content/uploads/2022/03/Franco-Giletta--scaled.jpg"
            />
        </Col>
        <Col className="mr-auto ml-auto">
          <h3>
            Franco Giletta nasce a Saluzzo (Cn) nel 1967, dove ancora tutt’oggi risiede. Durante la sua carriera ha avuto numerose opportunità per mettersi in mostra e per dimostrare quello che meglio sa fare, dipingere. Durante gli anni universitari passati presso la capitale ha avuto modo di frequentare l’ambienta artistico. Nel 1995 intraprese un’attività espositiva in Italia e all’estero e sempre lo stesso anno fu invitato, come unico italiano dell’anno, dalla Royal Society of Portrait Claret di Londra per l’esposizione annuale dei ritrattisti. Oltre all’arte ritrattista, ha praticato anche l’arte sacra, dove nel 2004 una sua opera “S. Antonio Maria Claret” fu collocata presso la Chiesa di Santa Lucia del Gonfalone a Roma. Sette anni dopo fu invitato dal Prof. Vittorio Sgarbi al Padiglione Regionale della 54° Biennale di Venezia. Le sue opere sono presente all’interno di collezioni private sia in Italia che all’estero, tra cui all’interno del Museo Stauros e la collezione Bulgari. Negli anni a seguire realizzò il doppio ritratto di Lucia Bosè e Magaly Solier per il film “Alfonsina y el mar”, espose la sua opera “Il Tesoro d’Italia” all’Expo di Milano del 2015 e realizzò un dipinto per la sede di Eataly al World Trade Center di New York. Negli anni a venire, Giletta, intraprese anche la via della scrittura, dove abbiamo potuto vedere in prima persona l’effetto che 10 anni fa scoprì sulla collina di saluzzo, sul quale decise di scrivere un <a target={"_blank"} href={"https://www.mondadoristore.it/ombra-torre-Saluzzo-enigma-Franco-Giletta/eai979128074926/"}>libro</a>.
            Dal chiostro si può accedere al refettorio dove, oltre al pregevole soffitto a cassettoni, si può ammirare il grande Affresco della Crocifissione, risalente ai primi del XVI secolo. I domenicani officiarono la chiesa fino al 1802, quando fu soppressa dalle autorità napoleoniche.
          </h3>
        </Col>
      </Container>
    </>
  );
}

export default Giletta;
