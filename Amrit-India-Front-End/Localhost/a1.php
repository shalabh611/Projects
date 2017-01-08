<? php

DEFINE ('DB_USER','admin');
DEFINE ('DB_PSWD','amrit');
DEFINE ('DB_HOST','http://localhost/phpmyadmin/db_structure.php?server=1&db=final&token=2d4a1bd0f5d42485dfcee22504f4d585');
DEFINE ('DB_NAME','final');

$dbcon=mysqli_connect(DB_HOST,DB_USER,DB_PSWD,DB_NAME);

?>