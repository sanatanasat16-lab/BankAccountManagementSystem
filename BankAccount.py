from abc import ABC, abstractmethod

# creating a class as an abstract class
# we cannot cerate an object of an abstract class 

class BankAccount(ABC):
    def __init__(self,balance):                # constructor of the class 
        self.__balance = balance                # we can also give self.__balance = 0 as default value

    def display_balance(self):               # method to display the balance 
        print(f'Account Balance is {self.__balance}')    # displaying a private information 

    @property
    def balance(self):                     # to return the balance amount 
        return self.__balance              # so that we can access ths balance amount n the chld classes. ie,self.balance

    @balance.setter
    def balance(self,amount):

        if type(amount)==str:
                    print("Invalid input. Please enter a valid number.")
        
        elif amount < 0:            # if the amount is less than 0 then raise an exception
            print ("Balance cannot be negative")
        
        else:
            self.__balance = amount
            print(f'Balance is updated to {amount}')

    def deposite(self,amount):

        if type(amount) == str:
            print("Invalid input. Please enter a valid number.")
        
        elif amount > 0:
            self.__balance = self.__balance + amount
            print(f'Deposite is successful and your balance is {self.__balance}')
        else:
            print("Deposite amount should be greater than 0") 


    def withdraw(self,amount):
        
        if type(amount) == str:
            print("Invalid input. Please enter a valid number.")
        
        elif amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f'Withdraw is successful and your balance is {self.__balance}')

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            print("Withdraw amount should be greater than 0")

    @abstractmethod                           # creating an abstract method called calculate_interest
    def calculate_interest(self):             # this method should be implemented in the child classes strictly
        pass


# bank_account = BankAccount(1000)
# bank_account.display_balance()
# bank_account.deposite(100)
# bank_account.withdraw(-50)




