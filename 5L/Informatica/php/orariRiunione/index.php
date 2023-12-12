<?php
session_start();

$giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"];
$fasce = ["9-11", "11-13", "14-16", "16-18"];

$errore = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST["nome"];
    $giorno = $_POST["giorno"];
    $fascia = $_POST["fascia"];

    if (empty($giorno) || empty($fascia)) {
        $errore = "Per favore, inserisci sia il giorno, il nome che la fascia oraria.";
    } else {
        if (!isset($_SESSION["partecipanti"])) {
            $_SESSION["partecipanti"] = array();
        }

        if (!array_key_exists($nome, $_SESSION["partecipanti"])) {
            $_SESSION["partecipanti"][$nome] = array();
        }

        $_SESSION["partecipanti"][$nome][] = $giorno . "-" . $fascia;
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            display: flex;
            justify-content: space-around;
        }
        .agency {
            width: 40%;
            text-align: center;
            padding-top: 50px;
        }
        form {
            width: 40%;
            margin: 20px auto;
        }
        label {
            display: block;
            margin-top: 20px;
        }
        input[type=text], select {
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type=submit], input[type=button] {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type=submit]:hover, input[type=button]:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
        }
    </style>
</head>
    <body>

    <div class="agency">
        <h1>Nik's Agency</h1>
    </div>

    <form method="post" action="index.php">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required>
        <label for="giorno">Giorno:</label>
        <select id="giorno" name="giorno">
            <option value="" selected disabled hidden>Seleziona un giorno</option>
            <?php foreach ($giorni as $giorno) { echo "<option value='" . $giorno . "'>" . $giorno . "</option>"; } ?>
        </select>
        <label for="fascia">Fascia oraria:</label>
        <select id="fascia" name="fascia">
            <option value="" selected disabled hidden>Seleziona una fascia oraria</option>
            <?php foreach ($fasce as $fascia) { echo "<option value='" . $fascia . "'>" . $fascia . "</option>"; } ?>
        </select>
        <input type="submit" value="Invia">
        <input type="button" value="Visualizza tabelle" onclick="window.location.href='tabella.php'" />
    </form>

    <?php
    if (!empty($errore)) {
        echo "<p class='error'>" . $errore . "</p>";
    }
    ?>

    </body>
</html>
