-- MariaDB dump 10.19  Distrib 10.6.11-MariaDB, for Linux (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_pierreh
-- ------------------------------------------------------
-- Server version	10.6.11-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Customers`
--

DROP TABLE IF EXISTS `Customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customers` (
  `customerID` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `fName` varchar(50) NOT NULL,
  `lName` varchar(50) NOT NULL,
  `birthDate` date NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `streetAddress` varchar(255) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip` varchar(50) NOT NULL,
  `cardNum` varchar(50) NOT NULL,
  `securityCode` varchar(50) NOT NULL,
  PRIMARY KEY (`customerID`),
  UNIQUE KEY `customerID` (`customerID`),
  UNIQUE KEY `userName` (`userName`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customers`
--

LOCK TABLES `Customers` WRITE;
/*!40000 ALTER TABLE `Customers` DISABLE KEYS */;
INSERT INTO `Customers` VALUES (1,'mcochran12','!Ra6aCrIwANUcHecHec7','Monica','Cochran','1972-06-03','(825) 574-8521','4492 James Street','Rochester','New York','14626','4519570895394958','982'),(2,'jthomas34','*rl8uyLFreGl#o8Ipuke','Jacob','Thomas','1974-09-16','(888) 011-6841','3005 Boone Street','Corpus Christi','Texas','36918','5501578583067356','383'),(3,'apalmer56','4?FrOVUbeswA_ewlRacO','Alicia','Palmer','1974-12-30','(180) 310-5765','4152 Oakwood Avenue','New York','New York','85842','3811393559791095','136'),(4,'cwilliams78','cE#lPU9?dO!lBRE!3eTh','Christopher','Williams','1987-02-17','(772) 431-5124','3129 Duke Lane','Piscataway','New Jersey','18297','2045927666843901','813'),(5,'mcampbell90','focRiS=lP9fRinA-L_E-','Mary','Campbell','1994-08-21','(306) 158-5494','2335 Lunetta Street','Clearwater','Florida','83906','7931897834276141','132');
/*!40000 ALTER TABLE `Customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderProducts`
--

DROP TABLE IF EXISTS `OrderProducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderProducts` (
  `orderID` int(11) NOT NULL,
  `productID` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`orderID`,`productID`),
  KEY `productID` (`productID`),
  CONSTRAINT `OrderProducts_ibfk_1` FOREIGN KEY (`orderID`) REFERENCES `Orders` (`orderID`) ON DELETE CASCADE,
  CONSTRAINT `OrderProducts_ibfk_2` FOREIGN KEY (`productID`) REFERENCES `Products` (`productID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderProducts`
--

LOCK TABLES `OrderProducts` WRITE;
/*!40000 ALTER TABLE `OrderProducts` DISABLE KEYS */;
INSERT INTO `OrderProducts` VALUES (1,1,1),(1,2,2),(1,3,1),(2,1,4),(2,4,3),(3,1,4),(3,3,6),(3,5,10),(4,1,7),(4,5,3),(5,4,2);
/*!40000 ALTER TABLE `OrderProducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Orders` (
  `orderID` int(11) NOT NULL AUTO_INCREMENT,
  `datePurchased` date NOT NULL,
  `customerID` int(11) NOT NULL,
  PRIMARY KEY (`orderID`),
  UNIQUE KEY `orderID` (`orderID`),
  KEY `customerID` (`customerID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `Customers` (`customerID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (1,'2023-02-09',1),(2,'2023-02-10',2),(3,'2023-02-11',3),(4,'2023-02-11',4),(5,'2023-02-12',5);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Products` (
  `productID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `retailPrice` decimal(19,2) NOT NULL,
  `vineyardID` int(11) NOT NULL,
  PRIMARY KEY (`productID`),
  UNIQUE KEY `productID` (`productID`),
  UNIQUE KEY `title` (`title`),
  KEY `vineyardID` (`vineyardID`),
  CONSTRAINT `Products_ibfk_1` FOREIGN KEY (`vineyardID`) REFERENCES `Vineyards` (`vineyardID`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES (1,'Château Canet Blanc','750 mL',24.00,1),(2,'Château Canet Rosé','750 mL',24.00,1),(3,'Château Canet Rouge','750 mL',24.00,1),(4,'William Hill Cabernet','750 mL',18.00,2),(5,'William Hill Chardonnay','750 mL',18.00,2);
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vineyards`
--

DROP TABLE IF EXISTS `Vineyards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Vineyards` (
  `vineyardID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `casesYearly` varchar(50) DEFAULT NULL,
  `yearFounded` varchar(4) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`vineyardID`),
  UNIQUE KEY `vineyardID` (`vineyardID`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vineyards`
--

LOCK TABLES `Vineyards` WRITE;
/*!40000 ALTER TABLE `Vineyards` DISABLE KEYS */;
INSERT INTO `Vineyards` VALUES (1,'Château Pontet-Canet','a winery in the Pauillac appellation of the Bordeaux wine region of France. Chateau Pontet-Canet is also the name of the red wine produced by this property.','40000','1855','https://www.chateaucanet.com/?lang=en'),(2,'William Hill Winery','Founded in 1976 by visionary vineyard developer William Hill, we are located on an exceptionally unique 200-acre parcel at the foot of Atlas Peak on the Silverado Bench.','50000','1976','https://www.williamhillestate.com/');
/*!40000 ALTER TABLE `Vineyards` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-20  0:01:34
