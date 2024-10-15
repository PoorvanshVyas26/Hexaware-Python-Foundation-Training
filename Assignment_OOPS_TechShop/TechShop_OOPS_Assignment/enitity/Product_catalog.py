# ProductCatalog.py

from enitity.Products import Product

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if any(p.product_id == product.product_id for p in self.products):
            raise ValueError("Product with this ID already exists.")
        self.products.append(product)

    def update_product(self, product_id, new_name=None, new_price=None):
        product = self.find_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found.")
        if new_name:
            product.product_name = new_name
        if new_price is not None:
            if new_price < 0:
                raise ValueError("Price cannot be negative.")
            product.price = new_price

    def remove_product(self, product_id):
        product = self.find_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found.")
        self.products.remove(product)

    def find_product_by_id(self, product_id):
        return next((p for p in self.products if p.product_id == product_id), None)
