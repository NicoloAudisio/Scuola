const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  const buttonValue = req.query.button;
  console.log(`Pulsante premuto: ${buttonValue}`);
  // Qui puoi aggiungere il codice per inviare il valore del pulsante all'Arduino.
  res.send('Pulsante premuto ricevuto!');
});

app.listen(port, () => {
  console.log(`Server in ascolto su http://localhost:${port}`);
});
