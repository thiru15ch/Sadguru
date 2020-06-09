# Sadguru's Amrut Tulya Tea Shop.

>> Download the project from github
>> Install python latest version : [Windows x86-64 executable installer](https://www.python.org/downloads/release/python-377/)
>> Install sublime text editor : [Click on Download For Windows](https://www.sublimetext.com/)
>> Set the environment variables - 

		<path installed>\Python\Python37\Scripts
		<path installed>\Python\Python37
		<path installed>\python\python37\lib\site-packages
		
>> Install flask using CMD 'pip install flask'
>> Install forms module using CMD 'pip install flask-wtf'
>> Install sqlalchemy using CMD 'pip install flask_sqlalchemy'
>> Install mysqlclient using CMD 'pip install mysqlclient'


>> Download XAMPP and install it for mysql db

>> In XAMPP control panel start apache and mysqldb. Then click on admin beside sql which redirects to phpmyadmin/mysqldb

	create a database name as 'sadguru'
	create a table named 'items' - cretae below columns

	id(INT, PRIMARY) - check Auto Increment option(A_I)
	name(text)
	description(text)
	price(int)
	status(int)
	image_file(varchar)
	
	
>> Finally open the command prompt in Windows & change the directory to where the project is located

>> Type the command - python app.py

	Now you will get a running on http://27.0.0.1:5000/

>> Copy the above host link and paste it in browser to see 'Sadguru's Amrit Tulya Tea Shop' homepage.
 
 
