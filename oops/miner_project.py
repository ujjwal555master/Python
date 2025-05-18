# Create a atm functionality prototype

class Atm:
    serialNo = 0   #static varible access without an object
    def __init__(self, name):
        self.name = name
        self.__balance = 1000 #1000 for reward new user #for hide the variable
        self.pin = 0
        print("create a pin")
        self.create_pin()

    def check_balance(self):
        print(self.__balance)

    def create_pin(self):
        pins = int(input("Enter pin number"))
        self.pin = pins
        print("pin", pins)
    # for private the method
    def __credit_money(self, money):
        self.__balance = self.balance + money

    def debt_money(self, money):
        self.__balance = self.balance - money

    @staticmethod
    def greet():
        print("hello")
        print(Atm.serialNo)   #for access the variable



