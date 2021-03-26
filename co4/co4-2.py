class Bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self):
        amt=float(input("enter the amount to be deposited:"))
        return(self.bal+amt)
    def withdraw(self):
        getamt=float(input("enter the amount to be withdrawn:"))
        if self.bal<getamt:
            print("insufficient balance")
        return(self.bal-getamt)
B1=Bank(101,"chithra","savings",2000)
print(B1.deposit())
print(B1.withdraw())