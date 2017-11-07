/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-11-01 13:14:24
*/
USE myschema;
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for enterprise_data
-- ----------------------------
DROP TABLE IF EXISTS `enterprise_data`;
CREATE TABLE `enterprise_data` (
  `NEIType` varchar(255) DEFAULT NULL,
  `nameAbbreviation` varchar(255) DEFAULT NULL,
  `EIA` varchar(255) DEFAULT NULL,
  `corporate_id` char(18) NOT NULL,
  `corporate` varchar(10) DEFAULT NULL,
  `contacts` varchar(10) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `zipCode` char(6) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `totalInvestment` int(11) DEFAULT NULL,
  `EIAInvestment` int(11) DEFAULT NULL,
  `EIAInvestmentProportion` int(11) DEFAULT NULL,
  `floorSpace` double DEFAULT NULL,
  `managementSpace` double DEFAULT NULL,
  `accommodationNum` int(11) DEFAULT NULL,
  `nonaccommodationNum` int(11) DEFAULT NULL,
  `stuffNum` int(11) DEFAULT NULL,
  `dayWT` int(11) DEFAULT NULL,
  `yearWT` int(11) DEFAULT NULL,
  `commissioningDate` int(11) DEFAULT NULL,
  `productNames` varchar(255) DEFAULT NULL,
  `constructionScale` varchar(50) DEFAULT NULL,
  `noiseEquipment` varchar(50) DEFAULT NULL,
  `noiseMonitoringPoints` int(11) DEFAULT NULL,
  `solidWaste` double DEFAULT NULL,
  `annualPowerConsumption` double DEFAULT NULL,
  `longtitude` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `east` varchar(255) DEFAULT NULL,
  `south` varchar(255) DEFAULT NULL,
  `west` varchar(255) DEFAULT NULL,
  `north` varchar(255) DEFAULT NULL,
  `districtTown` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`corporate_id`),
  CONSTRAINT `enterprise_data_ibfk_1` FOREIGN KEY (`corporate_id`) REFERENCES `userdata` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


