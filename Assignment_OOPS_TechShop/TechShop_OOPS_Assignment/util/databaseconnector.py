
import pyodbc


class DBUtil():
    print("Starting...")

    def __init__(self):
        pass

    @staticmethod
    def getDBConn():
        print("Connecting...")
        """
        Establish a connection to the database and return the Connection reference.
        Raises DatabaseException if connection fails.
        """
        try:
            print("trying...")
            
            conn = pyodbc.connect(driver = '{SQL Server}',
                server='LAPTOP-V5IQ580M',
                database='TECHSHOP',
                Trusted_Connection='yes'
            )
            print(conn)

            print("Connected Succesfully")
        
            return conn
        
        except pyodbc.InterfaceError as ie:
            print("Driver not found or not installed correctly.")
        except pyodbc.DatabaseError as de:
            print(f"Database error: {de}")
        except Exception as e:
            print(f"Connection failed: {str(e)}")
        return None

# if __name__ == "__main__":
#     connection = DBUtil.getDBConn()
#     if connection:
#         print("Connection established.")
#     else:
#         print("Failed to connect to the database.")