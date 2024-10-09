
import pyodbc


class DBUtil():
    print("Starting...")

    def __init__(self):
        pass

    @staticmethod
    def getDBConn():
        print("Connecting...")
        """
        Establish a connection to the MySQL database and return the Connection reference.
        Raises DatabaseException if connection fails.
        """
        try:
            print("trying...")
            
            conn = pyodbc.connect(driver = '{SQL Server}',
                server='LAPTOP-V5IQ580M',
                database='loan_management_system',
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

