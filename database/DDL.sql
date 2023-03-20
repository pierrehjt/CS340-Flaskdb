/*DDL.SQL
written by: Henri Pierre and David Tuney
lastEdited:02/16/2023*/


SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT=0;

/*Customers holds all data on customers applicable to sales*/
CREATE OR REPLACE TABLE Customers(
	customerID int UNIQUE NOT NULL AUTO_INCREMENT,
    userName varchar(50) UNIQUE NOT NULL,
    password varchar(50) NOT NULL,
    fName varchar(50) NOT NULL,
    lName varchar(50) NOT NULL,
	birthDate DATE NOT NULL,
    telephone varchar(50) NOT NULL,
    streetAddress varchar(255) NOT NULL,
    city varchar(50) NOT NULL,
    state varchar(50) NOT NULL,
    zip varchar(50) NOT NULL,
	cardNum varchar(50) NOT NULL,
    securityCode varchar(50) NOT NULL,
    PRIMARY KEY (customerID)
    
);

/*Orders holds information on when a customer purchased a product*/
CREATE OR REPLACE TABLE Orders(
	orderID int UNIQUE NOT NULL AUTO_INCREMENT,
	datePurchased DATE NOT NULL,
    customerID int NOT NULL,
    PRIMARY KEY (orderID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID)
	ON DELETE CASCADE
    
);

/*vineyard holds information about vineyards*/
CREATE OR REPLACE TABLE Vineyards(
	vineyardID int UNIQUE NOT NULL AUTO_INCREMENT,
	title varchar(255) UNIQUE NOT NULL,
	description varchar(255),
	casesYearly varchar(50),
	yearFounded varchar(4),
	website varchar(255),
	PRIMARY KEY (vineyardID)
	
);

/*products holds information on products in stock*/
CREATE OR REPLACE TABLE Products(
	productID int UNIQUE NOT NULL AUTO_INCREMENT,
    title varchar(255) UNIQUE NOT NULL,
	description varchar(255),
    retailPrice decimal(19,2) NOT NULL,
	vineyardID int NOT NULL,
    PRIMARY KEY (productID),
	FOREIGN KEY (vineyardID) REFERENCES Vineyards(vineyardID)
	ON DELETE CASCADE
);

/*OrderProducts is an intersection table that holds information on 
what order contained what products and how many of said products*/
CREATE OR REPLACE TABLE OrderProducts(
	orderID int NOT NULL,
    productID  int,
	quantity int NOT NULL,
    PRIMARY KEY (orderID, productID),
    FOREIGN KEY (orderID) REFERENCES Orders(orderID)
	ON DELETE CASCADE,
    FOREIGN KEY (productID) REFERENCES Products(productID)
	ON DELETE CASCADE
);




INSERT INTO Customers
(
	userName,
    password,
    fName,
    lName,
    birthDate,
    telephone,
    streetAddress,
    city,
    state,
    zip,
    cardNum,
    securityCode
)
VALUES
(
    'mcochran12', '!Ra6aCrIwANUcHecHec7', 'Monica', 'Cochran', '1972-06-03', '(825) 574-8521', '4492 James Street', 'Rochester', 'New York', '14626', '4519570895394958', '982'
),
(
    'jthomas34', '*rl8uyLFreGl#o8Ipuke', 'Jacob', 'Thomas', '1974-09-16', '(888) 011-6841', '3005 Boone Street', 'Corpus Christi', 'Texas', '36918', '5501578583067356', '383'
),
(
    'apalmer56', '4?FrOVUbeswA_ewlRacO', 'Alicia', 'Palmer', '1974-12-30', '(180) 310-5765', '4152 Oakwood Avenue', 'New York', 'New York', '85842', '3811393559791095', '136'
),
(
    'cwilliams78', 'cE#lPU9?dO!lBRE!3eTh', 'Christopher', 'Williams', '1987-02-17', '(772) 431-5124', '3129 Duke Lane', 'Piscataway', 'New Jersey', '18297', '2045927666843901', '813'
),
(
    'mcampbell90', 'focRiS=lP9fRinA-L_E-', 'Mary', 'Campbell', '1994-08-21', '(306) 158-5494', '2335 Lunetta Street', 'Clearwater', 'Florida', '83906', '7931897834276141', '132'
);

INSERT INTO Orders( customerID, datePurchased)
VALUES
('1',20230209),
('2',20230210),
('3',20230211),
('4',20230211),
('5',20230212);

INSERT INTO Vineyards(title, description, casesYearly, yearFounded, website)
VALUES
(
	'Château Pontet-Canet',
	'a winery in the Pauillac appellation of the Bordeaux wine region of France. Chateau Pontet-Canet is also the name of the red wine produced by this property.',
	'40000',
	'1855',
	'https://www.chateaucanet.com/?lang=en'
),
(
	'William Hill Winery',
	'Founded in 1976 by visionary vineyard developer William Hill, we are located on an exceptionally unique 200-acre parcel at the foot of Atlas Peak on the Silverado Bench.',
	'50000',
	'1976',
	'https://www.williamhillestate.com/'
);


INSERT INTO Products(productID, title, description, retailPrice, vineyardID)
VALUES
(
    '1','Château Canet Blanc', '750 mL', 24.00, '1'
),
(
    '2','Château Canet Rosé', '750 mL', 24.00, '1'
),
(
    '3','Château Canet Rouge', '750 mL', 24.00, '1'
),
(
    '4','William Hill Cabernet', '750 mL', 18.00, '2'
),
(
    '5','William Hill Chardonnay', '750 mL', 18.00, '2'
);

INSERT INTO OrderProducts(orderID, productID, quantity)
VALUES
('1', '1', 1),
('1','2',2),
('1','3',1),
('2','1',4),
('2','4',3),
('3','5',10),
('3','1',4),
('3','3',6),
('4','5',3),
('4','1',7),
('5','4',2);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;