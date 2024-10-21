-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: dbLibrosAnton
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

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
-- Table structure for table `tComentarios`
--

DROP TABLE IF EXISTS `tComentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tComentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `libro_id` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `libro_id` (`libro_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `tComentarios_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `tLibros` (`id`),
  CONSTRAINT `tComentarios_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `tUsuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tComentarios`
--

LOCK TABLES `tComentarios` WRITE;
/*!40000 ALTER TABLE `tComentarios` DISABLE KEYS */;
INSERT INTO `tComentarios` VALUES
(1,'La mejor novela de fantasía del mundo',1,1),
(2,'Famoso articulo de la revista Rolling Stone de 1971',2,1),
(3,'Primer libro de la antologia de ciencia ficcion de Dan Simmons',3,1),
(4,'El esperado nuevo manga de la autora de Dorohedoro',4,1),
(5,'Uno de los pilares fundacionales del universo del Mundodisco de Terry Pratchett',5,1);
/*!40000 ALTER TABLE `tComentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tLibros`
--

DROP TABLE IF EXISTS `tLibros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tLibros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) DEFAULT NULL,
  `imagen` varchar(200) DEFAULT NULL,
  `anho` year(4) DEFAULT NULL,
  `genero` varchar(200) DEFAULT NULL,
  `autor` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tLibros`
--

LOCK TABLES `tLibros` WRITE;
/*!40000 ALTER TABLE `tLibros` DISABLE KEYS */;
INSERT INTO `tLibros` VALUES
(1,'El nombre del viento','https://m.media-amazon.com/images/I/91PjnllfsxL._AC_UF894,1000_QL80_.jpg',2007,'Fantasia','P.Rothfuss'),
(2,'Miedo y Asco en Las Vegas','https://m.media-amazon.com/images/I/81qlbvlo58L._UF1000,1000_QL80_.jpg',1971,'Articulo','Hunter S. Thompson'),
(3,'Hyperion','https://m.media-amazon.com/images/I/91Ky9KCfAIL._UF1000,1000_QL80_.jpg',1989,'Ciencia Ficcion','Dan Simmons'),
(4,'Dai Dark','https://content.eccediciones.com/productos/19819/sobrecubierta_dai_dark_num1_WEB.jpg',2019,'Manga','Q Hayashida'),
(5,'Guardias! Guardias!','https://m.media-amazon.com/images/I/91di6iveLhL._AC_UF894,1000_QL80_.jpg',1989,'Fantasía/Comentario Social','Terry Pratchett');
/*!40000 ALTER TABLE `tLibros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUsuarios`
--

DROP TABLE IF EXISTS `tUsuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tUsuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apell` varchar(50) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `pass` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUsuarios`
--

LOCK TABLES `tUsuarios` WRITE;
/*!40000 ALTER TABLE `tUsuarios` DISABLE KEYS */;
INSERT INTO `tUsuarios` VALUES
(1,'Anton','EB','antoneb@mail.mail','123'),
(2,'Raul','PA','raulpa@mail.mail','123');
/*!40000 ALTER TABLE `tUsuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-21 17:45:55
