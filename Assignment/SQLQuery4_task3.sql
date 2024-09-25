--TASK 3
use TECHSHOP;


--1

select Orders.*,

(select FirstName from Customers

 where Customers.CustomerID=Orders.CustomerID) as Names

 from Orders;

 --2
 select * from OrderDetails;
  select * from Products;

SELECT P.ProductName, 
       SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM Products P
JOIN OrderDetails OD ON P.ProductID = OD.ProductID
GROUP BY P.ProductName;

--3
select * from OrderDetails;

SELECT OrderDetails.OrderID, Customers.FirstName, Customers.Email
FROM OrderDetails
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE OrderDetails.Quantity >= 1;

--4
select* from OrderDetails;
select* from Products;


select top 1 with ties a.ProductName , sum(b.Quantity) as Popular
FROM Products a , OrderDetails b
WHERE a.ProductID = b.ProductID
GROUP BY a.ProductName
ORDER BY Popular DESC;
 
 --5

 select ProductName,Description from Products;

 --6
 
 select a.FirstName ,AVG(b.TotalAmount)
 from Customers a , Orders b
 where a.CustomerID=b.CustomerID
 group by a.FirstName;

 --7 

select top 1 sum(a.Price * b.Quantity) as revenue,b.OrderID , FirstName

		from Products a , OrderDetails b , Orders c, Customers d

		where a.ProductID = b.ProductID
		and c.OrderID=b.OrderID
		and c.CustomerID=d.CustomerID
		group by b.OrderID, FirstName
		order by  revenue desc;

--8
select * from OrderDetails;

select a.ProductName , sum(b.Quantity ) as Number_of_Orders


from Products a , OrderDetails b

where a.ProductID = b.ProductID

group by a.ProductName;


--9
select * from Products;
select * from Orders;
select * from OrderDetails;

DECLARE @ProductName NVARCHAR(100);

SET @ProductName = 'Laptop';

select a.FirstName , b.ProductName

from Products b , Customers a , Orders c , OrderDetails d

where b.ProductID = d.ProductID
and d.OrderID = c.OrderID
and a.CustomerID = c.CustomerID
and ProductName = @ProductName;


--10

--time period - date: Order table OrderDate
--sum - product price* order detail quantity

select * from Orders;

select a.OrderDate, sum(b.price * c.Quantity) as revenue
from products b, Orders a, OrderDetails c
where a.OrderID = c.OrderID
and c.ProductID = b.ProductID
and OrderDate = '2024-09-08'
group  by OrderDate;















