
from BankAccount import BankAccount         # first BankAccount is the name of the file and second BankAccount is the name of the class

class SavingsAccount(BankAccount):
    def __init__(self,balance):                # constructor of the class
        super().__init__(balance)
        self.acc_type = "Savings Account"
        print(f'Account Type: {self.acc_type}')

    def calculate_interest(self):                 # implementation of the abstract method
        interest = self.balance * (5/100)
        print(f'Interest is {interest}')
        

# savings_account = SavingsAccount("John",1000)
