// array salvataggio
let dataArr = [];

// funzione aggiunta data
function addData(query) {
    let weatherData = {
        city: query.city,
        maxTemp: query.max,
        minTemp: query.min,
        date: new Date()
    };

    // push dati
    dataArr.push(weatherData);
}

// funzione stampa tabella
function getTable() {
    let table = '<table style="width:100%;border:1px solid black;font-family: Arial, sans-serif;background-color: #f4f4f4;color: #333;"><tr><th>Citta</th><th>Max Temp</th><th>Min Temp</th><th>Data</th></tr>';
    dataArr.forEach(item => {
        table += `<tr><td>${item.city}</td><td>${item.maxTemp}</td><td>${item.minTemp}</td><td>${item.date}</td></tr>`;
    });
    table += '</table>';
    table += '<button style="background-color: #2ecc71;color: #fff;border: none;border-radius: 5px;padding: 10px 20px;cursor: pointer;margin-top: 20px;display: block;" onclick="window.location.href=\'http://127.0.0.1:3000/\';">Ritorno all\'inserimento</button>';
    return table;
}

// esportazione
module.exports = { addData, getTable };
