<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'feedback')){
	echo "Database not selected";
}

$Name=$_POST['userName'];
$Email=$_POST['userEmail'];
$Mobile=$_POST['userPhone'];
$Message=$_POST['userMsg'];

$sql = "INSERT INTO feed(name,email,phone,msg) VALUES ('$Name','$Email','$Mobile','$Message')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}
?>