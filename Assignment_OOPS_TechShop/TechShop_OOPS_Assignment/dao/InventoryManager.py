# InventoryManager.py

from collections import OrderedDict
from enitity.Inventory import Inventory

class InventoryManager:
    def __init__(self):
        self.inventory = OrderedDict()

    def add_to_inventory(self, product, quantity):
        if product.product_id in self.inventory:
            self.inventory[product.product_id].quantity_in_stock += quantity
        else:
            self.inventory[product.product_id] = Inventory(product, quantity)

    def update_inventory(self, product_id, new_quantity):
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory.")
        self.inventory[product_id].quantity_in_stock = new_quantity

    def get_inventory(self):
        return self.inventory
