const server = require("http").createServer().listen(3009);
let products = [];
let operators = {};


const io = require('socket.io')(server, {
  cors: {
    origin: '*',
  }
});

io.on('connection', (socketClient) => {
    socketClient.on('addNickname', (nickname) => {
        operators[socketClient.id] = nickname;
        io.emit('nicknameList', Object.values(operators));
    });

    socketClient.on('addProduct', (product) => {
        product.operator = operators[socketClient.id];
        products.push(product);
        io.emit('productList', products);
    });

    socketClient.on('eliminaProdotto', (index) => {
        products.splice(index, 1);
        io.emit('productList', products);
    });

    // Funzione cerca
    // socketClient.on('searchProduct', (searchPr) => {
        
    //     const searchResults = products.filter(product => product.name.includes(searchPr));
    
    //     web_socket.emit('searchResult', searchResults);
    // });

    // lista dei prodotti e chi ha svolto l'azione
    socketClient.emit('productList', products);
    socketClient.emit('nicknameList', Object.values(operators));
});

