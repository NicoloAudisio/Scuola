<?php
session_start();

$utenti = array(
    "nicolo" => "1234",
    "marco" => "5678",
    "anna" => "9012",
    "martina" => "3456"
);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $colore = $_POST["colore"];

    if (array_key_exists($username, $utenti) && $utenti[$username] == $password) {
        $_SESSION["username"] = $username;
        $_SESSION["colore"] = $colore;
        header("Location: benvenuto.php");
    } else {
        echo "Username o password non validi.";
    }
}
?>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    Colore preferito: <input type="text" name="colore"><br>
    <input type="submit">
</form>
