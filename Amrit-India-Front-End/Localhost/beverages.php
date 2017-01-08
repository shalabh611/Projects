<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'buffet_sample')){
	echo "Database not selected";
}

$Name=$_POST['beverages1'];
$Name1=$_POST['beverages2'];
$Name2=$_POST['beverages3'];

$sql = "INSERT INTO beverages(b1,b2,b3) VALUES ('$Name','$Name1','$Name2')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
?>