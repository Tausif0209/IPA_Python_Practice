from abc import ABC,abstractmethod
class BankAccount(ABC):
  def __init__(self,customer_name,date_of_birth,acc_number,curr_balance):
    self.__customer_name=customer_name
    self.__date_of_birth=date_of_birth
    self.__acc_number=acc_number
    self.__cur_balance=curr_balance
  @abstractmethod
  def deposit(self,amount):
    pass

  @abstractmethod
  def withdraw(self,amount):
    pass

  def get_balance(self):
    return self.__cur_balance
  
  def _set_balance(self,newVal):
    self.__cur_balance=newVal
  
  def display_details(self):
    print(f"customer_name:{self.__customer_name}\nAccount number:-{self.__acc_number}\nCurrent Balance:-{self.__cur_balance}")


class SavingAccount(BankAccount):
  min_balance=100
  def deposit(self, amount):
    curr_balance=self.get_balance()
    new_val=curr_balance+amount
    self._set_balance(new_val)
  def withdraw(self, amount):
    curr_balance=self.get_balance()
    if curr_balance-amount<=self.min_balance:print("Balance Insufficient")
    else:self._set_balance(curr_balance-amount)
  
customer1=SavingAccount("Tausif Iqbal","09-04-2002","101",100)
customer1.deposit(50)
customer1.display_details()
customer1.withdraw(5)
customer1.display_details()

  
class CurrentAccount(BankAccount):
    overdraft_limit = 500
    def deposit(self, amount):
        self._set_balance(self.get_balance() + amount)
        print("Deposited:", amount)
    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            self._set_balance(self.get_balance() - amount)
            print("Withdrawn:", amount)
        else:
            print("Overdraft limit exceeded")

customer2 = CurrentAccount("Iqbal", "01-01-2000", 102, 1000)
customer2.withdraw(1800)
customer2.display_details()