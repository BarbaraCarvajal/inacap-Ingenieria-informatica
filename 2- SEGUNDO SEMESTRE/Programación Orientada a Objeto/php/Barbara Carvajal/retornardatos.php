<?php
    header('Content-type: application/json');

    $server = "localhost";
    $usuario = "root";
    $clave = "";
    $base="articulos";
    $conexion = mysqli_connect($server, $usuario,$clave,$base) or die ("probelmas de conexion");
    mysqli_set_charset($conexion, 'utf8');

    $datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos");
    $resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
    echo json_encode($resultado);
?>