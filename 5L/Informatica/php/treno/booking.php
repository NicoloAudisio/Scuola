<?php
session_start();

if(!isset($_COOKIE['login'])){
    header("Location: login.php");
    exit();
}

if(isset($_POST['logout'])){
    session_destroy();
    setcookie("login", "", time() - 60);
    header("Location: login.php");
    exit();
}

if(isset($_POST['calculate'])){
    $base_price = $_POST['base_price'];
    $train_type = $_POST['train_type'];
    $surcharge = 0;

    switch($train_type){
        case 'Freccia rossa seconda classe':
            $surcharge = 0.07;
            break;
        case 'Freccia rossa prima classe':
            $surcharge = 0.12;
            break;
        case 'Freccia rossa premium':
            $surcharge = 0.18;
            break;
    }

    $total_price = $base_price + ($base_price * $surcharge);
    echo "Il prezzo totale del biglietto è di " . $total_price . " euro e il treno utilizzato è il " . $train_type;
}
?>

<form method="post" action="booking.php">
    <label for="base_price">Prezzo base:</label><br>
    <input type="text" id="base_price" name="base_price"><br>
    <label for="train_type">Tipo di treno:</label><br>
    <select id="train_type" name="train_type">
        <option value="Freccia rossa seconda classe">Freccia rossa seconda classe</option>
        <option value="Freccia rossa prima classe">Freccia rossa prima classe</option>
        <option value="Freccia rossa premium">Freccia rossa premium</option>
    </select><br>
    <input type="submit" value="Calcola" name="calculate">
    <input type="submit" value="Logout" name="logout">
</form>
