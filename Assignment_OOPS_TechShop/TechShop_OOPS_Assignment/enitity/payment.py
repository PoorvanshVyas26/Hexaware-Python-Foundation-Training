# entity/Payment.py

class Payment:
    def __init__(self, payment_id, order_id, amount, status):
        self.__payment_id = payment_id
        self.__order_id = order_id
        self.__amount = amount
        self.__status = status

    @property
    def payment_id(self):
        return self.__payment_id

    @property
    def order_id(self):
        return self.__order_id

    @property
    def amount(self):
        return self.__amount

    @property
    def status(self):
        return self.__status

    def update_status(self, new_status):
        self.__status = new_status

    def get_payment_info(self):
        return {
            "PaymentID": self.__payment_id,
            "OrderID": self.__order_id,
            "Amount": self.__amount,
            "Status": self.__status
        }
