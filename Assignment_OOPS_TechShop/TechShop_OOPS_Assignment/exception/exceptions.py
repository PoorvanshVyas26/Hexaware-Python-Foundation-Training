
class InvalidDataException(Exception):
    """Exception raised for invalid data input."""
    def __init__(self, message):
        super().__init__(message)

class InsufficientStockException(Exception):
    """Exception raised when there is insufficient stock for a product."""
    def __init__(self, message):
        super().__init__(message)

class IncompleteOrderException(Exception):
    """Exception raised for incomplete order details."""
    def __init__(self, message):
        super().__init__(message)

class PaymentFailedException(Exception):
    """Exception raised for failed payment transactions."""
    def __init__(self, message):
        super().__init__(message)

class IOException(Exception):
    """Exception raised for input/output errors."""
    def __init__(self, message):
        super().__init__(message)

class SqlException(Exception):
    """Exception raised for SQL related errors."""
    def __init__(self, message):
        super().__init__(message)

class ConcurrencyException(Exception):
    """Exception raised for concurrency control issues."""
    def __init__(self, message):
        super().__init__(message)

class AuthenticationException(Exception):
    """Exception raised for authentication failures."""
    def __init__(self, message):
        super().__init__(message)

class AuthorizationException(Exception):
    """Exception raised for authorization failures."""
    def __init__(self, message):
        super().__init__(message)
