class Student:
    ''' lalit is good boy '''
    cname='lalit'
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print('Entert first name',self.name)
        print('Entert first name',self.age)
        print('Entert first name',self.address)
    @classmethod
    def avg(cls):
        print("The First name",cls.cname)
    @staticmethod
    def Avg(x,y):
        print("The Second no is ",x*y/2)
        
s=Student('lalit',26,'kalamb')
print(s)
s.display()
s.avg()
s.Avg(10,20)



''''

factorial

def fact(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
fact(5)

Febbonaci series

a=0
b=1

i=1
while i<=10:
    c=a+b
    print(c)

    a,b=b,c
    i=i+1
'''
    
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end=" ")
    print()


for i in range(1,10):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)


a=10
def f():
    global a
    a=20
    print(a)
def f1():
    print(a)
f()
f1()

'''


def f(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
f(5)










def f(a,**b):
    print(a)
    print(b)
f(10,name='lalit')















        

