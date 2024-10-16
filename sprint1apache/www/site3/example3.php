<html>

<body>
    <h1>Jubilación</h1>
    <?php
    $edadP = $_GET["edad"];

    function edad_en_10_años($edadP)
    {
        return $edadP + 10;
    }
    if (edad_en_10_años($edadP) > 65) {
        echo "En 10 años tendrás edad de jubilación";
    } else {
        echo "¡Disfruta de tu tiempo!";
    }
    ?>
</body>

</html>