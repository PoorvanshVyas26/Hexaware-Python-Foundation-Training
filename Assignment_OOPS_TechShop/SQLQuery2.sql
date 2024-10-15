create database TECHSHOP;
use TECHSHOP;
create table Customers(
CustomerID int identity Primary Key,
FirstName varchar(20),
LastName  varchar(20),Email varchar(40),Phone int,Address varchar(40))create table Products(ProductID int identity Primary Key,ProductName varchar(20),Description varchar(20),Price int)create table Orders(OrderID int identity Primary Key,CustomerID int,Foreign Key(CustomerID) references Customers(CustomerID),OrderDate date,TotalAmount int,)create table OrderDetails(OrderDetailID int identity Primary Key,OrderID int,Foreign Key	(OrderID) references Orders(OrderID),ProductID int,Foreign Key (ProductID) references Products(ProductID),Quantity int)create table Inventory(InventoryID int identity Primary Key,ProductID int,Foreign Key (ProductID) references Products(ProductID),QuantityInStock int,LastStockUpdate int)insert into Customers values('John', 'Doe', 'john.doe@example.com', 555-1234, '123 Elm St'),
('Jane', 'Smith', 'jane.smith@example.com', 555-5678, '456 Oak St'),
('Alice', 'Johnson', 'alice.j@example.com', 555-8765, '789 Pine St'),
('Bob', 'Brown', 'bob.brown@example.com', 555-4321, '101 Maple St'),
('Charlie', 'Davis', 'charlie.davis@example.com', 555-9876, '102 Cedar St'),
('David', 'Wilson', 'david.wilson@example.com', 555-1122, '222 Birch St'),
('Eva', 'Taylor', 'eva.taylor@example.com', 555-3344, '333 Walnut St'),
('Frank', 'Thomas', 'frank.thomas@example.com', 555-5566, '444 Chestnut St'),
('Grace', 'Moore', 'grace.moore@example.com', 555-7788, '555 Spruce St'),
('Harry', 'Anderson', 'harry.anderson@example.com', 555-9911, '666 Aspen St');
select * from Customers;INSERT INTO Products VALUES
('Laptop' , '15-inch display', 799),
('Smartphone' ,  '5G enabled', 599),
('Tablet', '10-inch screen', 299),
('Headphones', 'Noise-canceling', 199),
('Smartwatch', 'Fitness tracker', 149),
('Gaming Console', 'Next-gen gaming', 499),
('Wireless Mouse', 'Bluetooth mouse', 29),
('Mechanical Keyboard', 'RGB backlit', 99),
('Monitor', '27-inch 4K display', 399),
('External SSD', '1TB', 149);

select * from Products;

INSERT INTO Orders values
(1, '2024-09-01', 1500),   
(2, '2024-09-02', 2500),   
(3, '2024-09-05', 1000),   
(4, '2024-09-06', 3000),   
(1, '2024-09-07', 2200),   
(2, '2024-09-08', 1800),   
(5, '2024-09-10', 2700),   
(3, '2024-09-11', 3200);

INSERT INTO Orders values
(4, '2024-09-06', 3000);
select * from Orders;

select * from products;

select * from OrderDetails;


insert into OrderDetails values
(1, 10, 2),
(2, 9, 1),  
(3, 12, 5),  
(4, 11, 3),  
(5, 16, 4),  
(6, 15, 6),  
(7, 17, 2),  
(8, 13, 1),  
(7, 14, 8),  
(8, 18, 10); 
INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate)
VALUES 
(9, 50, 20230901),  
(10, 100, 20230902), 
(13, 200, 20230905), 
(14, 30, 20230828),  
(15, 75, 20230903),  
(16, 120, 20230910), 
(17, 60, 20230830),  
(18, 90, 20230912),  
(11, 150, 20230908), 
(12, 10, 20230911);  
select * from Inventory;


delete from OrderDetails where OrderDetailID>125;



--Queries

--1
select FirstName,LastName,Email from Customers;

--2
SELECT 
    OrderID,
    OrderDate,
    (SELECT FirstName 
     FROM Customers 
     WHERE Customers.CustomerID = Orders.CustomerID)AS Customer_Name
FROM 
    Orders;

--3
insert into Customers values ('Sherlock','Holmes','sherlock.holmes@gmail.com',NULL,'221B Baker Street');

select*from Customers;

--4

select * from Products
update Products
set Price = price*1.1;
select * from Products;

--5

declare @OrderID int = 4;

delete from OrderDetails where OrderID = @OrderID;
delete from Orders where OrderID=@OrderID;
select * from OrderDetails;

--6

insert into Orders values
(3,'2024-09-04',2500);
select* from orders;

--7

UPDATE Customers
SET 
    Email = 'raju.rastogi@gmail..com',
    Address = '221b, ST 12345'
WHERE 
    CustomerID = 10;

select*from Customers;

--8

select * from OrderDetails;
select * from Products;

select sum(p.price * o.Quantity) as order_amt, o.OrderID
from Products p, OrderDetails o 
where p.ProductID = o.ProductID
group by o.OrderID;

--9
select * from Customers;
select * from OrderDetails;
declare @CustomerID int = 4;

delete from Orders 

where CustomerID=@CustomerId;
select * from Orders;

delete from OrderDetails 
where OrderID = (select OrderID from Orders where CustomerID = @CustomerId);

--10

select * from Products;

insert into Products values
('PS5','Console',1055);

--11

Alter table Orders add Status varchar(20);




update Orders 
set Status = 'Pending';


Declare @OrderId int = 3;
update Orders
set Status = 'Shipped'
where OrderID=@OrderId;


--12

select * from Customers;
select*from Orders;
select* from OrderDetails;



SELECT C.*, 
       (SELECT COUNT(*)
        FROM Orders O 
        WHERE O.CustomerID = C.CustomerID) AS NumberOfOrders
FROM Customers C;
