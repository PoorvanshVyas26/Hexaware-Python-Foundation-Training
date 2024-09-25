use TECHSHOP;

--1

select * from Customers;
select * from Orders;
select * from Products;
select * from OrderDetails;


SELECT Customers.CustomerID, Customers.FirstName, Customers.LastName, Customers.Email
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;


--2

SELECT COUNT(*) AS TotalProducts
FROM Products;

--3
SELECT SUM(a.Quantity*b.Price) as Revenue
FROM OrderDetails a , Products b
WHERE a.ProductID = b.ProductID

--4

DECLARE @ProductName NVARCHAR(100);

SET @ProductName = 'Smartphone';

SELECT AVG(a.Quantity) Average  , b.ProductName 

FROM  OrderDetails a , Products b

WHERE a.ProductID = b.ProductID

AND ProductName = @ProductName

GROUP BY b.ProductName


--5

DECLARE @CustomerID int = 2 ;

SELECT a.CustomerID , SUM(c.Quantity * b.Price) TOTAL_REVENUE

FROM Customers a , Products b , OrderDetails c , Orders d

WHERE b.ProductID = c.ProductID

AND c.OrderID = d.OrderID

AND d.CustomerID = a.CustomerID

AND a.CustomerID = @CustomerID

GROUP BY a.CustomerID 

--UNION ALL
--SELECT a.CustomerID ,'Total' AS ProductName, SUM(c.Quantity * b.Price) TOTAL_REVENUE

--FROM Customers a , Products b , OrderDetails c , Orders d

--WHERE b.ProductID = c.ProductID

--AND c.OrderID = d.OrderID

--AND d.CustomerID = a.CustomerID

--AND a.CustomerID = @CustomerID

--GROUP BY a.CustomerID;



--6

SELECT TOP 1 WITH TIES C.FirstName, C.LastName, COUNT(O.OrderID) AS TotalOrders
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.FirstName, C.LastName
ORDER BY TotalOrders DESC;


--7

SELECT TOP 1 WITH TIES a.ProductName , SUM(b.Quantity) Units_Sold

FROM Products a , OrderDetails b

WHERE a.ProductID = b.ProductID

GROUP BY a.ProductName

ORDER BY Units_Sold DESC;


--8

SELECT TOP 1 WITH TIES a.FirstName , a.LastName , SUM(b.TotalAmount) Amount

FROM Customers a , Orders b

WHERE a.CustomerID = b.CustomerID

GROUP BY a.FirstName , a.LastName

ORDER BY Amount DESC;


--9


SELECT avg(o.TotalAmount) AVG_AMOUNT , o.CustomerID

FROM Orders o
GROUP BY  o.CustomerID;


select * from Orders;

--10

SELECT a.FirstName , a.LastName , COUNT(b.OrderID) Order_Count

FROM Customers a , Orders b

WHERE a.CustomerID = b.CustomerID

GROUP BY a.FirstName , a.LastName;

select * from Categories;
select * from Artworks;