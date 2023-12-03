// import fs
let fs = require("fs");

// creazione funzione fs
function readHTMLFile(path) {
    return fs.readFileSync(path);
}

// esportazione fs
module.exports = { readHTMLFile };
