-- Adminer 4.8.1 MySQL 10.6.10-MariaDB-log dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

USE `VoorraadBeheer`;

DELIMITER ;;

DROP PROCEDURE IF EXISTS `AddIngredient`;;
CREATE PROCEDURE `AddIngredient`(IN `param_ingredient` varchar(100), IN `param_amount` float, IN `param_unitid` int)
BEGIN
    INSERT INTO tblIngredient (Ingredient, Amount, UnitId)
    VALUES (param_ingredient, param_amount, param_unitid);
END;;

DROP PROCEDURE IF EXISTS `GetIngredient`;;
CREATE PROCEDURE `GetIngredient`(IN `param_ingredient` varchar(100))
BEGIN
SELECT tblIngredient.Id, tblIngredient.Ingredient, tblIngredient.Amount, tblUnit.Unit, tblUnit.UnitSmall FROM tblIngredient
INNER JOIN tblUnit on tblUnit.Id=tblIngredient.UnitId
WHERE tblIngredient.Ingredient = param_ingredient;
END;;

DROP PROCEDURE IF EXISTS `GetIngredients`;;
CREATE PROCEDURE `GetIngredients`()
SELECT tblIngredient.Id, tblIngredient.Ingredient, tblIngredient.Amount, tblUnit.Unit, tblUnit.UnitSmall FROM tblIngredient
INNER JOIN tblUnit on tblUnit.Id=tblIngredient.UnitId;;

DROP PROCEDURE IF EXISTS `IngredientExists`;;
CREATE PROCEDURE `IngredientExists`(IN `param_ingredient` varchar(100))
BEGIN
SELECT @cnt:=COUNT(tblIngredient.Id) FROM tblIngredient
WHERE tblIngredient.Ingredient = param_ingredient;

SELECT @cnt > 0;
END;;

DROP PROCEDURE IF EXISTS `RemoveIngredient`;;
CREATE PROCEDURE `RemoveIngredient`(IN `param_ingredient` varchar(100))
BEGIN
DELETE FROM tblIngredient WHERE Ingredient=param_ingredient;
END;;

DROP PROCEDURE IF EXISTS `UpdateIngredientAmount`;;
CREATE PROCEDURE `UpdateIngredientAmount`(IN `param_ingredient` varchar(100), IN `param_amount` float)
UPDATE tblIngredient
SET Amount = param_amount
WHERE Ingredient = param_ingredient;;

DROP PROCEDURE IF EXISTS `UpdateIngredientAmountAdd`;;
CREATE PROCEDURE `UpdateIngredientAmountAdd`(IN `param_ingredient` varchar(100), IN `param_amount` float)
UPDATE tblIngredient
SET Amount = Amount+param_amount
WHERE Ingredient = param_ingredient;;

DELIMITER ;

DROP TABLE IF EXISTS `tblIngredient`;
CREATE TABLE `tblIngredient` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Ingredient` varchar(100) NOT NULL,
  `Amount` float NOT NULL,
  `UnitId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `UnitId` (`UnitId`),
  CONSTRAINT `tblIngredient_ibfk_1` FOREIGN KEY (`UnitId`) REFERENCES `tblUnit` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;

INSERT INTO `tblIngredient` (`Id`, `Ingredient`, `Amount`, `UnitId`) VALUES
(1,	'Boter',	125,	1)
ON DUPLICATE KEY UPDATE `Id` = VALUES(`Id`), `Ingredient` = VALUES(`Ingredient`), `Amount` = VALUES(`Amount`), `UnitId` = VALUES(`UnitId`);

DROP TABLE IF EXISTS `tblProduct`;
CREATE TABLE `tblProduct` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Amount` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `tblProductIngredient`;
CREATE TABLE `tblProductIngredient` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `ProductId` int(11) NOT NULL,
  `IngredientId` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `UnitId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `ProductId` (`ProductId`),
  KEY `IngredientId` (`IngredientId`),
  KEY `UnitId` (`UnitId`),
  CONSTRAINT `tblProductIngredient_ibfk_1` FOREIGN KEY (`ProductId`) REFERENCES `tblProduct` (`Id`),
  CONSTRAINT `tblProductIngredient_ibfk_2` FOREIGN KEY (`IngredientId`) REFERENCES `tblIngredient` (`Id`),
  CONSTRAINT `tblProductIngredient_ibfk_3` FOREIGN KEY (`UnitId`) REFERENCES `tblUnit` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


DROP TABLE IF EXISTS `tblUnit`;
CREATE TABLE `tblUnit` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Unit` varchar(20) NOT NULL,
  `UnitSmall` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;

INSERT INTO `tblUnit` (`Id`, `Unit`, `UnitSmall`) VALUES
(1,	'Kilo gram',	'Kg')
ON DUPLICATE KEY UPDATE `Id` = VALUES(`Id`), `Unit` = VALUES(`Unit`), `UnitSmall` = VALUES(`UnitSmall`);

-- 2022-12-09 16:45:37
