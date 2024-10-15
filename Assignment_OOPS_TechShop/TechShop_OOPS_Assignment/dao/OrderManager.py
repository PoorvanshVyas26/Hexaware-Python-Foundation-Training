# OrderManager.py

from enitity.Orders import Order

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def update_order_status(self, order_id, new_status):
        order = self.find_order_by_id(order_id)
        if not order:
            raise ValueError("Order not found.")
        order.status = new_status

    def remove_order(self, order_id):
        order = self.find_order_by_id(order_id)
        if not order:
            raise ValueError("Order not found.")
        if order.status == 'Cancelled':
            self.orders.remove(order)

    def find_order_by_id(self, order_id):
        return next((o for o in self.orders if o.order_id == order_id), None)
    
    def sort_orders_by_date(self, ascending=True):
        self.orders = sorted(self.orders, key=lambda o: o.order_date, reverse=not ascending)
