import React, { useState, useEffect } from "react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardText,
  Row,
  Col,
  Button,
  Input,
} from "reactstrap";

function Gcc() {
  const [pokemonData, setPokemonData] = useState([]);
  const [carteAggiunte, setCarteAggiunte] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredPokemonData, setFilteredPokemonData] = useState([]);

  // Funzione per caricare i dati delle carte dal localStorage
  function caricaCarteDaLocalStorage() {
    const carteLocalStorage = localStorage.getItem("carteAggiunte");
    if (carteLocalStorage) {
      setCarteAggiunte(JSON.parse(carteLocalStorage));
    }
  }

  // Funzione per salvare i dati delle carte su localStorage
  function salvaCarteSuLocalStorage(carte) {
    localStorage.setItem("carteAggiunte", JSON.stringify(carte));
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          "https://raw.githubusercontent.com/MattiaBracco05/Pokemon/main/pokemon.json"
        );

        if (!response.ok) {
          throw new Error("Errore nella richiesta dei dati.");
        }

        const data = await response.json();
        setPokemonData(data[0].figurine); // Utilizziamo solo le figurine dal formato JSON
        caricaCarteDaLocalStorage();
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const risultatiRicerca = pokemonData.filter((pokemon) =>
      pokemon.nome.toLowerCase().includes(searchQuery.toLowerCase())
    );

    setFilteredPokemonData(risultatiRicerca);
  }, [searchQuery, pokemonData]);

  const aggiungiCarta = (pokemon) => {
    const nuoveCarte = [...carteAggiunte, pokemon];
    setCarteAggiunte(nuoveCarte);
    salvaCarteSuLocalStorage(nuoveCarte);
  };

  const eliminaCarta = (numero) => {
    const nuoveCarte = carteAggiunte.filter((carta) => carta.numero !== numero);
    setCarteAggiunte(nuoveCarte);
    salvaCarteSuLocalStorage(nuoveCarte);
  };

  return (
    <>
      <style>
        {`
          .pokemon_image {
            filter: grayscale(100%);
          }

          .pokemon_image.color {
            filter: none;
          }
        `}
      </style>
      <div className="content">
        <Row>
          <Col md="12">
            <Card>
              <CardHeader className="mb-5">
                <h5 className="card-category">Carte Possedute</h5>
                <CardTitle tag="h3">Elenco del tuo pokedex</CardTitle>
              </CardHeader>
            </Card>
          </Col>
        </Row>
        <div className="content">
          <Row>
            {carteAggiunte.map((carta) => {
              return (
                <Col md="4" key={carta.numero}>
                  <Card>
                    <CardHeader className="mb-5">
                      <h5 className="card-category">
                        {carta.stadio_evolutivo}
                      </h5>
                      <CardTitle tag="h3">{carta.nome}</CardTitle>
                      <CardText>
                        <img
                          alt="..."
                          className={`pokemon_image color`}
                          src={carta.url}
                        />
                        <br />
                        <br />Numero: <label>{carta.numero}</label>{" "}
                        <br />
                        Abilità:{" "}
                        <label>{carta.abilita.join(", ")}</label>{" "}
                        <br />
                      </CardText>
                      <Button onClick={() => eliminaCarta(carta.numero)}>
                        Elimina carta
                      </Button>
                    </CardHeader>
                  </Card>
                </Col>
              );
            })}
          </Row>
        </div>
        <Row>
          <Col md="12">
            <Card>
              <CardHeader className="mb-5">
                <h5 className="card-category">GCC</h5>
                <CardTitle tag="h3">Elenco delle carte collezionabili</CardTitle>
              </CardHeader>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md="12" className="mb-2">
            <Input
              type="text"
              placeholder="Cerca Pokémon"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            <Button
              style={{ marginBottom: "10px" }}
              onClick={() => setFilteredPokemonData(pokemonData)}
            >
              Cerca
            </Button>
          </Col>
        </Row>
        <Row>
          {filteredPokemonData.map((pokemon) => (
            <Col md="4" key={pokemon.numero}>
              <Card>
                <CardHeader className="mb-5">
                  <h5 className="card-category">{pokemon.stadio_evolutivo}</h5>
                  <CardTitle tag="h3">{pokemon.nome}</CardTitle>
                  <CardText>
                    <img
                      alt="..."
                      className={`pokemon_image ${
                        carteAggiunte.some((carta) => carta.numero === pokemon.numero)
                          ? "color"
                          : ""
                      }`}
                      src={pokemon.url}
                    />
                    Numero: <label>{pokemon.numero}</label> <br />
                    Abilità:{" "}
                    <label>{pokemon.abilita.join(", ")}</label> <br />
                  </CardText>
                  <Button onClick={() => aggiungiCarta(pokemon)}>
                    Aggiungi carta
                  </Button>
                </CardHeader>
              </Card>
            </Col>
          ))}
        </Row>
      </div>
    </>
  );
}

export default Gcc;
