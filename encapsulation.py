class bank:

    # CONSTRUCTOR: automatically called when object is created
    def __init__(self):
        # Double underscore __ make it private (name)
        self.__balance = 5000
    
    # Create the methid to deposit money into the account
    def deposit(self, amount):
        self.__balance += amount
    
    # Display the current balance
    def show_balance(self):
        print(self.__balance)


# Create a object  (instance) of the bank class 

b = bank()
b.deposit(6432)
b.show_balance()