<?php

mysql_connect('localhost','root','');

mysql_select_db('feedback');

$sql="SELECT * FROM feed";

$records=mysql_query($sql);
?>

<html>
<head>
<title>Reservation details</title>
</head>
<body>
<table width="600" border="1" cellpadding="1" cellspacing="1">
<tr>
<th>Name</th>
<th>Email</th>
<th>Phone</th>
<th>Msg</th>
<tr>

<?php

while($result=mysql_fetch_assoc($records)){
echo "<tr>";

echo "<td>".$result['name']."</td>";

echo "<td>".$result['email']."</td>";

echo "<td>".$result['phone']."</td>";

echo "<td>".$result['msg']."</td>";

echo "</tr>";
}

?>
</table>
<form action="table_links.html">
<input type="submit" value="Back" 
         name="Submit" id="frm1_submit" />
</form>

</body>
</html>
