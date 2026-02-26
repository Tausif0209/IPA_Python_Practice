class Bank:
  bname="union bank"
  bbranch=["Mango,dimna"]
  btiming="9am to 6pm"
  bloc="kol"
  # def set_details(self,name,age,profession):
  #   self.name=name
  #   self.age=age
  #   self.profession=profession
  def __init__(self,name,age,profession,balance):
    self.name=name
    self.age=age
    self.profession=profession
    self.balance=balance
  def withdraw(self):
    amt=int(input("Enter amount to withdraw"))
    if(amt<0):print("Error Negative value")
    elif self.balance<amt:print("Balance insufficient")
    else:self.balance-=amt
    print(f"updated balance:-{self.balance}")
  def deposit(self):
    amt=int(input("Enter amount to deposit"))
    if(amt<0):print("Error Negative value")
    self.balance+=amt
    print(f"updated balance:-{self.balance}")

  @classmethod
  def change_name(cls,name):
    cls.bname=name
#without using function
# p1=Bank()
# p1.name="Tausif"
# p1.age=20
# p1.profession="student"
# p2=Bank()
# p2.name="rohit"
# p2.age=20
# p2.profession="student"
# p3=Bank()
# p3.name="adit sir"
# p3.age=22
# p3.profession="Trainer"
#with using function
# p1=Bank()
# p1.set_details("Tausif",20,"student")
# p2=Bank()
# p2.set_details("Rohit",20,"Student")
# p3=Bank()
# p3.set_details("adit sir",22,"Trainer")
p1=Bank("Tausif",20,"student",8000)
p2=Bank("Rohit",20,"Student",14000)
p3=Bank("adit sir",22,"Trainer",1000000)

# print(f"{p1.name} {p1.balance}")
# p1.withdraw()
# print(f"{p1.name} {p1.balance}")

# p1.deposit()



Bank.change_name("SBI")
print(f"{p1.bname}")
# print(f"{p1.bname}\n{p1.name}\n{p1.profession}")
# print(f"{p3.bname}\n{p3.name}\n{p3.profession}")

