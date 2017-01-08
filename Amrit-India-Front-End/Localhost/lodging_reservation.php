<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'final1')){
	echo "Database not selected";
}

$Name=$_POST['name'];
$Email=$_POST['email'];
$Single=$_POST['numofsingle'];
$Doubl=$_POST['numofdouble'];
$Time=$_POST['time'];
$Contact=$_POST['contact'];
$Message=$_POST['userMsg'];

$sql = "INSERT INTO lodging_reservation(name,email,single,doubl,time,phone,msg) VALUES ('$Name','$Email','$Single','$Doubl','$Time','$Contact','$Message')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
header('Location: confirm.html');
?>