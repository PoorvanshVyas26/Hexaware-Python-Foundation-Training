
import sys
import os

# Get the absolute path of the root project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.databaseconnector import DBUtil
import pyodbc

class DAOImpl:
    def __init__(self):
        self.conn = DBUtil.getDBConn()
        if self.conn:
            self.cursor = self.conn.cursor()
        else:
            self.cursor = None
            raise Exception("Database connection could not be established.")

    # Customers CRUD operations
    def create_customer(self,FirstName,LastName, Email, Phone):
        try:
            sql = '''INSERT INTO Customers (FirstName,LastName, Email, Phone)
                     VALUES ( ?, ?, ?, ?)'''
            self.cursor.execute(sql, FirstName,LastName, Email, Phone)
            self.conn.commit()
            print(f"Customer created successfully!")
        except pyodbc.Error as e:
            print(f"Error creating customer: {e}")
            self.conn.rollback()

    def read_customer(self, CustomerID):
        try:
            sql = "SELECT * FROM Customers WHERE CustomerID = ?"
            self.cursor.execute(sql, CustomerID)
            customer = self.cursor.fetchone()
            if customer:
                print(f"Customer found: {customer}")
            else:
                print("Customer not found.")
            return customer
        except pyodbc.Error as e:
            print(f"Error reading customer: {e}")

    def update_customer(self, Email, Phone, Address, CustomerID):
        try:
            sql = '''UPDATE Customers 
                     SET  Email = ?, Phone = ?, Address = ? 
                     WHERE CustomerID = ?'''
            self.cursor.execute(sql, Email, Phone, Address,CustomerID)
            self.conn.commit()
            print(f"Customer updated successfully!")
        except pyodbc.Error as e:
            print(f"Error updating customer: {e}")
            self.conn.rollback()

    def delete_customer(self, CustomerID):
        try:
            sql = "DELETE FROM Customers WHERE CustomerID = ?"
            self.cursor.execute(sql, CustomerID)
            self.conn.commit()
            print(f"Customer deleted successfully!")
        except pyodbc.Error as e:
            print(f"Error deleting customer: {e}")
            self.conn.rollback()

    # Products CRUD operations
    def create_product(self, ProductName, Description, Price ):
        try:
            sql = '''INSERT INTO Products (ProductName, Description, Price)
                     VALUES (?, ?, ?)'''
            self.cursor.execute(sql, ProductName, Description, Price)
            self.conn.commit()
            print(f"Product created successfully!")
        except pyodbc.Error as e:
            print(f"Error creating product: {e}")
            self.conn.rollback()

    def read_product(self, product_id):
        try:
            sql = "SELECT * FROM Products WHERE ProductID = ?"
            self.cursor.execute(sql, product_id)
            product = self.cursor.fetchone()
            if product:
                print(f"Product found: {product}")
            else:
                print("Product not found.")
            return product
        except pyodbc.Error as e:
            print(f"Error reading product: {e}")

    def update_product(self, ProductID, ProductName, Price):
        try:
            sql = '''UPDATE Products 
                     SET ProductName = ?, Price = ? 
                     WHERE ProductID = ?'''
            self.cursor.execute(sql, ProductName, Price, ProductID)
            self.conn.commit()
            print(f"Product  updated successfully!")
        except pyodbc.Error as e:
            print(f"Error updating product: {e}")
            self.conn.rollback()

    def delete_product(self, ProductID):
        try:
            sql = "DELETE FROM Products WHERE ProductID = ?"
            self.cursor.execute(sql, ProductID)
            self.conn.commit()
            print(f"Product deleted successfully!")
        except pyodbc.Error as e:
            print(f"Error deleting product: {e}")
            self.conn.rollback()

    # Orders CRUD operations
    def create_order(self,CustomerID, OrderDate, Status, TotalAmount ):
        try:
            sql = '''INSERT INTO Orders (CustomerID, OrderDate, Status, TotalAmount)
                     VALUES (?, ?, ?, ?)'''
            self.cursor.execute(sql, CustomerID, OrderDate, Status, TotalAmount)
            self.conn.commit()
            print(f"Order created successfully!")
        except pyodbc.Error as e:
            print(f"Error creating order: {e}")
            self.conn.rollback()

    def read_order(self, OrderID):
        try:
            sql = "SELECT * FROM Orders WHERE OrderID = ?"
            self.cursor.execute(sql, OrderID)
            order = self.cursor.fetchone()
            if order:
                print(f"Order found: {order}")
            else:
                print("Order not found.")
            return order
        except pyodbc.Error as e:
            print(f"Error reading order: {e}")

    def update_order(self, OrderID, Status, TotalAmount):
        try:
            sql = '''UPDATE Orders 
                     SET Status = ?, TotalAmount = ? 
                     WHERE OrderID = ?'''
            self.cursor.execute(sql, OrderID, Status, TotalAmount)
            self.conn.commit()
            print(f"Order updated successfully!")
        except pyodbc.Error as e:
            print(f"Error updating order: {e}")
            self.conn.rollback()

    def delete_order(self, OrderID):
        try:
            sql = "DELETE FROM Orders WHERE OrderID = ?"
            self.cursor.execute(sql, OrderID )
            self.conn.commit()
            print(f"Order deleted successfully!")
        except pyodbc.Error as e:
            print(f"Error deleting order: {e}")
            self.conn.rollback()

    # OrderDetails CRUD operations
    def create_order_detail(self, OrderID, ProductID, Quantity):
        try:
            sql = '''INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
                     VALUES (?, ?, ?, ?)'''
            self.cursor.execute(sql, OrderID, ProductID, Quantity)
            self.conn.commit()
            print(f"Order Detail for Order ID created successfully!")
        except pyodbc.Error as e:
            print(f"Error creating order detail: {e}")
            self.conn.rollback()

    def read_order_detail(self, OrderID):
        try:
            sql = "SELECT * FROM OrderDetails WHERE OrderID = ?"
            self.cursor.execute(sql, OrderID)
            order_detail = self.cursor.fetchone()
            if order_detail:
                print(f"Order Detail found: {order_detail}")
            else:
                print("Order Detail not found.")
            return order_detail
        except pyodbc.Error as e:
            print(f"Error reading order detail: {e}")

    def update_order_detail(self, OrderDetailID, Quantity):
        try:
            sql = '''UPDATE OrderDetails 
                     SET Quantity = ?
                     WHERE OrderDetailID = ?'''
            self.cursor.execute(sql, OrderDetailID, Quantity)
            self.conn.commit()
            print(f"Order Detail updated successfully!")
        except pyodbc.Error as e:
            print(f"Error updating order detail: {e}")
            self.conn.rollback()

    def delete_order_detail(self, OrderDetailID):
        try:
            sql = "DELETE FROM OrderDetails WHERE order_detail_id = ?"
            self.cursor.execute(sql, OrderDetailID)
            self.conn.commit()
            print(f"Order Detail deleted successfully!")
        except pyodbc.Error as e:
            print(f"Error deleting order detail: {e}")
            self.conn.rollback()

    def track_order_status(self, order_id):
        try:
            sql = '''SELECT Status FROM Orders WHERE OrderID = ?'''
            self.cursor.execute(sql, order_id)
            status = self.cursor.fetchone()
            if status:
                print(f"Order: {order_id} Status: {status[0]}")
            else:
                print(f"No order found with ID: {order_id}")
            return status
        except pyodbc.Error as e:
            print(f"Error tracking order status: {e}")


    # Inventory CRUD operations
    def create_inventory_item(self, ProductID, QuantityInStock):
        try:
            sql = '''INSERT INTO Inventory (ProductID, QuantityInStock)
                     VALUES (?, ?)'''
            self.cursor.execute(sql, ProductID, QuantityInStock)
            self.conn.commit()
            print(f"Inventory item for Product ID created successfully!")
        except pyodbc.Error as e:
            print(f"Error creating inventory item: {e}")
            self.conn.rollback()

    def read_inventory_item(self, ProductID):
        try:
            sql = "SELECT * FROM Inventory WHERE ProductID = ?"
            self.cursor.execute(sql, ProductID)
            inventory_item = self.cursor.fetchone()
            if inventory_item:
                print(f"Inventory item found: {inventory_item}")
            else:
                print("Inventory item not found.")
            return inventory_item
        except pyodbc.Error as e:
            print(f"Error reading inventory item: {e}")

    def update_inventory_item(self, QuantityInStock, ProductID):
        try:
            sql = '''UPDATE Inventory 
                     SET QuantityInStock = ? 
                     WHERE ProductID = ?'''
            self.cursor.execute(sql, QuantityInStock, ProductID)
            self.conn.commit()
            print(f"Inventory for Product ID updated successfully!")
        except pyodbc.Error as e:
            print(f"Error updating inventory: {e}")
            self.conn.rollback()

    def delete_inventory_item(self, ProductID):
        try:
            sql = "DELETE FROM Inventory WHERE ProductID = ?"
            self.cursor.execute(sql, ProductID)
            self.conn.commit()
            print(f"Inventory item for Product ID deleted successfully!")
        except pyodbc.Error as e:
            print(f"Error deleting inventory item: {e}")
            self.conn.rollback()

    # Close the connection
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database connection closed.")




# def main():
#     dao = DAOImpl()  # Create an instance of DAOImpl

#     # Create a new customer
#     #new_prod = Customer(name="John Doe", email="john.doe@example.com", phone="1234567890")
    
#     # Call the create_customer method

   
#     dao.update_inventory_item(125,12)
    
#     # Close the DAO connection
#     dao.close()

# if __name__ == "__main__":
#     main()















































    