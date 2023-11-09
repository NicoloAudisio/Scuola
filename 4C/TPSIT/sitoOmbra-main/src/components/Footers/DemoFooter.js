import React from "react";

// reactstrap components
import { Row, Container } from "reactstrap";

function DemoFooter() {
  return (
    <footer className="footer footer-black footer-white">
      <Container>
        <Row>
          <nav className="footer-nav">
            <ul>
              <li>
                Audisio Nicolò
              </li>
              <li>
                Giusiano Massimo
              </li>
              <li>
                I.T.I.S. G. Rivoira, Verzuolo (CN)
              </li>
            </ul>
          </nav>
        </Row>
      </Container>
    </footer>
  );
}

export default DemoFooter;
