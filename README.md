# flask_app
This is a simple web application to view and manage the products in the repository built using Flask.

// This application lets the user the view and manage products in differen locations. Actions on the products in the inventory can be done from the Home page itself.
  In the Home page, three can be input fields can be seen(Product Name, Origin location, Destination Location).
  Depending upon the input from the user, a new product will be created and be placed in a location or an existing product will be moved to a different location.
  Product_Name which is chosen a unique field and hence no duplicates can be created.
  If the product is being newly created, Origin destination need to be empty. Similarly, if the product is being moved out,destination field is required to empty, if fields are not
  given properly, users will be prompted with a message.
  In any case of update or a new entry, the movement will be tracked and saved in a table along with the appropriate timestamp.
  
  Home page also has a simple navigation bar with elements to navigate to pages to view the list of all products, locations and movement trackings.
  
 Products tab on the navigation bar lists out all the products, their IDs and their current location.
 Inventories tab lists out all the locations of the shop and the quantity of products available.
 Shippings is basically a history tab which lists out all movements.
 
