<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'buffet_sample')){
	echo "Database not selected";
}

$Name=$_POST['dessert1'];
$Name1=$_POST['dessert2'];
$Name2=$_POST['dessert3'];

$sql = "INSERT INTO desserts(d1,d2,d3) VALUES ('$Name','$Name1','$Name2')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
?>