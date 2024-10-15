from exception.exceptions import InsufficientStockException
from enitity.Products import Product

class Inventory:
    def __init__(self, inventory_id, product: Product, quantity_in_stock):
        self.__inventory_id = inventory_id
        self.__product = product  # Composition relationship with Product
        self.__quantity_in_stock = quantity_in_stock

    @property
    def product(self):
        return self.__product  # Access to Product object

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_product(self):
        return self.__product

    def add_to_inventory(self, quantity):
        if quantity > 0:
            self.__quantity_in_stock += quantity

    def remove_from_inventory(self, quantity):
        if 0 < quantity <= self.__quantity_in_stock:
            self.__quantity_in_stock -= quantity

    def update_stock_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.__quantity_in_stock = new_quantity

    def is_product_available(self, quantity_to_check):
        return self.__quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.__product.price * self.__quantity_in_stock

    def list_low_stock_products(self, threshold):
        return self.__quantity_in_stock < threshold

    def list_out_of_stock_products(self):
        return self.__quantity_in_stock == 0

    def list_all_products(self):
        return {
            "Product": self.__product.get_product_details(),
            "QuantityInStock": self.__quantity_in_stock
        }
    
    
    def remove_from_inventory(self, quantity):
        if quantity > self.__quantity_in_stock:
            raise InsufficientStockException("Insufficient stock to fulfill the order.")
        self.__quantity_in_stock -= quantity

