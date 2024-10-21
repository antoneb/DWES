<?php
$db = mysqli_connect('localhost', 'root', '1234', 'dbLibrosAnton') or die('Fail');
?>
<html>

<body>
    <?php
    if (!isset($_GET['libro_id'])) {
        die('No se ha especificado un libro');
    }

    $libro_id = $_GET['libro_id'];
    $query = 'SELECT * FROM tLibros WHERE id=' . $libro_id;
    $result = mysqli_query($db, $query) or die('Query error');
    $only_row = mysqli_fetch_array($result);
    echo '<h1>' . $only_row['titulo'] . '</h1>';
    ?>
    
    <img src="<?php echo $only_row[2] ?>" alt="portada" width="300" height="450">

    <?php
    echo '<h2>' . $only_row['anho'] . '</h2>';
    ?>

    <h3>Comentarios:</h3>
    <ul>
        <?php
        $query2 = 'SELECT * FROM tComentarios WHERE libro_id=' . $libro_id;
        $result2 = mysqli_query($db, $query2) or die('Query error');

        while ($row = mysqli_fetch_array($result2)) {
            echo '<li>' . $row['comentario'] . '</li>';
        }

        mysqli_close($db);
        ?>
    </ul>
    <p>Deja un nuevo comentario:</p>
    <form action="/comment.php" method="post">
        <textarea rows="4" cols="50" name="new_comment"></textarea><br>
        <input type="hidden" name="libro_id" value="<?php echo $libro_id; ?>">
        <input type="submit" value="Comentar">
    </form>
</body>

</html>