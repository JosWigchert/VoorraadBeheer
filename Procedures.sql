DELIMITER ;;

CREATE PROCEDURE `AddProduct`(IN `param_product` varchar(100), IN `param_amount` int)
BEGIN
    INSERT INTO tblProduct (Product, Amount)
    VALUES (param_product, param_amount);
END;;

CREATE PROCEDURE `GetProduct`(IN `param_product` varchar(100))
BEGIN
    SELECT Id, Product, Amount FROM tblProduct
    WHERE Product = param_product;
END;;

CREATE PROCEDURE `GetProducts`()
BEGIN
    SELECT Id, Product, Amount FROM tblProduct;
END;;

CREATE PROCEDURE `ProductExists`(IN `param_product` varchar(100))
BEGIN
    SELECT @cnt:=COUNT(Id) FROM tblProduct
    WHERE Product = param_product;

    SELECT @cnt > 0;
END;;

CREATE PROCEDURE `RemoveProduct`(IN `param_product` varchar(100))
BEGIN
    DELETE FROM tblProduct WHERE Product=param_product;
END;;

CREATE PROCEDURE `UpdateProductAmount`(IN `param_product` varchar(100), IN `param_amount` float)
BEGIN
    UPDATE tblProduct
    SET Amount = param_amount
    WHERE Ingredient = param_product;
END;;

CREATE PROCEDURE `UpdateProductAmountAdd`(IN `param_product` varchar(100), IN `param_amount` float)
BEGIN
    UPDATE tblProduct
    SET Amount = Amount+param_amount
    WHERE Product = param_product;
END;;

