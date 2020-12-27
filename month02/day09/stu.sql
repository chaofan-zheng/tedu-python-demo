-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: stu
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cls`
--

DROP TABLE IF EXISTS `cls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('m','w','o') DEFAULT NULL,
  `score` float DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `indexName` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cls`
--

LOCK TABLES `cls` WRITE;
/*!40000 ALTER TABLE `cls` DISABLE KEYS */;
INSERT INTO `cls` VALUES (1,'Lily',19,'w',100),(2,'Tom',16,'m',76),(4,'James',16,'m',93),(5,'Joy',17,'m',69),(6,'Tonny',18,'o',82),(7,'Lucy',18,'w',73),(8,'Alex',16,'m',89),(9,'Emma',18,'w',84);
/*!40000 ALTER TABLE `cls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept`
--

DROP TABLE IF EXISTS `dept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dname` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept`
--

LOCK TABLES `dept` WRITE;
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` VALUES (1,'技术部'),(2,'销售部'),(3,'市场部'),(4,'行政部'),(5,'财务部'),(6,'总裁办公室');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `good_stu`
--

DROP TABLE IF EXISTS `good_stu`;
/*!50001 DROP VIEW IF EXISTS `good_stu`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `good_stu` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `age`,
 1 AS `sex`,
 1 AS `score`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `hobby`
--

DROP TABLE IF EXISTS `hobby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hobby` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `hobby` set('sing','dance','draw') DEFAULT NULL COMMENT '选择兴趣爱好',
  `price` float DEFAULT NULL,
  `tel` char(16) DEFAULT NULL,
  `remark` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hobby`
--

LOCK TABLES `hobby` WRITE;
/*!40000 ALTER TABLE `hobby` DISABLE KEYS */;
INSERT INTO `hobby` VALUES (1,'Lily','sing,dance',43800.9,NULL,'练舞奇才'),(2,'Joy','draw',8800,NULL,'当代达芬奇'),(3,'Emma','sing',24600,NULL,'天籁之音'),(4,'Jame','dance,draw',18000,NULL,NULL),(5,'Tom','sing',20000,NULL,NULL),(6,'Lucy','draw',18000,NULL,NULL);
/*!40000 ALTER TABLE `hobby` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marathon`
--

DROP TABLE IF EXISTS `marathon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marathon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `athlete` varchar(30) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `registration` datetime DEFAULT CURRENT_TIMESTAMP,
  `performance` time DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marathon`
--

LOCK TABLES `marathon` WRITE;
/*!40000 ALTER TABLE `marathon` DISABLE KEYS */;
INSERT INTO `marathon` VALUES (1,'尼古拉斯赵四','1995-10-01','2020-10-30 10:08:23','02:42:58'),(2,'田田边耕夫','1997-06-17','2020-11-02 18:28:03','02:29:18'),(3,'曹操','2001-03-09','2020-11-03 20:18:53','02:28:49'),(4,'奥特曼','1990-10-26','2020-12-03 11:03:07',NULL);
/*!40000 ALTER TABLE `marathon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` tinyint(4) DEFAULT '0',
  `sex` enum('m','w','o') DEFAULT 'o',
  `salary` decimal(8,2) DEFAULT '250.00',
  `hire_date` date NOT NULL,
  `dept_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dept_id` (`dept_id`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `dept` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'Lily',29,'w',20000.00,'2017-04-03',2),(2,'Tom',27,'m',16000.00,'2019-10-03',1),(3,'Joy',30,'m',28000.00,'2016-04-03',1),(4,'Emma',24,'w',8000.00,'2019-05-08',4),(5,'Abby',28,'w',17000.00,'2018-11-03',NULL),(6,'Jame',32,'m',22000.00,'2017-04-07',NULL),(7,'Baron',29,'m',17500.00,'2018-08-13',6);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo`
--

DROP TABLE IF EXISTS `sanguo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `country` enum('魏','蜀','吴') DEFAULT NULL,
  `attack` smallint(6) DEFAULT NULL,
  `defense` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo`
--

LOCK TABLES `sanguo` WRITE;
/*!40000 ALTER TABLE `sanguo` DISABLE KEYS */;
INSERT INTO `sanguo` VALUES (1,'曹操','男','魏',256,63),(2,'张辽','男','魏',328,69),(3,'甄姬','女','魏',168,34),(4,'夏侯渊','男','魏',366,83),(5,'刘备','男','蜀',220,59),(6,'诸葛亮','男','蜀',170,54),(7,'赵云','男','蜀',360,70),(8,'张飞','男','蜀',370,80),(9,'孙尚香','女','蜀',249,62),(10,'大乔','女','吴',190,44),(11,'小乔','女','吴',188,39),(12,'周瑜','男','吴',300,60),(13,'吕蒙','男','吴',300,71);
/*!40000 ALTER TABLE `sanguo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_bak`
--

DROP TABLE IF EXISTS `student_bak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_bak` (
  `id` int(11) NOT NULL DEFAULT '0',
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `score` float DEFAULT '0',
  `hobby` set('sing','dance','draw') DEFAULT NULL COMMENT '选择兴趣爱好',
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_bak`
--

LOCK TABLES `student_bak` WRITE;
/*!40000 ALTER TABLE `student_bak` DISABLE KEYS */;
INSERT INTO `student_bak` VALUES (1,'Lily',19,100,'sing,dance',43800.9),(5,'Joy',17,69,'draw',8800),(9,'Emma',18,84,'sing',24600),(2,'Tom',16,76,'sing',20000),(7,'Lucy',18,73,'draw',18000);
/*!40000 ALTER TABLE `student_bak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `good_stu`
--

/*!50001 DROP VIEW IF EXISTS `good_stu`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `good_stu` AS select `cls`.`id` AS `id`,`cls`.`name` AS `name`,`cls`.`age` AS `age`,`cls`.`sex` AS `sex`,`cls`.`score` AS `score` from `cls` where (`cls`.`score` > 70) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 11:18:59
