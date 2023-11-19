<?php
session_start();

if (!isset($_SESSION["username"])) {
    header("Location: index.php");
}

echo "Ciao " . $_SESSION["username"] . ", sei nella home page. Il tuo colore preferito è " . $_SESSION["colore"] . ".<br>";
echo "<a href='logout.php'>Logout</a>";