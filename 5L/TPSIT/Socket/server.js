var net = require('net');

var client = new net.Socket();
client.connect(4000, "127.0.0.1", function() {
    console.log('Connesso al server');
});

client.on('data', function(data) {
    var chat = document.getElementById('chat');
    chat.innerHTML += 'Ricevuto: ' + data + '<br />';
});

client.on('close', function() {
    console.log('Connessione chiusa');
});

function sendMessage() {
    var message = document.getElementById('message').value;
    client.write(message);
    document.getElementById('message').value = '';
}
