/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50716
Source Host           : localhost:3306
Source Database       : eia

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-11-16 22:00:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_EIA_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_EIA_user_id` FOREIGN KEY (`user_id`) REFERENCES `eia_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_enterprise
-- ----------------------------
DROP TABLE IF EXISTS `eia_enterprise`;
CREATE TABLE `eia_enterprise` (
  `enterpriseId` int(11) NOT NULL,
  `NEIType` varchar(255) DEFAULT NULL,
  `nameAbbreviation` varchar(255) DEFAULT NULL,
  `enterpriseName` varchar(255) DEFAULT NULL,
  `environmentAssessmentCompany` varchar(255) DEFAULT NULL,
  `corporateId` varchar(18) DEFAULT NULL,
  `corporateName` varchar(10) DEFAULT NULL,
  `contacts` varchar(10) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `postalCode` varchar(6) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `totalInvestment` int(11) DEFAULT NULL,
  `environmentalProtectionInvestment` int(11) DEFAULT NULL,
  `environmentalProtectionInvestmentProportion` double DEFAULT NULL,
  `floorSpace` int(11) DEFAULT NULL,
  `managementSpace` int(11) DEFAULT NULL,
  `nonAccommodationNum` int(11) DEFAULT NULL,
  `accommodationNum` int(11) DEFAULT NULL,
  `dayWorkTime` int(11) DEFAULT NULL,
  `yearWorkTime` int(11) DEFAULT NULL,
  `investmentTime` int(11) DEFAULT NULL,
  `productNames` varchar(255) DEFAULT NULL,
  `constructionScale` varchar(50) DEFAULT NULL,
  `noiseEquipment` varchar(50) DEFAULT NULL,
  `noiseMonitoringPoints` int(11) DEFAULT NULL,
  `annualSolidWasteOutput` double DEFAULT NULL,
  `annualPowerConsumption` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longtitude` double DEFAULT NULL,
  `east` varchar(50) DEFAULT NULL,
  `south` varchar(50) DEFAULT NULL,
  `west` varchar(50) DEFAULT NULL,
  `north` varchar(50) DEFAULT NULL,
  `township` varchar(5) DEFAULT NULL,
  `soundEnvironmentStandard` varchar(5) DEFAULT NULL,
  `groundwaterArea` varchar(50) DEFAULT NULL,
  `specialOptionforDaliang` varchar(5) DEFAULT NULL,
  `besideWaterTreatmentPlant` varchar(5) DEFAULT NULL,
  `sensitivePointDistance` varchar(5) DEFAULT NULL,
  `waterSourceDistance` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`enterpriseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_equipments
-- ----------------------------
DROP TABLE IF EXISTS `eia_equipments`;
CREATE TABLE `eia_equipments` (
  `equipId` int(11) NOT NULL AUTO_INCREMENT,
  `equipName` varchar(50) NOT NULL,
  `num` int(11) DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `enterpriseId_ID` int(11) NOT NULL,
  PRIMARY KEY (`equipId`),
  KEY `eia_equip_ID` (`enterpriseId_ID`),
  CONSTRAINT `eia_equip_ID` FOREIGN KEY (`enterpriseId_ID`) REFERENCES `eia_enterprise` (`enterpriseId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_materials
-- ----------------------------
DROP TABLE IF EXISTS `eia_materials`;
CREATE TABLE `eia_materials` (
  `materialId` int(11) NOT NULL AUTO_INCREMENT,
  `materialName` varchar(50) NOT NULL,
  `num` double(20,0) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `isOffcut` varchar(5) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `enterpriseId_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`materialId`),
  KEY `fk_material` (`enterpriseId_ID`),
  CONSTRAINT `fk_material` FOREIGN KEY (`enterpriseId_ID`) REFERENCES `eia_enterprise` (`enterpriseId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_products
-- ----------------------------
DROP TABLE IF EXISTS `eia_products`;
CREATE TABLE `eia_products` (
  `productsId` int(11) NOT NULL AUTO_INCREMENT,
  `productsName` varchar(50) DEFAULT NULL,
  `num` bigint(20) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  `enterpriseId_id` int(11) NOT NULL,
  PRIMARY KEY (`productsId`),
  KEY `EIA_products_enterpriseId_id_e0de4fac_fk_EIA_enter` (`enterpriseId_id`),
  CONSTRAINT `EIA_products_enterpriseId_id_e0de4fac_fk_EIA_enter` FOREIGN KEY (`enterpriseId_id`) REFERENCES `eia_enterprise` (`enterpriseId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_user
-- ----------------------------
DROP TABLE IF EXISTS `eia_user`;
CREATE TABLE `eia_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `enterpriseId_id` int(11) NOT NULL,
  `environmentAssessmentCompany` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `EIA_user_enterpriseId_id_a4de3ef9_fk_EIA_enterprise_enterpriseId` (`enterpriseId_id`),
  CONSTRAINT `EIA_user_enterpriseId_id_a4de3ef9_fk_EIA_enterprise_enterpriseId` FOREIGN KEY (`enterpriseId_id`) REFERENCES `eia_enterprise` (`enterpriseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `eia_user_groups`;
CREATE TABLE `eia_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `EIA_user_groups_user_id_group_id_32d8d605_uniq` (`user_id`,`group_id`),
  KEY `EIA_user_groups_group_id_3695c36a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `EIA_user_groups_group_id_3695c36a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `EIA_user_groups_user_id_4d1ed1c9_fk_EIA_user_id` FOREIGN KEY (`user_id`) REFERENCES `eia_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for eia_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `eia_user_user_permissions`;
CREATE TABLE `eia_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `EIA_user_user_permissions_user_id_permission_id_acb13ac1_uniq` (`user_id`,`permission_id`),
  KEY `EIA_user_user_permis_permission_id_ed8c48b8_fk_auth_perm` (`permission_id`),
  CONSTRAINT `EIA_user_user_permis_permission_id_ed8c48b8_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `EIA_user_user_permissions_user_id_969d5028_fk_EIA_user_id` FOREIGN KEY (`user_id`) REFERENCES `eia_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
