import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.databaseconnector import DBUtil
import pyodbc


from dao.TechshopIMPL import DAOImpl
from enitity.Customers import Customer
from dao.paymentmanager import PaymentManager

def main_menu():
    print("1. Add Customer")
    print("2. Update Customers")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Place order")
    print("6. Track Order Status")
    print("7. Payment Processing")
    print("8. Delete Product")
    print("9. Search Products by ID")
    print("10. Exit")

def main():
    dao = DAOImpl()  # Initialize the DAOImpl class to handle all DB interactions
    payment_manager = PaymentManager() #initializing the payment manager class for payment processing

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            FirstName = input("Enter First Name: ")
            LastName = input("Enter Last Name: ")
            Email = input("Enter Email: ")
            Phone = input("Enter Phone: ")
            dao.create_customer(FirstName, LastName, Email, Phone)

        elif choice == '2':
            # Update Customers
            CustomerID = input("Enter Customer ID to update: ")
            Email = input("Enter new Email: ")
            Phone = input("Enter new Phone: ")
            Address = input("Enter new Address: ")
        
            dao.update_customer(Email, Phone, Address, CustomerID)




        elif choice == '3':
            # Add Product
            
            ProductName = input("Enter Product Name: ")
            Description = input("Enter Product Description: ")
            try:
                Price = float(input("Enter Product Price: "))
                if Price < 0:
                    raise ValueError("Price cannot be negative.")
            except ValueError as e:
                print(e)
                return
            dao.create_product( ProductName, Description, Price)

        elif choice == '4':
            # Update Product
            # Prompt user for product details
            ProductID = input("Enter Product ID to update: ")

            # Check if product exists before updating
            product = dao.read_product(ProductID)  # Make sure this method is defined in your DAO
            if not product:
                print("Product not found.")
                continue

            ProductName = input("Enter new Product Name: ")

            try:
                Price = float(input("Enter new Product Price: "))
                if Price < 0:
                    raise ValueError("Price cannot be negative.")
            except ValueError as e:
                print(e)
                continue

            # Call the update method with correct argument order
            dao.update_product(ProductID, ProductName, Price)
            print("Product updated successfully!")



        elif choice == '5':
            # Place Order
            CustomerID = input("Enter customer ID: ")
            OrderDate = input("Enter order date (YYYY-MM-DD): ")
            Status = input("Enter order status: ")
            TotalAmount = float(input("Enter order total: "))
            dao.create_order(CustomerID, OrderDate, Status, TotalAmount)
            #CustomerID, OrderDate, Status, TotalAmount


        elif choice == '6':
            # Track Order Status
            order_id = input("Enter order ID to track status: ")
            dao.track_order_status(order_id)


        elif choice == '7':
            # Payment Processing
            order_id = input("Enter order ID: ")
            amount = float(input("Enter payment amount: "))
            payment_manager.process_payment(order_id, amount)


        elif choice == '8':
            # Delete Product
            product_id = input("Enter product ID: ")
            dao.delete_product(product_id)

        elif choice == '9':
            # Search Products 
            product_id = input("Enter product ID: ")
            dao.read_product(product_id)
  


        elif choice == '10':
            # Exit
            print("Exiting...")
            dao.close()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
