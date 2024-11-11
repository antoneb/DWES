<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
$query = 'SELECT id,titulo, imagen, autor, genero, anho FROM tLibros';
$result = mysqli_query($db, $query) or die('Query error');
?>

<html>

<head>
    <link rel="stylesheet" href="estilos.css">
</head>

<body>
    <h1>Conexion establecida</h1>
    <h3> <a href="./login.php">Login</a> <a href="./register.php">Registro</a> </h3>
    <h3><a href="./logout.php">Cerrar sesion</a></h3>
    <table>
        <tr>
            <th>Portada</th>
            <th>Titulo</th>
            <th>Autor</th>
            <th>Genero</th>
            <th>Año</th>
        </tr>

        <?php
        while ($row = mysqli_fetch_array($result)) {
        ?>
            <tr>
                <td><a href="detail.php?libro_id=<?php echo $row[0] ?>"> <img src="<?php echo $row[2] ?>" alt="portada"></img></a></td>
                <td><?php echo $row[1]; ?></td>
                <td><?php echo $row[3]; ?></td>
                <td><?php echo $row[4]; ?></td>
                <td><?php echo $row[5]; ?></td>
            </tr>

        <?php
        }
        mysqli_close($db);
        ?>


    </table>
</body>

</html>