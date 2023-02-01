<?php
header('Content-Type: application/json');

$server="localhost";
$usuario="root";
$clave="";
$base="productos";
$conexion=mysqli_connect($server,$usuario,$clave,$base) or die("problemas") ;
mysqli_set_charset($conexion,'utf8'); 

$datos = mysqli_query($conexion, "SELECT codigo, descripcion, precio from articulos");
$resultado = mysqli_fetch_all($datos, MYSQLI_ASSOC);
echo json_encode($resultado);        
?>