import React from "react";

// reactstrap components
import { Container } from "reactstrap";

// core components

function IndexHeader() {
  return (
    <>
      <div
        className="page-header section-dark"
        style={{
          backgroundImage: "url(" + require("assets/img/chiesaSanGiovanni.jpg") + ")"
        }}
      >
        <div className="filter" />
        <div className="content-center">
          <Container>
            <div className="title-brand">
              <h1 className="presentation-title">L'ombra sul campanile</h1>
            </div>
            <h2 className="presentation-subtitle text-center">
              Fenomeno osservato a Saluzzo (CN) il 22 dicembre 2022
            </h2>
          </Container>
        </div>
      </div>
    </>
  );
}

export default IndexHeader;
