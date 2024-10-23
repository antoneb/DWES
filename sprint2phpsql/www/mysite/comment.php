<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
?>
<html>

<body>
    <?php
    $libro_id = $_POST['libro_id'];
    $comentario = $_POST['new_comment'];
    $fechaPost = time();
    $query = "INSERT INTO tComentarios(comentario, fechaPost, libro_id, usuario_id)
VALUES ('" . $comentario . "',CURRENT_TIMESTAMP," . $libro_id . ",NULL)";
    mysqli_query($db, $query) or die('Error');
    echo "<p>Nuevo comentario ";
    echo mysqli_insert_id($db);
    echo " añadido</p>";
    echo "<a href='/detail.php?libro_id=" . $libro_id . "'>Volver</a>";
    mysqli_close($db);
    ?>
</body>

</html>