from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount:.2f}")

if __name__ == "__main__":
    # Example usage
    credit_card_payment = CreditCardPayment()
    credit_card_payment.process_payment(100)
    upi_payment = UPIPayment()
    upi_payment.process_payment(50)