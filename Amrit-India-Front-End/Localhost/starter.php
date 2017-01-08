<?php
$con=mysqli_connect('127.0.0.1','root','');
if(!$con){
	echo "Not Connected";
}
if(!mysqli_select_db($con,'buffet_sample')){
	echo "Database not selected";
}


$Name=$_POST['starter1'];
$Name1=$_POST['starter2'];
$Name2=$_POST['starter3'];

$del="DELETE FROM STARTER";
$records1=mysql_query($del);

$sql = "INSERT INTO starter(s1,s2,s3) VALUES ('$Name','$Name1','$Name2')";

if(!mysqli_query($con,$sql)){
	echo "Not inserted";
}
else{
	echo "Inserted";
}

?>