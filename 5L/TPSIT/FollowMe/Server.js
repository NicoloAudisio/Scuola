const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
  const path = url.parse(req.url, true).pathname;

  if (path === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Pagina di test');
  } else if (path === '/getDirections') {
    // Qui dovresti implementare la logica per gestire le direzioni.
    // Potrebbe essere necessario leggere da un file JSON o da un database.
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ message: 'getDirections endpoint' }));
  } else if (path === '/showAll') {
    // Qui dovresti implementare la logica per mostrare tutte le informazioni richieste.
    // Potrebbe essere necessario leggere da un file JSON o da un database.
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ message: 'showAll endpoint' }));
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

const port = 3000;
server.listen(port, () => {
  console.log(`Server in ascolto alla porta ${port}`);
});
