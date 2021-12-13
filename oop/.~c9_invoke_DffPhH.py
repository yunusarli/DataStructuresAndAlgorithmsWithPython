import math

class CreditCard:
    def __init__(self,customer,bank,acnt,limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt#account number
        self._limit = limit
        self._balance = 0

    def get_limit(self):
        return self._limit

    def get_customer(self):
        return self._customer

    def get_account(self):
        return self._acnt

    def get_bank(self):
        return self._bank

    def get_balance(self):
        return self._balance

    def charge(self,price):

        if price + self.get_balance() > self.get_limit():
            return False
        else:
            self._balance += price

    def make_payment(self,amount):
        assert amount < self.get_balance(), "The amount you want to pay is more than your debt"

        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    def __init__(self,*args,apr):
        super().__init__(*args)
        self._apr = apr

    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += self.OVERLIMIT_FEE
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = math.pow(1+self._apr,1/12)
            self._balance *= monthly_factor

#a class for testing class data members
class Example(PredatoryCreditCard):
    #class data members
    OVERLIMIT_FEE = 10
    

if __name__ == "__main__":
    wallet = list()
    wallet.append(Example('yunus arli','ziraat bankası','4242 4242 4422 5252',1400,apr=0.082))
    wallet.append(Example('yunus arli','ziraat bankası','4242 4242 4422 5252',1800,apr=0.082))
    wallet.append(Example('yunus arli','ziraat bankası','4242 4242 4422 5252',700,apr=0.082))

    for val in range(17):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)

    for c in range(3):
        print(" Customer = ", wallet[c].get_customer())
        print(" Bank =" , wallet[c].get_bank())
        print(" Account =" , wallet[c].get_account())
        print(" Limit =" , wallet[c].get_limit())
        print(" Balance =" , wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =" , wallet[c].get_balance())
            print()
            
            