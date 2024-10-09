# InvalidLoanException.py

class InvalidLoanException(Exception):
    """Exception raised when the requested loan is not found."""

    def __init__(self, message="Invalid Loan: The requested loan does not exist"):
        self.message = message
        super().__init__(self.message)

# DatabaseException.py

class DatabaseException(Exception):
    """Exception raised for errors that occur during database operations."""

    def __init__(self, message="Database Error: An error occurred while accessing the database"):
        self.message = message
        super().__init__(self.message)
