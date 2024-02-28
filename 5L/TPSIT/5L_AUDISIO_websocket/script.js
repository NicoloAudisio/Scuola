let web_socket;

// Funzione connessione al server con stampa console log
function connectToServer() {
    const serverAddress = document.getElementById('serverAddress').value;
    const operatorNickname = document.getElementById('operatorNickname').value;

    if (serverAddress === "" || operatorNickname === "") {
        alert("Assicurati di inserire l'indirizzo IP e il tuo nickname.");
        return;
    }


    web_socket = io.connect(`${serverAddress}`);
    web_socket.on('connect', () => {
        console.log('Connesso al server');
        document.getElementById('productForm').style.display = 'block';
    });

    web_socket.on('productList', (products) => {
        prodotti(products);
    });

    web_socket.on('nicknameList', (operators) => {
        accessi(operators);
    });

    web_socket.emit('addNickname', operatorNickname);
    showPopup("Connessione avvenuta con successo!");
}

// funzione aggiungi prodotto
function addProduct() {
    const productName = document.getElementById('productName').value;
    const productDescription = document.getElementById('productDescription').value;
    const productQt = document.getElementById('productQt').value;
    const productPosition = document.getElementById('productPosition').value;
    const productPrice = document.getElementById('productPrice').value;

    const product = {
        name: productName,
        description: productDescription,
        qt: productQt,
        position: productPosition,
        price: productPrice,
    };

    web_socket.emit('addProduct', product);
    showPopup("Prodotto aggiunto con successo!");
}

// funzione stampa prodotti
function prodotti(products) {
    const productList = document.getElementById('products');
    productList.innerHTML = '';

    products.forEach((product, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>Nome: ${product.name}<br/>Descrizione: ${product.description}<br/>Quantità: ${product.qt}<br/>Prezzo: ${product.price}€<br/>Posizione: ${product.position}<br/>Operatore: ${product.operator}<br/></span>
            <button onclick="eliminaProdotto(${index})">Elimina</button>
        `;
        productList.appendChild(listItem);
    });
}

// funzione elimina prodotto
function eliminaProdotto(index) {
    web_socket.emit('eliminaProdotto', index);
    showPopup("Prodotto eliminato con successo!");
}

// funzione stampa accessi
function accessi(operators) {
    const operatorList = document.getElementById('operators');
    operatorList.innerHTML = '';

    operators.forEach(operator => {
        const listItem = document.createElement('li');
        listItem.textContent = operator;
        operatorList.appendChild(listItem);
    });
}

// funzione mostra pop-up
function showPopup(message) {
    const popup = document.createElement('div');
    popup.className = 'popup';
    popup.textContent = message;
    document.body.appendChild(popup);

    setTimeout(() => {
        popup.remove();
    }, 3000); // Il pop-up scompare dopo 3 secondi
}

// funzione ricerca e stampa prodotto
// function searchAndPrintProduct(searchPr) {
//     const searchPr = document.getElementById('search').value;

//     if (searchPr === "") {
//         alert("Inserisci il nome del prodotto da cercare.");
//         return;
//     } else {
//         console.log("hai inserito un prodotto");
//     }

//     web_socket.emit('searchProduct', searchPr);

//     web_socket.on('searchProduct', (products) => {
//         prodotti(products);
//     });
// }
