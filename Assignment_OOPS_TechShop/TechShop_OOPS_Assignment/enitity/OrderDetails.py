# order_detail.py
from enitity.Orders import Order
from enitity.Products import Product
from enitity.Inventory import Inventory
from exception.exceptions import ProductUnavailableException
from exception.exceptions import InsufficientStockException

class OrderDetail:
    def __init__(self, order_detail_id, order: Order, product: Product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order  # Composition relationship with Order
        self.__product = product  # Composition relationship with Product
        self.__quantity = quantity

    @property
    def order(self):
        return self.__order  # Access to Order object

    @property
    def product(self):
        return self.__product  # Access to Product object

    @property
    def quantity(self):
        return self.__quantity

    def calculate_subtotal(self):
        return self.__product.price * self.__quantity

    def get_order_detail_info(self):
        return {
            "OrderDetailID": self.__order_detail_id,
            "OrderID": self.__order.order_id,
            "Product": self.__product.get_product_details(),
            "Quantity": self.__quantity,
            "Subtotal": self.calculate_subtotal()
        }

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.__quantity = new_quantity

    def add_discount(self, discount_amount):
        # Logic to apply a discount
        pass


    def __validate_product_availability(self):
        """Validate if the product is available and has sufficient stock in the inventory."""
        # Check if the product exists in inventory
        inventory = Inventory.get_inventory_by_product_id(self.__product.product_id)
        if not inventory:
            raise ProductUnavailableException(f"Product ID {self.__product.product_id} is unavailable in the inventory.")
        
        # Check if sufficient stock is available
        if inventory.quantity < self.__quantity:
            raise InsufficientStockException(f"Only {inventory.quantity} units of product ID {self.__product.product_id} are available.")
        
        # If validation passes, deduct the stock
        inventory.update_stock(-self.__quantity)

    def get_order_details(self):
        """Retrieve details about the order."""
        return {
            "OrderID": self.__order.order_id,
            "ProductID": self.__product.product_id,
            "ProductName": self.__product.name,
            "Quantity": self.__quantity
        }