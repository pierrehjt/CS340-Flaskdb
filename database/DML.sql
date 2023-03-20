/*group 139, Henri Pierre and David Tuney
Data Manipulation Queries
definitions of the SQL queries used in the CS340 database project
lastEdited:03/20/2023*/


/*Query for add a new character functionality with colon : character being used to 
denote the variables that will have data from the backend programming language*/

/***********Customer related Queries***********/

/*select all customers to populate customer page/ customer dropdowns*/
SELECT * FROM Customers


/*select a specific customer and all their information for update customer form*/
SELECT * FROM Customers WHERE customerID = :inputcustomerID


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
DELETE FROM Customers WHERE customerID = :inputcustomerID


/***********Order related Queries***********/
/*add order*/
INSERT INTO Orders (datePurchased, customerID) VALUES (:inputdatePurchased, :inputcustomerID)

/*add product to order*/
INSERT INTO OrderProducts (orderID, productID, quantity) VALUES (:inputorderID, :inputproductID, :inputquantity)

/* select order information to populate orders page */
SELECT 
	Orders.datePurchased,
	Customers.customerID,
	Orders.orderID,
	Products.productID,
	Products.title,
	sum(OrderProducts.quantity) as quantity_ordered,
	sum(Products.retailPrice * OrderProducts.quantity) as total_price
FROM Customers
	JOIN Orders ON Customers.customerID = Orders.customerID
	JOIN OrderProducts ON Orders.orderID = OrderProducts.orderID
	LEFT JOIN Products ON OrderProducts.productID = Products.productID
GROUP BY orderID, Products.productID

/*select all orders to populate orders dropdown*/
SELECT * FROM Orders

/*select a specific order to edit*/
SELECT * FROM Orders WHERE orderID = :inputorderID

/*select all products in an order*/
SELECT * FROM OrderProducts WHERE orderID = :inputorderID

/*select specific productid for checking if a product is associated with an order*/
SELECT productID FROM OrderProducts WHERE orderID = :inputorderID AND productID = :inputproductID

/*delete selected order*/
DELETE FROM Orders WHERE orderID = :inputorderID

/*deleted selected item from order*/
DELETE FROM OrderProducts WHERE orderID = :inputorderID AND productID = :productID

/*add user input amount of product to existing order*/
UPDATE OrderProducts SET quantity = quantity + :inputquantity WHERE orderID = :inputorderID AND productID = :inputproductID;


/*update specific product in order*/
UPDATE OrderProducts SET productID = :productID, quantity = :inputquantity WHERE orderID = :inputorderID AND productID = :productID;

/*update specific order*/
UPDATE Orders SET datePurchased = :inputdatePurchased, customerID = :inputcustomerID WHERE orderID = :inputorderID AND customerID = :inputcustomerID;


/***********product related Queries***********/
/*select all Products to populate Products page/ Product dropdowns*/
SELECT * FROM Products

/*select specific product to edit*/
SELECT * FROM Products WHERE productID = :inputproductID

/*select specific productid for checking if a product is associated with an order*/
SELECT productID FROM Products WHERE productID = %s

/*insert new product*/
INSERT INTO Products (title, description, retailPrice, vineyardID) VALUES (:inputtitle, :inputdescription, :inputretailPrice, :inputvineyardID)

/*delete product*/
DELETE FROM Products WHERE productID = :inputproductID

/*edit selected product*/
UPDATE Products SET title =:inputtitle, description =:inputdescription, retailPrice =:inputretailPrice,vineyardID =:inputvineyardID WHERE productID =:inputproductID

/***********Vineyard related Queries***********/
/*select all Vineyards to populate Vineyards page/ Vineyard dropdowns*/
SELECT * FROM Vineyards;

/*select specific vineyard to edit*/
SELECT * FROM Vineyards WHERE vineyardID = :inputvineyardID

/*create new vineyard*/
INSERT INTO Vineyards (title, description, casesYearly, yearFounded, website) VALUES (:inputtitle, :inputdescription, :inputcasesYearly, :inputyearFounded, :inputwebsite)

/*delete vineyard*/
DELETE FROM Vineyards WHERE vineyardID = :inputvineyardID

/*edit specific vineyard*/
UPDATE Vineyards SET title =:inputtitle, description =:inputdescription, casesYearly = :inputcasesYearly,yearFounded = :inputyearFounded,website = :inputwebsite WHERE vineyardID = :inputvineyardID

