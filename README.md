# Sadguru's Amrut Tulya Tea Shop.

Import the folder into Sublime Text

Created app.py for routing(where url binding to that function) and forms.py for form input

Different templates created that contain static data and rendered using Jinja template library

Run the app.py file in the command prompt where it says Running on http://127.0.0.1:5000/

go to the below [link](http://127.0.0.1:5000/) to see the frontend of Sadguru's Amrut tulya tea shop.

It shows a button **Additem** and when you click it will call the backend service that pop up the new item form to add item to the inventory.

on click of additem,values are saved in the Sadguru table in [mysqldatabase](http://localhost/phpmyadmin/sql.php?db=sadguru&table=items&pos=0) and redirects to where list of items is displayed using GET method.

upon click on the item name will call backend service that displays the item details alone.

Finally we have a **Delete** button that calls delete request where the item deleted from the frontend. But in the backend we set the status of item as '1'(as the records should not be actually deleted in the Database).

The items with status 0 will be displayed every time on the frontend.
    
