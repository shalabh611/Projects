<?php

mysql_connect('localhost','root','');

mysql_select_db('final1');

$sql="SELECT * FROM lodging_reservation";

$records=mysql_query($sql);
?>

<html>
<head>
  <title>Amrit India</title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link href="css/style.css" rel="stylesheet" type="text/css"  media="all" />
  <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
 </head>
  <body>
	<!----start-header----->
	 <div class="header">
	     <div class="wrap">
			<div class="top-header">
				<div class="logo">
					<!--a href="index.html"><img src="images/logo.png" title="logo" /></a-->
					<p><figure class="f1"><a href="home.html"><img src="images/amrit-india.png" alt="Amrit India" title="logo " /></figure>
					</p>
				</div>
                <div>
                    <h1 class="TitleOFAI">AMRIT INDIA</h1>
                </div>
				<div class="social-icons">
					<ul>
						<li><a href="https://www.facebook.com/Amrit-India-349896811838177/?fref=ts"><img src="images/facebook.png" title="facebook" /></a></li>
						<li><a href="#"><img src="images/twitter.png" title="twitter" /></a></li>
						<li><a href="#"><img src="images/google.png" title="google pluse" /></a></li>
					</ul>
				</div>
				<div class="clear"> </div>
			</div>
			<!---start-top-nav---->
			<div class="top-nav">
				<div class="top-nav-left">
					<ul>
						<li><a href="home.html">Home</a></li>
						<li><a href="about.html">About</a></li>
						<li><a href="gallery.html">Gallery</a></li>
						<li><a href="menu.html">Menu</a></li>
						<li><a href="">Reservation<img src="images/arrow-down-small-16.png" /></a>
                            <ul class="dropdown">
                                <li class="update"><a class="format" href="Dining_Reservation.html">Dining</a></li>
                                <li class="update"><a class="format" href="Lodging_Reservation.html">Lodging</a></li>
                                
                            </ul>
                        </li>
						<li><a href="Lodging.html">Lodging</a></li>
						<li class="active"><a href="contact.html">Contact Us</a></li>
						<div class="clear"> </div>
					</ul>
				</div>
				<div class="top-nav-right">
					<form>
						<input type="text"><input type="submit" value="" />
					</form>
				</div>
				<div class="clear"> </div>
			</div>
			<!---End-top-nav---->
		</div>
	</div>
   <!----End-header----->
		 <!---start-content---->
		 <div class="content">
		 	<!---start-contact---->
		 	<div class="contact">
		 		<div class="wrap">
				<div class="section group">				
							
				<div class="col span_2_of_3">
				  <div class="contact-form">
				  	<h3>Dining Table</h3>

<table width="600" border="1" cellpadding="1" cellspacing="1">
<tr>
<th>Name</th>
<th>Email</th>
<th>Single</th>
<th>Double</th>
<th>Time</th>
<th>Phone</th>
<th>Msg</th>
<tr>

<?php

while($result=mysql_fetch_assoc($records)){
echo "<tr>";

echo "<td>".$result['name']."</td>";

echo "<td>".$result['email']."</td>";

echo "<td>".$result['single']."</td>";

echo "<td>".$result['doubl']."</td>";

echo "<td>".$result['time']."</td>";

echo "<td>".$result['phone']."</td>";

echo "<td>".$result['msg']."</td>";

echo "</tr>";
}

?>
</table> </div>
  				</div>				
			  </div>
			</div>
			</div>
		 	<!---End-contact---->
		 <!---End-content---->
		 
	</body>
</html>
