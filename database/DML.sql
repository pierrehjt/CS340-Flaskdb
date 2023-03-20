/*group 139, Henri Pierre and David Tuney
Data Manipulation Queries*/

/*Query for add a new character functionality with colon : character being used to 
denote the variables that will have data from the backend programming language*/

/***********Customer related Queries***********/

/*select all customer ids and names to populate customers dropdown*/
SELECT customerID, fName, lName FROM Customers


/*select a specific customer and all their information for update customer form*/
SELECT customerID, fName, lName, userName, password, birthDate, streetAddress, city, state, zip, telephone, cardNum, securityCode 
FROM Customers WHERE :customerID_selected_from_browse_customer_page


/*add a new customer*/
INSERT INTO Customers (
	fName,
	lName,
	userName,
	password,
	birthDate,
	streetAddress,
	city,
	state,
	zip,
	telephone,
	cardNum,
	securityCode
)
Values (
	:fnameinput,
	:lNameinput,
	:userNameinput,
	:passwordinput,
	:birthDateinput,
	:streetAddressinput,
	:cityinput,
	:stateinput,
	:zipinput,
	:telephoneinput,
	:cardNuminput,
	:securityCodeinput
)


/*update a specific customer and all their information from update customer form*/
UPDATE Customers SET 
	fName = :fnameinput,
	lName = :lNameinput,
	userName = :userNameinput,
	password = :passwordinput,
	birthDate = :birthDateinput,
	streetAddress = :streetAddressinput,
	city = :cityinput,
	state = :stateinput,
	zip = :zipinput,
	telephone = :telephoneinput,
	cardNum = :cardNuminput,
	securityCode = :securityCodeinput
WHERE customerID = :customerID_from_update_form

/*delete a customer*/
DELETE FROM Customers WHERE customerID = :customerID_selected_from_browse_customer_page;


/***********Order related Queries***********/

/* add a new order*/
INSERT INTO Orders(customerID, datePurchased)
VALUES(:customerID_from_dropdown, :dateinput)

/*select all order information to populate orders dropdown*/
SELECT 
	
    CONCAT(fName,' ',lName) AS name,
    Customers.customerID,
    sum(OrderProducts.quantity) as total_products_ordered,
    sum(Products.retailPrice * OrderProducts.quantity) as total_price
	
From Customers
	JOIN Orders ON Customers.customerID = Orders.customerID
	JOIN OrderProducts ON Orders.orderID = OrderProducts.orderID
	LEFT JOIN Products ON OrderProducts.productID = Products.productID
GROUP BY name, Orders.orderID


/*select a specific order and all its information for update order form*/
SELECT 
	Orders.customerID,
    Orders.datePurchased,
    OrderProducts.quantity,
    Products.productID,
    Products.title
FROM Orders
	JOIN OrderProducts ON Orders.orderID = OrderProducts.orderID
    JOIN Products ON OrderProducts.productID = Products.productID
WHERE Orders.orderID = :orderID_selected_from_browse_order_page




/*update a specific Orders purchase date*/
UPDATE Products SET 
	datePurchased = :newdate
WHERE orderID = :orderID_from_update_form

/*remove an order*/
DELETE FROM Orders WHERE orderID = :orderID_selected_from_browse_order_page;


/***********product order Queries***********/
/*add a product to an order*/
INSERT INTO OrderProducts (orderID, productID, quantity)
values (:orderID_from_update_form, :productIDinput, :quantityinput)


/*remove a product from an order*/
DELETE FROM orderProducts WHERE productID = :productIDinput

/*update product ordered*/
UPDATE OrderProducts SET
	productID = :product_from_update_form
	quantity = :quantityinput
WHERE orderID = :orderID_from_update_form


/***********product related Queries***********/
/*add a new product*/
INSERT INTO Products (title, description, retailPrice, vineyardID)
Values (:titleinput, :descinput, :priceinput, :vineyard_dropdown)

/*select all product ids and titles to populate products dropdown*/
SELECT productID, title FROM Products;


/*select a specific product and all its information for update product form*/
SELECT productID, title, description, retailPrice, vineyardID
FROM Products
WHERE :productID_selected_from_browse_product_page


/*update a specific product and all its information from update product form*/
UPDATE Products SET 
	title =:titleinput
	description =:descinput
	retailPrice = :priceinput
WHERE productID = :productID_from_update_form


/*delete a product*/
DELETE FROM Products WHERE productID = :productID_selected_from_browse_product_page;

/***********Vineyard related Queries***********/
/*add a new vineyard*/
INSERT INTO Vineyards(title, description, casesYearly, yearFounded, website)
values (:titleinput, :descriptioninput, :casesYearlyinput, :yearinput, :websiteinput)

/*select all vineyards to populate vineyards dropdown*/
SELECT 
	Vineyards.vineyardID,
    Vineyards.title,
	Vineyards.description,
	Vineyards.casesYearly,
	Vineyards.yearFounded,
	Vineyards.website
From Vineyards
GROUP BY vineyardID

/*select all wines associated to a vineyard*/
SELECT 
	Products.productID,
	Products.title AS Product_Name,
    Products.retailPrice
FROM Vineyards
	LEFT JOIN Products ON Vineyards.vineyardID = Products.vineyardID
WHERE Vineyards.vineyardID = :selected_vineyard

/*update a vineyard*/
UPDATE Vineyards SET
	vineyardID = :product_from_update_form
	title = :titleinput
	description = :descriptioninput
	casesYearly = :casesYearlyinput
	yearFounded = :yearFoundedinput
	website = :websiteinput
WHERE orderID = :orderID_from_update_form

/*delete a vineyard*/
DELETE FROM Vineyards WHERE vineyardID = :vineyardID_selected_from_browse_vineyards_page;

