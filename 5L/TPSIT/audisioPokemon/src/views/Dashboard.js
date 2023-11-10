import React from "react";
import classNames from "classnames";
import { Line, Bar } from "react-chartjs-2";

// reactstrap components
import {
  Button,
  ButtonGroup,
  Card,
  CardHeader,
  CardBody,
  CardTitle,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  UncontrolledDropdown,
  Label,
  FormGroup,
  Input,
  Table,
  Row,
  Col,
  UncontrolledTooltip,
} from "reactstrap";

// core components
import {
  chartExample1,
  chartExample2,
  chartExample3,
  chartExample4,
} from "variables/charts.js";

function Dashboard(props) {
  const [bigChartData, setbigChartData] = React.useState("data1");
  const setBgChartData = (name) => {
    setbigChartData(name);
  };

  // Dati del programmatore
  const programmerInfo = {
    nome: "Nicolò",
    cognome: "Audisio",
    bio: "Ciao, sono Nicolò Audisio, ho 18 anni e abito in un piccolo paesino della provincia di Cuneo con circa  tremila persone. Ho iniziato il mio percorso di studi presso l'IIS 'G. Rivoira' nel 2019 con l'obiettivo di diventare un programmatore di siti web e di applicazioni. Tuttavia, durante la quarantena ho sviluppato una passione per le forze armate e le forze di polizia. Ho approfondito l'argomento e ho deciso che il mio futuro sarà nell'ambito della Pubblica Sicurezza, mantenendo sempre la passione per l'informatica. Sentivo la necessità di mettermi a disposizione della società, di essere quella 'mano invisibile' che può aiutare le persone bisognose. Per realizzare questo desiderio, nel novembre 2022 ho deciso di entrare a far parte della Croce Rossa Italiana, presso il comitato territoriale di Manta. Dopo aver superato tutti gli esami necessari per diventare soccorritore volontario del 118, ho svolto un periodo semestrale di tirocinio, conclusosi nell'agosto 2023 con un totale di oltre 200 ore di volontariato, accumulate in un periodo di 5 mesi.",
    imageSrc: require("./me.jpg"), // Importa l'immagine
  };

  return (
    <>
      <div className="content">
        <Row>
          <Col xs="12">
            <Card className="card-chart">
              <CardHeader>
                <Row>
                  <Col className="text-left" sm="6">
                    <h5 className="card-category"></h5>
                    <CardTitle tag="h2">Carte Totali Italiane</CardTitle>
                  </Col>
                  <Col sm="6">
                    <ButtonGroup
                      className="btn-group-toggle float-right"
                      data-toggle="buttons"
                    >
                      <Button
                        tag="label"
                        className={classNames("btn-simple", {
                          active: bigChartData === "data1",
                        })}
                        color="info"
                        id="0"
                        size="sm"
                        onClick={() => setBgChartData("data1")}
                      >
                        <span className="d-none d-sm-block d-md-block d-lg-block d-xl-block">
                          Carte Collezionabili Italiane
                        </span>
                        <span className="d-block d-sm-none">
                          <i className="tim-icons icon-single-02" />
                        </span>
                      </Button>
                    </ButtonGroup>
                  </Col>
                </Row>
              </CardHeader>
              <CardBody>
                <div className="chart-area">
                  <Line
                    data={chartExample1[bigChartData]}
                    options={chartExample1.options}
                  />
                </div>
              </CardBody>
            </Card>
          </Col>
        </Row>

        {/* Card per la presentazione del programmatore */}
        <Row>
          <Col xs="12" sm="6" className="mt-5">
            <Card>
              <CardHeader>
                <h5 className="card-category">Programmatore</h5>
                <CardTitle tag="h4">
                  {programmerInfo.nome} {programmerInfo.cognome}
                </CardTitle>
              </CardHeader>
              <CardBody>
                <p>{programmerInfo.bio}</p>
              </CardBody>
            </Card>
          </Col>
          <Col xs="12" sm="6" className="mt-5">
            <Card>
              <CardHeader>
                <img
                  src={programmerInfo.imageSrc}
                  alt="Immagine del programmatore"
                  style={{ maxWidth: "50%", marginBottom: "15px" }}
                />
              </CardHeader>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default Dashboard;