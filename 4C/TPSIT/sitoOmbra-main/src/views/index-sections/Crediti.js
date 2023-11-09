import React from "react";

// reactstrap components
import {
  NavItem,
  NavLink,
  Nav,
  Pagination,
  PaginationItem,
  PaginationLink,
  Progress,
  TabContent,
  TabPane,
  Container,
  Row,
  Col
} from "reactstrap";

// core components

function Crediti() {
  const [activeTab, setActiveTab] = React.useState("1");
  const toggle = (tab) => {
    if (activeTab !== tab) {
      setActiveTab(tab);
    }
  };
  return (
    <>
      <div className="section">
        <Container>
          <div className="title">
              <h2>Crediti</h2>
              <br/>
          </div>
          <Row>
            <Col md="6">
              <h3>Audisio Nicolò</h3>
              <br />
              <p className="description">
                ● Progettazione e realizzazione della pagina su Giletta<br/>
                ● Progettazione e realizzazione della pagina della Chiesa di San Giovanni<br/>
                ● Progettazione e realizzazione della pagina dei crediti<br/>
                ● Fotografie<br/>
              </p>
            </Col>  
            <Col md="6">
            <h3>Giusiano Massimo</h3>
              <br />
              <p className="description">
                ● Progettazione e realizzazione della home page<br/>
                ● Progettazione e realizzazione della navbar<br/>
                ● Progettazione e realizzazione della pagina sull'ombra<br/>
                ● Testi<br/>
              </p>
            </Col>  
          </Row>
        </Container>
      </div>
    </>
  );
}

export default Crediti;
