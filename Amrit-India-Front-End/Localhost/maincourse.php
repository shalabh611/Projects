<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'buffet_sample')){
	echo "Database not selected";
}

$Name=$_POST['maincourse1'];
$Name1=$_POST['maincourse2'];
$Name2=$_POST['maincourse3'];
$Name3=$_POST['maincourse4'];

$sql = "INSERT INTO maincourse(m1,m2,m3,m4) VALUES ('$Name','$Name1','$Name2','$Name3')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
?>