# Existing System Interface
class PaymentProcessor:
    def process_payment(self, amount: float):
        raise NotImplementedError("Subclasses should implement this method")


# Current Payment Gateway(Adaptee)
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount} payment through PayPal.")


class StripeAPI:
    def make_payment(self, amount: float):
        print(f"Processing ${amount} payment through Stripe.")


# Stripe Adapter
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_api: StripeAPI):
        self.stripe_api = stripe_api

    def process_payment(self, amount: float):
        # Adapting the call to the new interface
        self.stripe_api.make_payment(amount)

#Client

def checkout(payment_processor :PaymentProcessor,amount:float):
    payment_processor.process_payment(amount)

#Usage
paypal_processor = PayPalProcessor()
stripe_processor  = StripeAdapter(StripeAPI())

# Process payment through PayPal
checkout(paypal_processor,150)

# Process payment through Stripe
checkout(stripe_processor,150)
