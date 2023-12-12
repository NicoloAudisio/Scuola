<?php
session_start();

$giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"];
$fasce = ["9-11", "11-13", "14-16", "16-18"];

if (isset($_SESSION["partecipanti"])) {
    $conteggio = array();
    foreach ($_SESSION["partecipanti"] as $nome => $disponibilita) {
        foreach ($disponibilita as $opzione) {
            if (!array_key_exists($opzione, $conteggio)) {
                $conteggio[$opzione] = 0;
            }
            $conteggio[$opzione]++;
        }
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
            }
            h2 {
                color: #333;
                margin-left: 20px;
            }
            table {
                width: 90%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 15px;
                text-align: center;
            }
            th {
                background-color: #4CAF50;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            input[type=button] {
                display: block;
                width: 200px;
                height: 50px;
                margin: 20px auto;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
            }
            input[type=button]:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>

    <h2>Disponibilità:</h2>
    <table>
        <tr>
            <th>Nome</th>
            <th>Disponibilità</th>
        </tr>
        <?php
        foreach ($_SESSION["partecipanti"] as $nome => $disponibilita) {
            echo "<tr>";
            echo "<td>" . $nome . "</td>";
            echo "<td>";
            sort($disponibilita);
            foreach ($disponibilita as $opzione) {
                echo $opzione . "<br>";
            }
            echo "</td>";
            echo "</tr>";
        }
        ?>
    </table>

    <h2>Numero di persone disponibili per ogni fascia oraria:</h2>
    <table>
        <tr>
            <th>Fascia Oraria</th>
            <th>Numero di Persone</th>
        </tr>
        <?php
        foreach ($giorni as $giorno) {
            foreach ($fasce as $fascia) {
                $opzione = $giorno . "-" . $fascia;
                if (array_key_exists($opzione, $conteggio)) {
                    echo "<tr>";
                    echo "<td>" . $opzione . "</td>";
                    echo "<td>" . $conteggio[$opzione] . "</td>";
                    echo "</tr>";
                }
            }
        }
        ?>
    </table>

    <input type="button" value="Inserisci orari" onclick="window.location.href='index.php'" />

    </body>
</html>