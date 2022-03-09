<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>time table generator</title>
</head>
<body>
    <form>
    start: <input type="text" name="start" id="start">
    time: <input type="number" name="time" id="time">
    stop: <input type="text" name="stop" id="stop">
    </form>
</body>
</html>
<?php
    $start = $_GET['start'];
    $time = $_GET['time'];
    $stop = $_GET['stop'];
    $start = strtotime($start);
    $stop = strtotime($stop);
    $time = $time * 60; 
    echo "$start<br>";