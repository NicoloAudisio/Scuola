<?php
session_start();

if(isset($_POST['login'])){
    $username = $_POST['username'];
    $password = $_POST['password'];

    if($username == 'admin' && $password == 'password'){
        $_SESSION['username'] = $username;
        setcookie("login", $username, time() + 120);
        header("Location: booking.php");
        exit();
    }
}
?>

<form method="post" action="login.php">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br>
    <input type="submit" value="Login" name="login">
</form>
