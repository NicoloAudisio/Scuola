const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

let punteggi = {};

app.get('/', (req, res) => {
    res.render('form');
});

app.post('/punteggi', (req, res) => {
    let gioco = req.body.gioco;
    let punteggio = parseInt(req.body.punteggio);
    if (punteggi[gioco]) {
        punteggi[gioco] = Math.max(punteggi[gioco], punteggio);
    } else {
        punteggi[gioco] = punteggio;
    }
    res.redirect('/');
});

app.get('/riepilogo', (req, res) => {
    let maxPunteggio = 0;
    let maxGioco = '';
    for (let gioco in punteggi) {
        if (punteggi[gioco] > maxPunteggio) {
            maxPunteggio = punteggi[gioco];
            maxGioco = gioco;
        }
    }
    res.render('riepilogo', { punteggi: punteggi, maxGioco: maxGioco, maxPunteggio: maxPunteggio });
});

app.listen(3000, () => {
    console.log('Server in ascolto sulla porta 3000');
});
