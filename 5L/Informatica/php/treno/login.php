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

<!DOCTYPE html>
<html lang="it">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <title>TrenITIS</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/css/templatemo-plot-listing.css">
    <link rel="stylesheet" href="assets/css/animated.css">
    <link rel="stylesheet" href="assets/css/owl.css">
  </head>

  <style>
    .login{
        width: 100%;
        height: 100%;
        background-color: #8d99af;
        border: none;
        font-size: 15px;
        border-top-right-radius: 7px;
        border-bottom-right-radius: 7px;
        color: white;
    }
  </style>

<body>

  <!-- ***** Preloader Start ***** -->
  <div id="js-preloader" class="js-preloader">
    <div class="preloader-inner">
      <span class="dot"></span>
      <div class="dots">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </div>
  <!-- ***** Preloader End ***** -->

  <div class="main-banner">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="top-text header-text">
            <h2>Accedi</h2>
          </div>
        </div>
        <div class="col-lg-12">
          <form id="search-form" method="post" action="login.php">
            <div class="row">
              <div class="col-lg-4 align-self-center">
                  <fieldset>
                      <input type="text" name="username" class="searchText" placeholder="Username" autocomplete="on" required>
                  </fieldset>
              </div>
              <div class="col-lg-4 align-self-center">
                <fieldset>
                    <input type="password" name="password" class="searchText" placeholder="Password" autocomplete="on" required>
                </fieldset>
            </div>
              <div class="col-lg-4">                        
                  <fieldset class="login">
                    <input type="submit" style="margin-top:50px; color:white" class="login" value="Login" name="login">
                  </fieldset>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="sub-footer">
            <p>Copyright © 2023 Audisio Nicolò</p>
          </div>
        </div>
      </div>
    </div>
  </footer>


  <!-- Scripts -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/js/owl-carousel.js"></script>
  <script src="assets/js/animation.js"></script>
  <script src="assets/js/imagesloaded.js"></script>
  <script src="assets/js/custom.js"></script>

</body>

</html>
