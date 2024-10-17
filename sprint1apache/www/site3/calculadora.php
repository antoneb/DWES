<!DOCTYPE html>

<body>

    <h1>Calculadora</h1>
    <p>Realiza las operaciones indicadas</p>



    <!--
    Efectivamente carlos no lei el enunciado jajajajajaj 
    <form action="/calculadora.php" method="post">

        <label for="cantidad_input1">Primer valor:</label><br>
        <input type="text" id="cantidad_input1" name="fcantidad1"><br>
        <label for="cantidad_input2">Segundo valor:</label><br>
        <input type="text" id="cantidad_input2" name="fcantidad2"><br>

        <input type="radio" id="sumarI" name="operacion" value="sumar">
        <label for="sumarI">Sumar</label><br>

        <input type="radio" id="restarI" name="operacion" value="restar">
        <label for="restarI">Restar</label><br>

        <input type="radio" id="multI" name="operacion" value="mult">
        <label for="multI">Multiplicar</label><br>

        <input type="radio" id="divI" name="operacion" value="div">
        <label for="divI">Division</label><br>

        <input type="submit" value="Operar">
    </form>
  -->
    <form action="./calculadora.php" method="post">
        <label for="cantidad_input1">Primer valor:</label><br>
        <input type="text" id="cantidad_input1" name="fcantidad1"><br>
        <label for="cantidad_input2">Segundo valor:</label><br>
        <input type="text" id="cantidad_input2" name="fcantidad2"><br>

        <select name="operacion">
            <option value="sumar">Sumar</option>
            <option value="restar">Restar</option>
            <option value="mult">Multiplicar</option>
            <option value="div">Dividir</option>
        </select>

        <input type="submit" value="Operar" name="Operar">
    </form>

    <p> Resultado:

        <?php
        //utilizando un switch case
        if (isset($_POST["Operar"])) {
            //Podria haber utilizado directamente post pero me parecio mas legible asi
            $op = $_POST["operacion"];
            $op1 = $_POST["fcantidad1"];
            $op2 = $_POST["fcantidad2"];

            switch ($op) {
                case "sumar":
                    echo $op1 . " + " . $op2 . " = " . ($op1 + $op2);
                    break;
                case "restar":
                    echo $op1 . " - " . $op2 . " = " . ($op1 - $op2);
                    break;
                case "mult":
                    echo $op1 . " * " . $op2 . " = " . ($op1 * $op2);
                    break;
                case "div":
                    echo $op1 . " / " . $op2 . " = " . ($op1 / $op2);
                    break;
            }
        }



        //utilizando if-else y $_post
        /** 

        if (isset($_POST["operacion"])) {
            if ($_POST["operacion"] == "sumar") {
                echo $_POST["fcantidad1"] . " + " . $_POST["fcantidad2"] . " = " . $_POST["fcantidad1"] + $_POST["fcantidad2"];
            }

            if ($_POST["operacion"] == "restar") {
                echo $_POST["fcantidad1"] . " - " . $_POST["fcantidad2"] . " = " . $_POST["fcantidad1"] - $_POST["fcantidad2"];
            }

            if ($_POST["operacion"] == "mult") {
                echo $_POST["fcantidad1"] . " * " . $_POST["fcantidad2"] . " = " . $_POST["fcantidad1"] * $_POST["fcantidad2"];
            }

            if ($_POST["operacion"] == "div") {
                echo $_POST["fcantidad1"] . " / " . $_POST["fcantidad2"] . " = " . $_POST["fcantidad1"] / $_POST["fcantidad2"];
            }
        }
         */

        ?>
    </p>

</body>

</html>