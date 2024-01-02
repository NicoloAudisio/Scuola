import React from "react";

// reactstrap components
import {
  Button,
  Container,
  UncontrolledTooltip
} from "reactstrap";

// core components
import ProfilePageHeader from "./Profile";

function ProfilePage() {
  React.useEffect(() => {
    document.body.classList.add("profile-page");
    document.body.classList.add("sidebar-collapse");
    document.documentElement.classList.remove("nav-open");
    window.scrollTo(0, 0);
    document.body.scrollTop = 0;
    return function cleanup() {
      document.body.classList.remove("profile-page");
      document.body.classList.remove("sidebar-collapse");
    };
  }, []);
  return (
    <>
      <div className="wrapper">
        <ProfilePageHeader />
        <div className="section">
          <Container>
            <div className="button-container">
              <Button
                className="btn-round btn-icon"
                color="info"
                id="tooltip515203352"
                size="lg"
                href="https://www.instagram.com/nik_audisio_/"
                target="_blank"
              >
                <i className="fab fa-instagram"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip515203352">
                Follow me on Instagra
              </UncontrolledTooltip>
              <Button
                className="btn-round btn-icon"
                color="info"
                id="tooltip340339231"
                size="lg"
                href="https://www.facebook.com/nik.audisio/"
                target="_blank"
              >
                <i className="fab fa-facebook"></i>
              </Button>
              <UncontrolledTooltip delay={0} target="tooltip340339231">
                Follow me on Facebook
              </UncontrolledTooltip>
            </div>
            <h3 className="title">About me</h3>
            <h5 className="description">
            Mi chiamo Nicolò Audisio, ho 18 anni e studio informatica. Sono appassionato di tecnologia e del suo potenziale per risolvere problemi complessi.<br/>
            Oltre ai miei studi, dedico il mio tempo come barelliere volontario presso la Croce Rossa di Manta. Questo ruolo riflette il mio impegno verso il servizio comunitario e il mio desiderio di aiutare gli altri in situazioni di emergenza.<br/>
            Sono anche un appassionato delle forze dell’ordine, che rispecchia il mio rispetto per coloro che lavorano per mantenere la sicurezza e l’ordine. La mia dedizione al soccorso e alle forze dell’ordine mostra il mio spirito altruista e il mio impegno verso il benessere della mia comunità.<br/>
            </h5>
          </Container>
        </div>
      </div>
    </>
  );
}

export default ProfilePage;
