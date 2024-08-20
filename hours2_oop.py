import os
os.system('cls')

class Deposit:

    def __init__(self,name,amount=0):
        self.name=name
        self.amount=amount

    def __add__(self,other):
        second_name=self.name+''+other.name
        second_amount=self.amount+other.amount
        return f'the new deposit is for {second_name} and it has {second_amount}$'
    
    def __iadd__(self,other):
        self.amount+=other.amount
        return f'{self.name} has {self.amount} \n {other.name} has 0'
    
    def __str__(self):
        return f'{self.name}:{self.amount}'
    
    def deposit(self,bardasht):
        self.amount=self.amount-bardasht
        return f'{self.name} has {self.amount}'
    
    def withdraw(self,variz):
        self.amount=self.amount+variz
        return f'{self.name} has {self.amount}'
    
    def transfer(self,other,x):
        if x<other.amount:
            return f'mojudi kafi nist'
        else:
            self.amount=self.amount+x
            other.amount=other.amount-x
            return f'{self.name}:{self.amount}\n{other.name}:{other.amount}'
        



p1=Deposit('reza',2000)
p2=Deposit('saeed',3000)
p2.deposit
print(p1)
print(p1+p2)
p2+=p1
print(p2)



    