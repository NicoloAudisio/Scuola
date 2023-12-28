// Importa i moduli necessari
const express = require('express');
const app = express();

// Imposta EJS come motore di rendering
app.set('view engine', 'ejs');

// Utilizza bodyParser per analizzare i dati del form
app.use(bodyParser.urlencoded({ extended: true }));

// Crea un oggetto per memorizzare i punteggi
let punteggi = {};

// Rotta per il form
app.get('/', (req, res) => {
    res.render('form');
});

// Rotta per gestire l'invio del form
app.post('/punteggio', (req, res) => {
    let gioco = req.body.gioco;
    let punteggio = parseInt(req.body.punteggio);

    // Se il gioco esiste già, aggiorna il punteggio se è più alto
    if (gioco in punteggi) {
        if (punteggio > punteggi[gioco]) {
            punteggi[gioco] = punteggio;
        }
    } else {
        // Altrimenti, aggiungi il gioco e il punteggio
        punteggi[gioco] = punteggio;
    }

    res.redirect('/riepilogo');
});

// Rotta per la pagina di riepilogo
app.get('/riepilogo', (req, res) => {
    let massimoPunteggio = Math.max(...Object.values(punteggi));
    let giocoConPunteggioMassimo = Object.keys(punteggi).find(key => punteggi[key] === massimoPunteggio);

    res.render('riepilogo', { punteggi: punteggi, massimoPunteggio: massimoPunteggio, giocoConPunteggioMassimo: giocoConPunteggioMassimo });
});

// Avvia il server
app.listen(3000, () => {
    console.log('Server in ascolto sulla porta 3000');
});