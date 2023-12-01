-- MariaDB dump 10.19-11.1.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ventana_pyside
-- ------------------------------------------------------
-- Server version	11.1.2-MariaDB

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
-- Table structure for table `personas`
--

DROP TABLE IF EXISTS `personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `dni` varchar(12) NOT NULL,
  `edad` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES
(1,'Lorenzo','Bregant','40.704.033',26),
(2,'Pedro','Fernandez','14.503.032',64),
(3,'Juan','Bresan','48.292.944',19),
(4,'Leo','Messi','34.432.543',34),
(5,'Sergio','Aguero','33.593.332',35),
(7,'Miguel','Del Sel','30.212.332',50),
(8,'Peter','Pan','20.321.004',18),
(9,'Juan Pablo','Ferrari','32.445.321',56),
(10,'Pedro','Picapiedra','23.432.169',70),
(11,'Federico','Bal','34.023.044',43),
(12,'Nicolas','Otamendi','35.029.932',37),
(13,'Angel','Di Maria','33.049.239',37),
(14,'Lionel','Scaloni','31.099.323',43),
(15,'Lautaro','Martinez','42.932.123',35),
(16,'Emiliano','Martinez','30.420.213',37),
(17,'Franco','Armani','95.923.924',40),
(18,'Roberto','Gomez','39.344.212',59),
(19,'Leo','Messi','40.556.233',35),
(20,'Jose Maria','Listorti','30.221.059',56),
(21,'Gabriel','Azcua','45.032.942',21),
(22,'Isaias','Fernandez','39.494.922',23),
(23,'Gonzalo','Higuain','34.554.326',47),
(24,'Fernanda','Aguirre','49.233.249',34),
(25,'Maria','De Los Angeles','32.542.334',45),
(26,'Javier','Milei','34.545.662',43),
(27,'Sergio','Massa','24.929.458',57),
(28,'Victoria','Villaruel','39.292.482',49),
(29,'Maximo','Kirchner','29.484.583',50),
(30,'Nicolas','Perez','39.234.934',45),
(31,'Pablo','Neruda','24.945.432',50),
(33,'Susana','Gimenez','12.203.492',70),
(34,'Mirta','Legrand','01.392.942',101),
(36,'Pelado','Almeida','20.342.943',45),
(37,'Mercedes','Sosa','23.556.742',45),
(38,'Maria','Becerra','45.932.994',24),
(39,'Juan','Magan','34.569.064',18),
(40,'Moria','Casan','34.567.223',80),
(41,'Gabriela','Barrera','39.432.456',45),
(42,'Pablo','Medina','23.456.332',40),
(43,'Ezequiel','Medina','19.243.992',34),
(44,'Hugo','Torres','23.456.223',48),
(45,'Sergio','Torres','20.304.504',54),
(46,'Monica','Argento','23.567.543',46),
(47,'Peter','Capusotto','20.432.506',69),
(48,'Sergio','Luna','39.445.932',34),
(49,'Marito','Baracus','30.392.449',37),
(50,'Megan','Fox','39.203.003',38),
(52,'Chicharito','Hernandez','49.292.030',40),
(54,'Luis','Suarez','20.309.442',37),
(55,'Gonzalo','Heredia','29.384.992',28),
(56,'Fernando','Gago','28.394.922',41);
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-01 15:36:05
