<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
session_start();
?>
<html>

<body>
    <?php

    $user_id_a_insertar = 'NULL';
    if (!empty($_SESSION['user_id'])) {
        $user_id_a_insertar = $_SESSION['user_id'];
    }
    $libro_id = $_POST['libro_id'];
    $comentario = $_POST['new_comment'];
    $fechaPost = time();
    $query = "INSERT INTO tComentarios(comentario, fechaPost, libro_id, usuario_id)
VALUES ('" . $comentario . "',CURRENT_TIMESTAMP," . $libro_id . "," . $user_id_a_insertar . ")";
    mysqli_query($db, $query) or die('Error');
    echo "<p>Nuevo comentario ";
    echo mysqli_insert_id($db);
    echo " añadido</p>";
    echo "<a href='/detail.php?libro_id=" . $libro_id . "'>Volver</a>";
    mysqli_close($db);
    ?>
</body>

</html>