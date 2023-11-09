import React from "react";

// reactstrap components

// core components
import IndexNavbar from "components/Navbars/IndexNavbar.js";
import IndexHeader from "components/Headers/IndexHeader.js";
import DemoFooter from "components/Footers/DemoFooter.js";

// index sections
import Intro from "views/index-sections/Intro.js";
import Chiesa from "views/index-sections/Chiesa.js";
import Giletta from "views/index-sections/Giletta.js";
import Crediti from "views/index-sections/Crediti.js";

function Index() {
  document.documentElement.classList.remove("nav-open");
  React.useEffect(() => {
    document.body.classList.add("index");
    return function cleanup() {
      document.body.classList.remove("index");
    };
  });
  return (
    <>
      <IndexNavbar />
      <IndexHeader />
      <div className="main">
        <Intro />
        <Chiesa />
        <Giletta />
        <Crediti />
        <DemoFooter />
      </div>
    </>
  );
}

export default Index;
