<?php

mysql_connect('localhost','root','');

mysql_select_db('buffet_sample');

$sql="SELECT * FROM maincourse";

$maincourse=mysql_query($sql);
?>

<?php

mysql_connect('localhost','root','');

mysql_select_db('buffet_sample');

$sql="SELECT * FROM starter";

$starter=mysql_query($sql);
?>
<?php

mysql_connect('localhost','root','');

mysql_select_db('buffet_sample');

$sql="SELECT * FROM beverages";

$beverages=mysql_query($sql);
?>

<?php

mysql_connect('localhost','root','');

mysql_select_db('buffet_sample');

$sql="SELECT * FROM desserts";

$desserts=mysql_query($sql);
?>
<!DOCTYPE HTML>
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
						<li  class="active"><a href="menu.html">Menu</a></li>
						<li><a href="">Reservation<img src="images/arrow-down-small-16.png" /></a>
                            <ul class="dropdown">
                                <li class="update"><a class="format" href="Dining_Reservation.html">Dining</a></li>
                                <li class="update"><a class="format" href="Lodging_Reservation.html">Lodging</a></li>
                                
                            </ul>
                        </li>
						<li><a href="Lodging.html">Lodging</a></li>
						<li><a href="contact.html">Contact Us</a></li>
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
		 	<!---start-services---->
		 	<div class="services">
		 		<div class="wrap">
					<div class="services-header">
						<h3>Services</h3><br/>
						<p>This is our buffet menu for the day</p>
						<div class="clear"> </div>
					</div>
					<div class="services-grids">
						<div class="services-grid">
							<a href="#">Starters</a>
							
                            
                            <ul>
<?php

while($result=mysql_fetch_assoc($starter)){


echo "<li>".$result['s1']."</li><br/>";
echo "<li>".$result['s2']."</li><br/>";
echo "<li>".$result['s3']."</li><br/>";


}

?>
</ul>
                            
							</div>
						<div class="services-grid">
							<a href="#">Main Course</a>
							                       <ul>
<?php

while($result=mysql_fetch_assoc($maincourse)){


echo "<li>".$result['m1']."</li><br/>";
echo "<li>".$result['m2']."</li><br/>";
echo "<li>".$result['m3']."</li><br/>";
echo "<li>".$result['m4']."</li><br/>";


}

?>
</ul>
						</div>
						<div class="services-grid">
							<a href="#">Desserts</a>
													                       <ul>
<?php

while($result=mysql_fetch_assoc($desserts)){


echo "<li>".$result['d1']."</li><br/>";
echo "<li>".$result['d2']."</li><br/>";
echo "<li>".$result['d3']."</li><br/>";




}

?>
</ul>
							</div>
						<div class="services-grid">
							<a href="#">Beverages</a>
																			                       <ul>
<?php

while($result=mysql_fetch_assoc($beverages)){


echo "<li>".$result['b1']."</li><br/>";
echo "<li>".$result['b2']."</li><br/>";
echo "<li>".$result['b3']."</li><br/>";



}

?>
</ul>
							</div>
							
						 <div class="clear"> </div>
				    <form action="Dining_Reservation.html">
					<span><input type="submit" class="mybutton" value="Book Table" style="display: block; margin: 0 auto;"></span>
					</form>
					</div>
					
				
				<div class="specials">
					<div class="specials-heading">
						<h3>Our Menu</h3>
						<div class="clear"> </div>
					<div class="about-info">
					<p>Keen to push traditional Indian culinary delights into the 21st century, our experimental menu serves the most exotic dishes you can find anywhere in the country&#39;s well you get the picture.
					   If you haven&#39;t crossed this one off your list yet, the tasting menu paired with the wine is a great way to get introduced to the ingenious palette of the restaurant that stands 29th on the Asia&#39;s Best List. 
					   Speciality - The signature truffle dishes, such as the risotto with fresh Umbrian black truffle and the tagliolini with pancetta and Umbrian black truffle</p>
					</div>
					</div>
					<div class="clear"> </div>
					<div class="specials-grids">
						<div class="special-grid">
							<a href="#">Vegetarian</a>
							<ol>
							<li>Indian Bread</li><br/>
							<li>Palak Paneer</li><br/>
							<li>Kadai Paneer</li><br/>
							<li>Chole bhature</li><br/>
							<li>Rumali roti</li><br/>
							<li>Baingan bharta</li><br/>
							<li>Masala Dosa</li><br/>
							<li>Bhindi masala fry</li><br/>
							<li>Idli Vada</li><br/>
							<li>Malai Kofta</li><br/>
							<li>Samosa and Pakoda</li><br/>
							<li>Gobi Manchuri</li><br/>
							<li>North Indian Meal</li><br/>
							<li>Carrot Halwa</li><br/>
							<li>Kheer</li><br/>
							<li>Navratan Korma</li><br/>
							<li>Masala Chai</li><br/>
							<li>Rogan Josh</li><br/>
							<li>Veg Biriyani</li><br/>
							</ol>
							</div>
						<div class="special-grid">
							<a href="#">Non Vegetarian</a>
							<ol>
							<li>Chicken Curry</li><br/>
							<li>Fish Curry </li><br/>
							<li>Butter Chicken</li><br/>
							<li>Chicken Roast Masala</li><br/>
							<li>Almond Chicken</li><br/>
							<li>Dahi Murg</li><br/>
							<li>Methi Murg</li><br/>
							<li>Egg kurma</li><br/>
							<li>Crab Curry</li><br/>
							<li>Chicken Biryani</li><br/>
							<li>Shrimp Biryani</li><br/>
							<li>Chicken Manchuri</li><br/>
							<li>Chilli Chicken</li><br/>
							<li>Chicken Lollypop</li><br/>
							<li>Fish Masala</li><br/>
							<li>Crab Fry</li><br/>
							<li>Fish Cutlet</li><br/>
							<li>Pepper Chicken</li><br/>
							<li>Chicken Fry</li><br/>
							</ol>
							</div>
						<div class="special-grid spe-grid">
							<a href="#">Beverages</a>
							<ol>
							<li>York Sparkling Cuvée Brut</li><br/>
							<li>Zampa Soirée Brut Rosé</li><br/>
							<li>Charosa Selections Sauvignon Blanc</li><br/>
							<li>Fratelli Sangiovese Bianco</li><br/>
							<li>Krsma Sangiovese</li><br/>
							<li>Sula Dindori Reserve Shiraz</li><br/>	
							<li>Myra Reserve Shiraz</li><br/>
							</ol>
							</div>
						<div class="clear"> </div>
					</div>
					<div class="clear"> </div>
					</div>
					<div class="projects-bottom-paination">
						<ul>
							<li><a href="gallery.html">1</a></li>
							<li><a href="menu1.html">2</a></li>
							<li class="active"><a href="#">3</a></li>
							
						</ul>
					</div>
				</div>
				</div>
		 	<!---End-services---->
		 <!---End-content---->
		 <!---start-footer---->
		 <div class="footer">
		<div class="wrap">
			<div class="footer-grid">
				<h3>Subscribe</h3>
				<p>Join our mailing list and get latest news on deals and upcoming events!</p>
				
				<form method="post">
					<span><label>Email</label></span>
					<span><input name="userName" type="text" class="textbox"></span> </br></br>
					<span><input type="submit" class="mybutton" value="Submit"></span>
				</form>
			</div>
			<div class="footer-grid">
				<h3>Special Events</h3>
				<p>Click to view our upcoming events</p>
				<form>
				<span><input type="submit" class="mybutton" value="View"></span>
				</form>
			</div>
			<div class="clear"> </div>
		</div>
		<div class="clear"> </div>
	</div>
		 <!---End-footer---->
	</body>
</html>
