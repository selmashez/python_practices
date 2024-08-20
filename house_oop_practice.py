class House:
    color='white'
    def __init__(self,room,metraj):
        self.room=room
        self.metraj=metraj
    def fullname(self):
        return f'this house has {self.room} rooms and it is{self.metraj} meter'

class Circle:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def cal_mohit(self):
        return self.pi*(self.r)
    
class Circle1:
    pi=3.14
    def __init__(self,r):
        self.r=r
    def cal_mohit(self):
        return Circle1.pi*(self.r)
    

house1=House(3,160)
print(house1.color)
house1.color='blue'
print(house1.color)
del house1.color
print(house1.color)

circle0=Circle(10)
print(circle0.cal_mohit())
circle0.pi=2
print(circle0.cal_mohit())

circle1=Circle1(10)
print(circle1.cal_mohit())
circle1.pi=2
print(circle1.cal_mohit())

class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def fullname(self):
        return f'my name is {self.firstname} and {self.lastname}'


class Stusent(Person):
    def __init__(self,firstname,lastname,major):
        super().__init__(firstname,lastname)
        self.major=major
    

student1=Stusent('selma','shez','com')
print(student1.fullname())
        



