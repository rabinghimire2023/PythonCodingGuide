class PaymentProcessor:
    def process_payment(self, amount):
        pass

class RefundProcessor:
    def process_refund(self, amount):
        pass

class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class OnlineRefundProcessor(RefundProcessor):
    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")

def perform_payment(payment_processor, amount):
    payment_processor.process_payment(amount)

def perform_refund(refund_processor, amount):
    refund_processor.process_refund(amount)

online_payment_processor = OnlinePaymentProcessor()
online_refund_processor = OnlineRefundProcessor()

perform_payment(online_payment_processor, 100)
perform_refund(online_refund_processor, 50)
