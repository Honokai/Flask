<?php 
if($_POST!=null)
    $usuario = $_POST['user'];
    $senha = $_POST['pass'];
    $conection = mysqli_connect('127.0.0.1', $usuario, $senha,'site');
if(!($conection))
    echo(mysqli_error($conection));
?>

<!DOCTYPE html>  
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    Great
</body>
</html>
