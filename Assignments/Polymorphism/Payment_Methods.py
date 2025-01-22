#Polymorphism
#Payment Methods      #Payment modes and transfer amount

class PaymentMethod:
    def process_payment(self,amount):
        raise NotImplementedError("Subclasses must implement this method")
        
class CreditCardPayment(PaymentMethod):
    def process_payment(self,amount):
        return f"Processing credit card payment of ${amount}"
        
class PayPalPayment(PaymentMethod):
    def process_payment(self,amount):
        return f"Processing PayPal payment of ${amount}"
        
class BankTransferPayment(PaymentMethod):
    def process_payment(self,amount):
        return f"Processing bank transfer payment of ${amount}"
        
#Function demonstrating polymorphism
def make_payment(payment_method,amount):
    print(payment_method.process_payment(amount))
    
#Create instances for different payment methods
credit_card=CreditCardPayment()
paypal=PayPalPayment()
bank_transfer=BankTransferPayment()

#Process payments using polymorphism
make_payment(credit_card,100)      #Output : Processing credit card payment of $100
make_payment(paypal,50)            #Output : Processing PayPal payment $50
make_payment(bank_transfer,200)    #Output : Processing bank transfer payment of $200
