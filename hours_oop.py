import os
os.system('cls')

class Time:
    def __init__(self,h,m,s):
        if h>=24:
            raise ValueError("it should be less than 24")
        if m>=59:
            raise ValueError("it should be less than 60")
        if s>=59:
            raise ValueError("it should be less than 60")
        self.h=h
        self.m=m
        self.s=s


    def __str__(self):
        return f'the time is : {'%02d'%self.h}:{'%02d'%self.m}:{'%02d'%self.s}'
    

    def __add__(self,other):
        s1=self.s+other.s
        if s1>59:
            x = s1//60
            s1=s1-60
            m1 = self.m + other.m + x
            if m1 > 59:
                y = m1//60
                m1 = m1 - 60
                h1 = self.h + other.h + y
            h1 = self.h + other.h
        else:
            m1 = self.m + other.m 
            if m1 > 59:
                y = m1//60
                m1 = m1 - 60
                h1 = self.h + other.h + y
            h1 = self.h + other.h
        return f"the total time is : {'%02d'%h1}:{'%02d'%m1}:{'%02d'%s1}"

    def __eq__(self,other):
        return (self.h==other.h and self.m==other.m and self.s==other.s)
    
    def __gt__(self,other):
        return (self.h>other.h)\
        or (self.h==other.h and self.m>other.m)\
        or (self.h==other.h and self.m==other.m and self.s>other.s)  

    def __sub__(self,other):
        if self.s>other.s:
            s1=self.s-other.s
        else:
            s1=(self.s+60)-other.s
            self.m=self.m-1
        if self.m>other.m:
            m1=self.m-other.m
        else:
            m1=self.m+60-other.m
            self.h=self.h-1
        h1=self.h-other.h

        return f'the total time is: {'%02d'%h1}:{'%02d'%m1}:{'%02d'%s1}'




time1=Time(16,2,58)
time2=Time(3,28,36)

print(time1)
print(time2)
print(time1+time2)
print(time1-time2)
print(time1==time2)
print(time1>time2)

        