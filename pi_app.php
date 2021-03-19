<?php
    $arg = file_get_contents('php://input');
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    $output = shell_exec("./model.py {$arg}");
    echo($output);
    echo($arg);
?>
