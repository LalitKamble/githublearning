'''
try:
    a=int(input("Enter the no:"))
    b=int(input("Enter second no:"))
    a/b
except ZeroDivisionError:
    print('invalid error')

    
n=int(input("Enter the no :"))

for i in range(10):

    try:
        c=n/i
        print(c)
    except ZeroDivisionError:
        print("second values is ")




'''


'''
try:
    print(a)
except:
    print("Enter the values")





ZeroDivisionError
ValueError

try:
    a=int(input('Entert no'))
    b=int(input("Entert the no"))
    print(a/b)
except ZeroDivisionError:
    print("second value can not be zero")
except ValueError:
    print("please Entert the digit")
    
'''

'''
constructor

function overloading
'''
'''
class Emp:
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print(a+b+c)
a=Emp()
a.sum(10,20)
a.sum(10,20,30)

'''

'''
in python

class Emp:
    def f(self,*a):
        print(a)
        
b=Emp()
b.f(10,20,30,20,20,20,20,20,20,20,20,200,20,32,0,1,'lalit')
'''
'''
single Inheristance



class Emp:
    eno=0
    ename=''
    eaddress=''
    esal=0
    
    def getdetails(self):
        self.eno=int(input('Entert the name:'))
        self.ename=input('Entert the name:')
        self.eaddress=input('Entert the name:')
        self.esal=float(input('Entert the name:'))
class Emp1(Emp):
    hr=0
    def getdetails1(self):
        self.hr=input("Entert the name")
    def showDetails(self):
        print("Enter the eno :",self.eno)
        print("Enter the eno :",self.ename)
        print("Enter the eno :",self.eaddress)
        print("Enter the eno :",self.esal)
        print("Enter the eno :",self.hr)
        
a=Emp1()
a.getdetails()
a.getdetails1()
a.showDetails()

'''
'''
multiple Inheritance

class Abc:
    def add(self,a,b):
        print("Enter the no :",a+b)
class Pqr:
    def sub(self,a,b):
        print("Substration:",a-b)
class Xyz(Abc,Pqr):
    def mul(self,a,b):
        print("Multiplication :",a*b)
    def div(self,a,b):
        print("div :",a/b)

o=Xyz()
o.add(10,20)
o.sub(10,20)
o.mul(10,20)
o.div(10,20)
        
'''
'''
multilevel inheritance

class Abc:
    a=0
class Pqr(Abc):
    b=0
class Xyz(Pqr):
    c=0
    def get(self):
        print(self.a,
              self.b,
              self.c)
o=Xyz()
o.a=10
o.b=20
o.c=30
o.get()
'''

'''
Data Abstration
class Abc:
    __p=100
    o='lalit'
    def f(self):
        print("Hiding Data Abstration")
a=Abc()
a.f()
print(a.o)
'''

'''   
class Emp:
    def __init__(self,**x):
        self.x=x
    def Display(self):
        print("Entert the name:",self.x)
a=Emp(name='lalit',sal='lalit')
a.Display()
'''

'''
class Emp:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def Display(self):
        print("Enter the no:",self.a)
        print("Enter the no:",self.b)

    def __add__(self,other):
        return Emp(self.a+other.a,
                   self.b+other.b)
x=Emp()
x.Display(10,20)


a=20
print("The {:.2f}".format(a))

for i in range(1,5):
    for j in range(0,5-i-1):
        print(end=' ')
    for j in range(1,i+1):
        print('*',end=" ")
    print()





n=int(input("Enter the name :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))    


a=[1,2,3,4,5,6,7,8,9]
v={i for i in a}
print(v)
'''
from functools import reduce

a=[1,2,3,4,5,6,7,8,9,5,2]
b=list(map(lambda s:s*s,a))
print(b)


b=tuple(filter(lambda a:a%2==0,a))
print(b)


b=reduce(lambda x,y:x+y,a)
print(b)

'''

def outer(func):
    print("Enter the outer dec")
    def inner():
        print('inner dec')
    return inner
def outer1(func):
    print("Outer")
    def inner1():
        print("inner dec")
    return inner

dist()
dist.inner()
a.inner1()

a=int(input("Enter the no  :"))
b=int(input("Enter the no1 :"))

c= a if a>b else b
print(c)
                
'''
'''
list dict set comphrensation

a=[1,2,3,4,5,6,7,8,9]

b={i*i for i in a}
print(b)




for i in range(1,8):
    for j in range(0,5-i-1):
        print(end=' ')
    for j in range(1,i+1):
        print("*",end=" ")
    print()


n=int(input("Entert the no:"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
    


for i in range(11,0,-1):
    for j in range(0,11-i):
        print(end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()


for i in range(11,0,-1):
    for j in range(0,11-i):
        print(end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()




a={i*i for i in range(1,10)}
print(a)

from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda b:b%2==0,a))
print(k)


v=list(map(lambda a:a+a,a))
print(v)


b=reduce(lambda c,y:c+y,a)
print(b)


a='lalit is good boy'
a=a.split()
l=[]
for i in a:
    if i!='lalit':
        l.append(i)
    print(l)


'''






































































    





























































        
        
        
        























               


























        
    
