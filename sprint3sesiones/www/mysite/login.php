<html>

<head>
    <meta charset="UTF-8">
</head>
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
/**
 * Usuario ejemplo para Login:
 * email:  anton@anton.com
 * pass: 123
 * **************************
 * WARNING: 
 * No se puede iniciar sesion en los usuarios creados en la tarea anterior
 * debido a que su contraseña es 123 (en la DB) y el login solo se
 * puede hacer con contraseñas seguras (hasheadas)
 */

?>
<script></script>

<body>
    <h3><a href="./logout.php">Logout</a></h3>
    <h1>Login</h1>
    <form name="loginForm" action="login.php" onsubmit="return validateForm()" method="post">
        <input name="f_email" type="text" placeholder="e-mail"><br>
        <input name="f_password" type="password" placeholder="Contraseña"><br>
        <input type="submit" value="Iniciar sesión">
    </form>

    <h1>Cambiar contraseña</h1>
    <form name="cambiarPass" action="login.php" onsubmit="return validateFormPass()" method="post">
        <input name="f_email" type="text" placeholder="e-mail"><br>
        <input name="f_password" type="password" placeholder="Contraseña antigua"><br>
        <input name="f_passwordNueva" type="password" placeholder="Contraseña nueva"><br>
        <input type="submit" value="Cambiar">
    </form>
</body>
<?php

if (!$_POST['f_email'] || !$_POST['f_password']) {
    echo "<p>Por favor completa todos los campos</p>";
} else {
    $email_posted = $_POST['f_email'];
    $password_posted = $_POST['f_password'];
    $password_nueva = $_POST['f_passwordNueva'];

    $query = "SELECT id, pass FROM tUsuarios WHERE email = '" . $email_posted . "'";
    $result = mysqli_query($db, $query) or die('Query error');

    if (mysqli_num_rows($result) > 0) {
        $only_row = mysqli_fetch_array($result);

        if (password_verify($password_posted, $only_row[1]) && $_POST["f_passwordNueva"]) {
            $query = "UPDATE tUsuarios SET pass='" . password_hash($password_nueva, PASSWORD_DEFAULT)  . "' WHERE email=" . "'" . $email_posted . "'" . ";";
            echo $query;
            mysqli_query($db, $query) or die('Query error');
            session_start();
            $_SESSION['user_id'] = $only_row[0];
        } else if (password_verify($password_posted, $only_row[1])) {
            echo "<p>Usuario autenticado</p>";
            session_start();
            header('Location: main.php');
            $_SESSION['user_id'] = $only_row[0];
        } else {
            echo '<p>Contraseña incorrecta</p>';
        }
    } else {
        echo '<p>Usuario no encontrado con ese email</p>';
    }
}

?>
<script>
    function validateForm() {
        let x = document.forms["loginForm"]["f_email"].value;
        if (x == "") {
            alert("Campo mail vacio");
            return false;
        }
        let y = document.forms["loginForm"]["f_password"].value;
        if (y == "") {
            alert("Campo contraseña vacio");
            return false;
        }
    }

    function validateFormPass() {
        let x = document.forms["cambiarPass"]["f_email"].value;
        if (x == "") {
            alert("Campo mail vacio");
            return false;
        }
        let y = document.forms["cambiarPass"]["f_password"].value;
        if (y == "") {
            alert("Campo contraseña vacio");
            return false;
        }
    }
</script>

</html>