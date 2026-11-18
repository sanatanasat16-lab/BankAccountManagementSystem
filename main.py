
from CurrentAccount import CurrentAccount

# create  an object of current account

ca1 = CurrentAccount(1000)
ca1.deposite(5000000)
ca1.withdraw(1000)
ca1.display_balance()
ca1.calculate_interest()

from SavingsAccount import SavingsAccount

ca2 = SavingsAccount(100000)
ca2.deposite(50000)
ca2.withdraw(20000)
ca2.calculate_interest()
ca2.display_balance()


# from SimpleAccount import SimpleAccount

# # sim_acc1 = SimpleAccount()
# # sim_acc1.method1()

# # from BankAccount import BankAccount

# # bankAcc1 =  BankAccount(0)
# # bankAcc1.deposite()      # it will not work because BankAccount is an abstract class and we cannot create an object of an abstract class

# from SavingsAccount import SavingsAccount

# ca2 = SavingsAccount(1000)
# ca2.calculate_interest()
# ca2.display_balance()
# ca2.deposite('500')
