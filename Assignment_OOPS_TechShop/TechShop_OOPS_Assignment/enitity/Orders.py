from exception.exceptions import IncompleteOrderException
from exception.exceptions import ConcurrencyException

from enitity.Customers import Customer
from enitity.OrderDetails import OrderDetail

class Order:
    def __init__(self, order_id, customer: Customer):
        self.__order_id = order_id
        self.__customer = customer  # Composition relationship
        self.__order_details = []
        self.__order_date = None  # Initialize order date
        self.__total_amount = 0.0

    @property
    def order_id(self):
        return self.__order_id

    @property
    def customer(self):
        return self.__customer  # Access to Customer object

    def calculate_total_amount(self):
        self.__total_amount = sum(detail.calculate_subtotal() for detail in self.__order_details)
        return self.__total_amount

    def get_order_details(self):
        return {
            "OrderID": self.__order_id,
            "Customer": self.__customer.get_customer_details(),
            "OrderDetails": [detail.get_order_detail_info() for detail in self.__order_details],
            "TotalAmount": self.__total_amount
        }

    def update_order_status(self, status):
        self.__order_status = status

    def cancel_order(self):
        # Logic to cancel the order and adjust stock levels for products
        pass
     
    def version(self):
        return self.__version

    def update_order(self, new_total_amount, current_version):
        # Check if the version matches the current version
        if self.__version != current_version:
            raise ConcurrencyException("Order was updated by another user. Please retry.")
        
        # If the version matches, proceed with update
        self.__total_amount = new_total_amount
        
        # Increment the version number after a successful update
        self.__version += 1




    def process_order(self):
        if not self.__order_details:  # Assuming this is a list of order details
            raise IncompleteOrderException("Order details are incomplete.")
        
 