from enitity.payment import Payment
from exception.exceptions import PaymentFailedException
import random

class PaymentManager:
    def __init__(self):
        self.payments = []  # This will hold a list of Payment objects
        self.max_retries = 3  # Set a limit for payment retries

    def process_payment(self, order_id, amount):
        payment_id = len(self.payments) + 1  # Generate a simple payment ID
        payment = Payment(payment_id, order_id, amount, "Pending")

        for attempt in range(self.max_retries):
            try:
                self._attempt_payment(payment)
                payment.update_status("Completed")  # Update status on success
                self.payments.append(payment)  # Save the successful payment
                print("Payment processed successfully.")
                return True  # Payment successful
            except PaymentFailedException as e:
                payment.update_status("Failed")  # Update status on failure
                print(f"Attempt {attempt + 1}: {e}")
                if attempt == self.max_retries - 1:
                    print("Max retry limit reached. Payment failed.")
                    return False  # Payment failed after retries

    def _attempt_payment(self, payment):
        # Simulate a failure scenario for negative amounts or 0 amounts
        if payment.amount <= 0:
            raise PaymentFailedException("Payment amount must be greater than zero.")
        
        # Simulate random payment processing failure
        if random.choice([True, False]):  # Randomly decide if payment fails
            raise PaymentFailedException("Payment processing failed.")

    def retry_payment(self, payment_id):
        payment = self.get_payment(payment_id)
        if payment and payment.status == "Failed":
            return self.process_payment(payment.order_id, payment.amount)
        else:
            print("No failed payment found for retry.")
            return False

    def cancel_payment(self, payment_id):
        payment = self.get_payment(payment_id)
        if payment and payment.status == "Failed":
            payment.update_status("Cancelled")
            print(f"Payment ID {payment_id} cancelled successfully.")
            return True
        else:
            print("Payment cannot be cancelled as it is not failed or does not exist.")
            return False

    def get_payment(self, payment_id):
        for payment in self.payments:
            if payment.payment_id == payment_id:
                return payment
        return None  # Payment not found

    def list_payments(self):
        return [payment.get_payment_info() for payment in self.payments]

    def update_payment_status(self, payment_id, new_status):
        payment = self.get_payment(payment_id)
        if payment:
            payment.update_status(new_status)
            return True
        return False
