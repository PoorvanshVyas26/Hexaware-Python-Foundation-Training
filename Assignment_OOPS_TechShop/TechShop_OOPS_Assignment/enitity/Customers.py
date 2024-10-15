import re
from exception.exceptions import InvalidDataException
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__total_orders = 0  # Initialize total orders
       # self.__is_admin = is_admin

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def address(self):
        return self.__address
    
    @property
    def is_admin(self):
        return self.__is_admin

    def calculate_total_orders(self):
        return self.__total_orders

    def get_customer_details(self):
        return {
            "CustomerID": self.__customer_id,
            "FirstName": self.__first_name,
            "LastName": self.__last_name,
            "Email": self.__email,
            "Phone": self.__phone,
            "Address": self.__address,
            "TotalOrders": self.__total_orders,
           # "IsAdmin": self.is_admin,
        }

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.__email = email
        if phone:
            self.__phone = phone
        if address:
            self.__address = address

    
    
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise InvalidDataException("Invalid email address format.")

    def register_customer(self, first_name, last_name, email, phone, address):
        self.validate_email(email)