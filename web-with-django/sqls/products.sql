/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : django

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-10-30 23:27:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `product_name` varchar(255) DEFAULT NULL,
  `corporate_id` char(18) NOT NULL,
  `unit` varchar(20) NOT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`corporate_id`),
  CONSTRAINT `enterprise_data_ibfk_1` FOREIGN KEY (`corporate_id`) REFERENCES `userdata` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
