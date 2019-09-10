'''
import pickle

class Employee:
  def __init__(self,eno,ename,esal,eaddr):
      self.eno=eno
      self.ename=ename
      self.esal=esal
      self.eaddr=eaddr
  def display():
      print("Employee name",self.eno)
      print("Employee ename",self.ename)
      print("Employee esal",self.esal)
      print("Employee eaddre",self.eaddr)
e=Employee(1,'lalit',100000,'kalamb')
f=open('file.dat','wb')
pickle.dump(e,f)
print("pickle file completed")
f.close()
        
f=open("file.dat",'rb')
e1=pickle.load(f)
print("Unplicking file is completed")
f.close()



a=range(1,10,5)
for i in a:
  print(i)
'''


n=int(input("Enter the no:"))
if n==0:
  print("zero")
elif n==1:
  print('one')
elif n==2:
  print('two')
elif n==3:
  print('three')
elif n==4:
  print('foure')
elif n==5:
  print('five')
elif n==6:
  print('six')
elif n==7:
  print('seven')
elif n==8:
  print('eight')
elif n==9:
  print('nine')
else:
  print("Enter the 0-9 digite")


list=['one','two','three','four','five','six','seven','eight','nine']
n=int(input("Enter the 0-9 digit: "))
print(list[n])

'''

a=10
def f1():
  a=20
  print(a)
def f2():
  print(a)

f1()
f2()

20
10

def f1():
  global a
  a=20
  print(a)
def f2():
  print(a)

f1()
f2()

ouput

20
20
  '''
'''      
l=[1,2,3,4,5,6,7,8,9]
l1=tuple(filter(lambda x:x%2==0,l))
print(l1)

      
l=[1,2,3,4,5,6,7,8,9]
def square(n):
  return n*n
  
l1=tuple(map(square,l))
print(l1)
'''

'''
l=[1,2,3,4,5,6,7,8]
k=[1,2,5,8,6,9,5]
l=tuple(map(lambda x,y:x/y,l,k))
print(l)




l=[1,2,3,4,5,6,7,8,9]
s=tuple(filter(lambda n:n%2==0,l))
print(s)


def calculate(a,b):
  print("the sume :",a+b)
  print("the sume :",a-b)
  print("the sume :",a*b)
  print("the sume :",a/b)

calculate(100,20)
'''
'''
write a program nth no of series
'''
'''
def isEven(n):
    if (n % 2 != 0 or n==1):
        return False
    else:
        return True

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)

def prime(n):
    if n ==1 :
        return 2
    else:

        return (2*(n-1)+1)

n = int(input("Enter a number :"))
if isEven(n):
    n=n/2
    print(prime(n))
else:
    n=n//2+1
    print(fib(n))

'''
'''
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else :
        return fib(n-1)+fib(n-2)
a=fib(2)
print(a)
'''
'''
cmd line arguments
'''
'''
from sys import argv
print("The cmd line argument: ",len(argv))
print("The cmd line argument: ",argv)
print("The cmd line argument: ",)
for i in argv:
  print(i)
'''

'''
factorial
'''
'''
def Fact(a):
  s=1
  for i in range(1,a+1):
    s=s*i
    print(s)
Fact(5)

def getemp(eno,ename,eaddress):
  print(eno,' ',ename,' ',eaddress)
getemp(1,'lalit','kalamb')

def emp(*s):
  print(s)
a=input("Enter the name:")
emp(a)

def emp(a,*b):
  
  print(b)
emp(10,20,30,'lalit')



def emp(a,**b):
  print(a)
  print(b)
emp(10,b='lalit')


'''
'''
list comprehension even
a=[i for i in range(10)if i%2==0]
print(a)
output:
  [0, 2, 4, 6, 8]

a=[i for i in range(10)if i%2!=0]
print(a)

output:
  [1, 3, 5, 7, 9]
  

a=(i for i in range(10) if i%2==0)
print(a,type(a))
for q in a:
  print(q)
  
'''
'''
from functools import reduce

a=reduce(lambda x,y:x+y,range(1,100))
print(a)

b=[1,2,3,4,5,6,7,8,9,10]
n=tuple(filter(lambda a:a%2==0,b))
print(n)

'''
'''

  
def even(a):
  if a%2==0:
    print("Even")
  else:
    print("odd")
n=int(input("Enter the no"))
b=even(n)


def fact(a):
  s=1
  for i in range(1,a+1):
    s=s*i
  print(s)
fact(5)

'''
'''
def local():
  global a
  a=22
  print(a)
def f():
  print(a)
local()
f()
'''
'''
def emp(name,sal,*a):
  print(name,sal,a)
emp('lalit',10000,10,10,10,10,10,20,320)

class abc():
  a=20
  b=30
  
  def dis():
    print("entert the name:")
print(abc.a)
print(abc.b)
abc.dis()
'''
class Emp:
  eno=0
  ename=''
  def __init__(self,eno, ename):
    self.eno=eno
    self.ename=ename
  def display(self):
    print(self.eno,' ',self.ename)
a=Emp(1,'lalit')
a.display()



class Emp:
  def sum(self,*a):
    print(a)
  
z=Emp()
z.sum(10,20,2,3,3,3,3)
z.sum(10,20,30)



'''
Decoratoer


without touchint existing function exted its functionality is called as Decorator
'''
'''
def emp(name):
  print("Decorator",name)
a=emp
emp('lalit')
emp('lalit kamble')
'''
def outer(func):
  print("outer Decorator")
  def inner():
    print("inner Decorator")
  return inner
def outer1(func):
  print("outer Decorator")
  def inner():
    print("inner Decorator")
  
  return inner
@outer1
@outer
def outer2():
  print('outer nam')

outer2()

'''
def emp(func):
  print("Decorator")
  def inner():
    print('inner Decorator')
  
  return inner
@emp
def emp1():
  print('emp1')
emp1()
'''
'''
def shooting(func):
  print("first Decoratoer")
  def inner(name):
    if name=='lalit':
      print('*'*40)
      print('I am ',name)
    else:
      func(name)
  return inner
@shooting
def shooting1(name):
  print("second Decorator")
shooting1('lalit')

'''
'''

def outer(func):
  print("first name")
  def inner():
    print('inner function')
  return inner
def outer1(func):
  print("first name")
  def inner(name):
    if name=='lalit':
      print('#'*40)
      print(name)
      print('@'*40)
    else:
      func(name)
  return inner

@outer1
@outer
def show(name):
  print('second function',name)
show('lalit')




def gan():
  yield 'a'
b=gan()
print(type(b))
print(next(b))
print(b)

'''
'''

first interview q





def fact(a):
  s=1
  for i in range(1,a+1):
    s=s*i
  print(s)
fact(5)

'''
'''
s=int(input("Enter the number:"))
for i in range(n):
  print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
  
  1 
 2 2 
3 3 3 

'''
'''  
for i in range(1,11):
  for j in range(1,i+1):
    print('*',end="")
  print("")

output
*
**
***
****
*****
******
*******
********
*********
**********
prime no

for i in range(1,10):
  count=0
  for j in range(1,i+1):
    if(i%j==0):
      count+=1
  if(count==2):
    print(i)
output:
  2
3
5
7
11
13
17
19
23
29

'''

for i in range(1,50):
  count=0
  for j in range(1,i+1):
    if(i%j==0):
      count+=1
  if(count==2):
    print(i)

def f(n):
  if n==1 or n==2:
    return 1
  return f(n-1)+f(n-2)

for i in range(1,10):
  print(f(i))

  


n=int(input("Enter the no :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
    
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1)+f(n-2)
for i in range(1,10):
    print(f(i))
    
        
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
def fact(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
fact(5)
    
for i in range(1,11):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)

        
palin=input("Entert the name:")
rev=palin[::-1]
if palin == rev:
    print("input:{},rev {}".format(palin,rev))
    print("palindrom")
    
else:
    print("input:{},rev {}".format(palin,rev))
    print('not palindrom')













    






  


    


















































































  












































  
