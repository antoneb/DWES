<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
</head>
<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
?>


<body>
    <h1>Registro</h1>
    <form action="register.php" method="post">
        <input name="f_email" type="text" placeholder="email"><br>
        <input name="f_password" type="password" placeholder="contraseña"><br>
        <input name="f_password_check" type="password" placeholder="confirmar contraseña"><br>
        <input type="submit" value="Registrar usuario"><br>
    </form>
</body>

<?php
if (!$_POST['f_email'] || !$_POST['f_password'] || !$_POST['f_password_check']) {
    echo "<p>Por favor completa todos los campos</p>";
} else if ($_POST['f_password'] != $_POST['f_password_check']) {
    echo "<p>No coinciden las contraseñas</p>";
} else {
    //Obtener los valores del form
    $email_posted = $_POST['f_email'];
    $password_posted = $_POST['f_password'];
    $password_check = $_POST['f_password_check'];

    //Genera un username a partir del correo
    $username = substr($email_posted, 0, 5);

    //Busca usuarios con el mismo email que el posteado
    $query = "SELECT id FROM tUsuarios WHERE email = '" . $email_posted . "'";
    $result = mysqli_query($db, $query) or die('Query error');


    if (mysqli_num_rows($result) > 0) {
        // if rows > 0 --> existe usuario con ese email
        echo "<p>Ese usuario ya está registrado</p>";
    } else {
        //No existe usuario --> encriptamos contraseña y añadimos a DB
        $password_hashed = password_hash($password_posted, PASSWORD_DEFAULT);
        $password_hashed = substr($password_hashed, 0, 199);
        $query = "INSERT INTO tUsuarios (nombre, apell,email,pass) VALUES (" . "'" . $username . "'" . ",NULL," . "'" . $email_posted . "'" . ",'" . $password_hashed . "');";
        mysqli_query($db, $query) or die('Query error');
        echo "<p>Usuario registrado correctamente</p>";
    }
}
?>

</html>