/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorites` (
  `pk_favorites` int NOT NULL AUTO_INCREMENT,
  `user_pk_user` int NOT NULL,
  `recipe_pk_recipe` int NOT NULL,
  PRIMARY KEY (`pk_favorites`),
  KEY `fk_favorites_user_idx` (`user_pk_user`),
  KEY `fk_favorites_recipe1_idx` (`recipe_pk_recipe`),
  CONSTRAINT `fk_favorites_recipe1` FOREIGN KEY (`recipe_pk_recipe`) REFERENCES `recipe` (`pk_recipe`),
  CONSTRAINT `fk_favorites_user` FOREIGN KEY (`user_pk_user`) REFERENCES `user` (`pk_user`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
INSERT INTO `favorites` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,3),(5,5,5),(6,5,3),(7,2,7),(8,6,1),(9,2,8),(10,9,2);
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fridge`
--

DROP TABLE IF EXISTS `fridge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fridge` (
  `pk_fridge` int NOT NULL AUTO_INCREMENT,
  `user_pk_user` int NOT NULL,
  `ingredient_pk_ingredient` int NOT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`pk_fridge`),
  KEY `fk_fridge_user1_idx` (`user_pk_user`),
  KEY `fk_fridge_ingredient1_idx` (`ingredient_pk_ingredient`),
  CONSTRAINT `fk_fridge_ingredient1` FOREIGN KEY (`ingredient_pk_ingredient`) REFERENCES `ingredient` (`pk_ingredient`),
  CONSTRAINT `fk_fridge_user1` FOREIGN KEY (`user_pk_user`) REFERENCES `user` (`pk_user`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fridge`
--

LOCK TABLES `fridge` WRITE;
/*!40000 ALTER TABLE `fridge` DISABLE KEYS */;
INSERT INTO `fridge` VALUES (1,1,1,10),(2,1,2,2),(3,1,3,0),(4,1,4,1),(5,1,6,1),(6,2,1,50),(7,5,2,32),(8,7,2,645),(9,9,3,203),(10,6,7,2);
/*!40000 ALTER TABLE `fridge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredient`
--

DROP TABLE IF EXISTS `ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredient` (
  `pk_ingredient` int NOT NULL AUTO_INCREMENT,
  `recipe_pk_recipe` int NOT NULL,
  `unit_price` int DEFAULT NULL,
  `refridgerated` tinyint DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`pk_ingredient`),
  KEY `fk_ingredient_recipe1_idx` (`recipe_pk_recipe`),
  CONSTRAINT `fk_ingredient_recipe1` FOREIGN KEY (`recipe_pk_recipe`) REFERENCES `recipe` (`pk_recipe`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
INSERT INTO `ingredient` VALUES (1,1,2,1,'Eggs'),(2,1,3,1,'Milk'),(3,1,1,0,'Salt'),(4,3,1,0,'Bread'),(5,2,4,0,'Lemon'),(6,2,2,0,'Sugar'),(7,9,3,0,'Tomato'),(8,9,6,1,'Cheese'),(9,4,1,0,'Banana'),(10,7,10,1,'Chicken'),(11,2,5,0,'Pumpernickel');
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `pk_recipe` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `serving_size` int DEFAULT NULL,
  `cooking_time` int DEFAULT NULL,
  `makes` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`pk_recipe`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'scrambled eggs',1,5,'2 servings'),(2,'traybake',1,60,'8 servings'),(3,'toast',1,1,'1 servings'),(4,'Banana Bread',1,8,'6 servings'),(5,'Cheeseburger soup',2,1,'3 servings'),(6,'Amish Breakfast Casserole',4,7,'10 serving'),(7,'Pumpkin Spice Cupcakes',1,1,'12 serving'),(8,'Chicken Pot Pie',1,2,'8 serving'),(9,'Pizza',1,2,'8 serving'),(10,'Chicken Fajitas',2,1,'1 serving');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `steps`
--

DROP TABLE IF EXISTS `steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `steps` (
  `pk_steps` int NOT NULL AUTO_INCREMENT,
  `recipe_pk_recipe` int NOT NULL,
  `step_description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`pk_steps`),
  KEY `fk_steps_recipe1_idx` (`recipe_pk_recipe`),
  CONSTRAINT `fk_steps_recipe1` FOREIGN KEY (`recipe_pk_recipe`) REFERENCES `recipe` (`pk_recipe`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `steps`
--

LOCK TABLES `steps` WRITE;
/*!40000 ALTER TABLE `steps` DISABLE KEYS */;
INSERT INTO `steps` VALUES (1,1,'1: Crack the egg'),(2,1,'2: Whisk the egg'),(3,1,'3: Add the milk'),(4,1,'4: Mix and put over heat'),(5,2,'1: Mix all dry ingredients together'),(6,2,'2: Crack and whisk the eggs, mix with milk'),(7,2,'3: Cobmine each bowl, stir well'),(8,2,'4: Bake for 40 minutes as 375 degrees'),(9,2,'5: Bring out, let cool for 45 minutes'),(10,2,'6: Cut and serve');
/*!40000 ALTER TABLE `steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store` (
  `pk_store` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `hours` varchar(45) DEFAULT NULL,
  `employee_count` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`pk_store`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store`
--

LOCK TABLES `store` WRITE;
/*!40000 ALTER TABLE `store` DISABLE KEYS */;
INSERT INTO `store` VALUES (1,'Target','101 Main Street','9 to 5','500'),(2,'Walmart','102 Main Street','24/7','300'),(3,'Wegmans','143 Main Street','10-4','200'),(4,'Rite Aid','Forbes & Atwood','24/7','20'),(5,'CSV','102 Centre Ave','24/7','15'),(6,'Forbes Street Market','534 Forbes Ave','24/7','15'),(7,'Publics','163 Merian','9 to 5','432'),(8,'7/11','328 Green Lane','24/7','3'),(9,'Sunoco','PA Turnpike','24/7','200'),(10,'Wawa','423 University Drive C','24/7','3000');
/*!40000 ALTER TABLE `store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_inventory`
--

DROP TABLE IF EXISTS `store_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_inventory` (
  `pk_store_inventory` int NOT NULL AUTO_INCREMENT,
  `ingredient_pk_ingredient` int NOT NULL,
  `store_pk_store` int NOT NULL,
  `stock` int DEFAULT NULL,
  PRIMARY KEY (`pk_store_inventory`),
  KEY `fk_store_inventory_ingredient1_idx` (`ingredient_pk_ingredient`),
  KEY `fk_store_inventory_store1_idx` (`store_pk_store`),
  CONSTRAINT `fk_store_inventory_ingredient1` FOREIGN KEY (`ingredient_pk_ingredient`) REFERENCES `ingredient` (`pk_ingredient`),
  CONSTRAINT `fk_store_inventory_store1` FOREIGN KEY (`store_pk_store`) REFERENCES `store` (`pk_store`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_inventory`
--

LOCK TABLES `store_inventory` WRITE;
/*!40000 ALTER TABLE `store_inventory` DISABLE KEYS */;
INSERT INTO `store_inventory` VALUES (1,1,1,60),(2,2,1,50),(3,3,1,756),(4,4,1,534),(5,5,1,6453),(6,6,1,34),(7,2,2,543),(8,4,2,423),(9,4,2,5432),(10,5,2,5);
/*!40000 ALTER TABLE `store_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `pk_user` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `joined_date` datetime(6) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`pk_user`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'user1','2001-02-01 00:00:00.000000','john','smith'),(2,'user2','2001-02-02 00:00:00.000000','Jane','Doe'),(3,'user3','2001-02-03 00:00:00.000000','Jim','Davis'),(4,'user4','2002-02-03 00:00:00.000000','Garfield','The cat'),(5,'user5','2004-02-03 00:00:00.000000','Suresh','Rapp'),(6,'user6','2005-02-03 00:00:00.000000','Francine','Ruarc'),(7,'user7','2006-02-03 00:00:00.000000','Branimir','Vogels'),(8,'user8','2007-02-03 00:00:00.000000','Kaltrina','Embla'),(9,'user9','2009-02-03 00:00:00.000000','Amadou','Spano'),(10,'user10','2010-02-03 00:00:00.000000','Xenagoras','Moss');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-24 14:06:11

#SQL Queries
#Shows the contents of the user's fridge ordered by lowest to highest
#"What ingredients am I low on"
SELECT i.name, f.amount
FROM ingredient i 
JOIN fridge f
ON i.pk_ingredient = f.pk_fridge
JOIN user u
ON f.user_pk_user = u.pk_user
WHERE u.user_name = "user1"
ORDER BY f.amount ASC;

#Show if the user has ingredients to make scambled eggs
#"Can I make scrambled eggs?"
SELECT i.name, if(f.amount > 0, "Yes", "No") as "Having"
FROM recipe r
JOIN ingredient i 
ON r.pk_recipe = i.recipe_pk_recipe
JOIN fridge f 
ON i.pk_ingredient = f.ingredient_pk_ingredient
JOIN user u
ON f.user_pk_user = u.pk_user
WHERE u.user_name = "user1" AND i.recipe_pk_recipe = 1;

#Cost of making the recipe using unit price
#"How much will it cost me to make scambled eggs"
SELECT r.name, SUM(i.unit_price) as "Total Price"
FROM recipe r
JOIN ingredient i 
ON r.pk_recipe = i.recipe_pk_recipe
JOIN fridge f 
ON i.pk_ingredient = f.ingredient_pk_ingredient
WHERE i.recipe_pk_recipe = 1
GROUP BY r.name;

#Details on a store
#"Where and when can I go to Target"
SELECT s.name, s.address, s.hours, s.employee_count
FROM store s
WHERE s.name = "Target";

#Stores that have more than 5 ingredients
#"I am unsure what specific thing I want. I want to go to a store with a large stock, list all those stores"
SELECT s.name, COUNT(i.name) AS "Item Count"
FROM store s 
JOIN store_inventory si
ON s.pk_store = si.store_pk_store
JOIN ingredient i 
ON si.ingredient_pk_ingredient = i.pk_ingredient
HAVING COUNT(i.name) > 5;

#Shows all saved ingredients and their availability or not in local stores
#EX: Pumpernickle is not available anywhere 
#This can also be changed to show the availability of a specific ingredient with the WHERE statement for further value 
#"What's the inventory of all local buisnesses"
SELECT i.name as "Ingredient", IFNULL(s.name,"Not Available") as "Store Name", IFNULL(si.stock, 0) AS "Stock"
FROM ingredient i
LEFT JOIN store_inventory si
ON i.pk_ingredient = si.ingredient_pk_ingredient
LEFT JOIN store s
ON s.pk_store = si.store_pk_store;

#How many of x ingredient do I have
#"How many eggs do I have
SELECT i.name as "Name", f.amount as "Amount"
FROM user u 
JOIN fridge f
ON u.pk_user = f.user_pk_user
JOIN ingredient i 
ON i.pk_ingredient = f.ingredient_pk_ingredient
WHERE u.user_name = "user1" and i.name IN (SELECT name 
									FROM ingredient 
                                    WHERE name = "Eggs");
                                    
#Call the steps of a recipe
#"What are the steps of scrambled eggs"
SELECT s.step_description as "Step:"
FROM recipe r
JOIN steps s
ON r.pk_recipe = s.recipe_pk_recipe
WHERE r.name = "scrambled eggs"
ORDER BY s.pk_steps  ASC;

#Call the ingredients of a recipe
#"What are the ingredients in this recipe"
SELECT i.name as "Ingredient"
FROM recipe r
JOIN ingredient i
ON i.recipe_pk_recipe = r.pk_recipe
WHERE r.name IN (SELECT name FROM recipe WHERE name = "traybake");

#Show a user profile 
SELECT u.user_name as "User Name", CONCAT(u.first_name," ",u.last_name) as "Name", joined_date as "Date Joined",
(SELECT count(name) FROM recipe r
JOIN favorites f ON r.pk_recipe = f.recipe_pk_recipe
 WHERE f.user_pk_user = 1) AS "Favorited Recipe Count"
FROM user u
WHERE u.user_name = "user1";

#Rollback transaction for removing a user and their fridge contents
BEGIN;

	DELETE FROM fridge 
    WHERE pk_user_pk = 1;
    
    DELETE FROM USER
    WHERE pk_user = 1;
    
	COMMIT;