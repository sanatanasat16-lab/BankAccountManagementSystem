
from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self,balance):                # constructor of the class
        super().__init__(balance)
        self.acc_type = "Current Account"
        print(f'Account Type: {self.acc_type}')  

    def calculate_interest(self):
        interest = 0
        print(f'Interest is {interest}')
        
