create database loan_management_system;

use loan_management_system;


CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    email_address VARCHAR(60),
    phone_number VARCHAR(15),
    address VARCHAR(150),
    credit_score INT
);


CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    principal_amount Decimal(10, 2),
    interest_rate INT,
    loan_term INT,
    loan_type VARCHAR(20),
    loan_status VARCHAR(20)    
);


INSERT INTO Customer VALUES
(1,'John Doe', 'johndoe@gmail.com', '123-456-7890', '123 Maple Street, New York, NY', 750),
(2,'Jane Smith', 'janesmith@yahoo.com', '234-567-8901', '456 Oak Avenue, Los Angeles, CA', 680),
(3,'Michael Brown', 'michael.b@gmail.com', '345-678-9012', '789 Pine Drive, Chicago, IL', 720),
(4,'Emily Davis', 'emily.davis@hotmail.com', '456-789-0123', '101 Birch Lane, Houston, TX', 800),
(5,'Chris Johnson', 'cjohnson@outlook.com', '567-890-1234', '202 Cedar Street, Miami, FL', 690),
(6,'Anna Wilson', 'anna.w@gmail.com', '678-901-2345', '303 Spruce Avenue, Seattle, WA', 710),
(7,'David Clark', 'davidc@yahoo.com', '789-012-3456', '404 Willow Road, Denver, CO', 765),
(8,'Sophia Martinez', 'sophia.martinez@gmail.com', '890-123-4567', '505 Fir Court, Boston, MA', 780),
(9,'James Lee', 'jameslee@hotmail.com', '901-234-5678', '606 Redwood Circle, San Francisco, CA', 820),
(10,'Olivia Taylor', 'olivia.t@gmail.com', '012-345-6789', '707 Elm Street, Dallas, TX', 690);

    
    
INSERT INTO Loan VALUES
	(1,7, 500000, 8, 36, 'CarLoan', 'Approved'),
	(2,2, 1000000, 7, 60, 'HomeLoan', 'Pending'),
	(3,6, 300000, 9, 24, 'CarLoan', 'Approved'),
	(4,4, 800000, 6, 48, 'HomeLoan', 'Approved'),
	(5,5, 700000, 8, 36, 'CarLoan', 'Approved'),
	(6,1, 1200000, 7, 60, 'HomeLoan', 'Pending'),
	(7,2, 400000, 9, 24, 'CarLoan', 'Approved'),
	(8,8, 900000, 6, 48, 'HomeLoan', 'Pending'),
	(9,9, 600000, 8, 36, 'CarLoan', 'Pending'),
	(10,10, 1100000, 7, 60, 'HomeLoan', 'Pending'),
	(11,3, 350000, 9, 24, 'CarLoan', 'Approved'),
	(12,4, 750000, 6, 48, 'CarLoan', 'Approved');

select * from Customer;