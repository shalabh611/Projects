<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'final')){
	echo "Database not selected";
}

$Name=$_POST['name'];
$Email=$_POST['email'];
$People=$_POST['numpeople'];
$Time=$_POST['time'];
$Contact=$_POST['contact'];
$Message=$_POST['userMsg'];

$sql = "INSERT INTO dining_reservation(name,email,people,time,phone,msg) VALUES ('$Name','$Email','$People','$Time','$Contact','$Message')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
header('Location: confirm.html');
?>