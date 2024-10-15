# product.py
class Product:
    def __init__(self, product_id, product_name, description, price, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price
        self.__quantity_in_stock = quantity_in_stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock

    def get_product_details(self):
        return {
            "ProductID": self.__product_id,
            "ProductName": self.__product_name,
            "Description": self.__description,
            "Price": self.__price,
            "QuantityInStock": self.__quantity_in_stock
        }

    def update_product_info(self, price=None, description=None):
        if price is not None and price >= 0:
            self.__price = price
        if description:
            self.__description = description

    def is_product_in_stock(self):
        return self.__quantity_in_stock > 0
