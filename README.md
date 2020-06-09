# Sadguru's Amrut Tulya Tea Shop.

Download the files from GIT to local
 Install python latest version
 Install sublime text editor

set environment variables - 

		<path installed>\Python\Python37\Scripts
		<path installed>\Python\Python37
		<path installed>\python\python37\lib\site-packages
		

install flask - (pip install flask) using CMD

install forms module - pip install flask-wtf

pip install flask_sqlalchemy

pip install mysqlclient


Download XAMPP and istall it for mysql db

In XAMPP control panel start apache and mysqldb. Then click on admin beside sql which redirects to phpmyadmin/mysqldb

	create a database name as 'sadguru'
	create a table named 'items' - cretae below columns

	id(INT, PRIMARY) - check Auto Increment option(A_I)
	name(text)
	description(text)
	price(int)
	status(int)
	image_file(varchar)
	
	
Finally go to CMD change the directory to where the project is located

use the command - python app.py

	Now you will get a running on http://27.0.0.1:5000/
	copy the link and paste it in browser to see sadguru's amrut tulya tea shop homepage.
 
 

    
