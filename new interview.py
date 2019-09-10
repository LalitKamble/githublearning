from functools import reduce 
'''
dict Comprehension 

a=[1,2,3,4,5,6,7,8,9.0]
b={i:i for i in a}
print(b)

output :

{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9.0: 9.0}
'''
'''
a=[1,2,3,4,5,6,7,8,9.0]

b={i for i in a for j in range(1,5)}
print(b)

output:

{1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9.0, 9.0, 9.0, 9.0}

'''

'''

call=[{'name':'akshay','Duration':'4:59:00'},
      {'name':'aniket','Duration':'4:59:00'}, second change hote conform nahi mahit
      {'name':'anuja','Duration':'4:59:00'},
      {'name':'akash','Duration':'4:59:00'}]


print(claa[0]);print('Amount':'100')

output:

    [{'name':'akshay','Duration':'4:59:00','Amount':'totle Value'}]
'''


'''

call=[{'name':'akshay','Duration':'4:59:00'},
      {'name':'aniket','Duration':'4:59:00'}, 
      {'name':'anuja','Duration':'4:59:00'},
      {'name':'akash','Duration':'4:59:00'}]


print(call[0])
'''

'''

a='my name is salman'
b=(a[ ::-1])
c=b.split()

print(' '.join(c))




print(a[-6::],end=" ");print(a[-9:-7],end=" ");print(a[-14:-10],end=" ");
print(a[-17:-15],end=" ")




a='my name is salman'
b=a.split()

print(' '.join(b[::-1]))






for i in range(1,10):
    count=0
    for j in range(1,i+1):
        if (i%j==0):
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


'''
'''
febbonacci
a=0
b=1

i=1
while i<=10:
    c=a+b
    print(c)

    a,b=b,c
    i+=1

def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1) + f(n-1)
for i in range(1,10):
    print(f(i))
'''


'''
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end="")
    print()

for i in range(1,20):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i)


n=int(input('Enter the no:'))
for i in range(n):
  

    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))




def f(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
f(5)


palin=input('Enter the palindrom : ')
rev=palin[::-1]
if palin==rev:
    print('input {},rev {}'.format(palin,rev))
    print("palindrom")
else:
    print('input {},rev {}'.format(palin,rev))
    print(" not palindrom")


n=int(input("Enter the no  :"))
for i in range(1,10+1):
    print(n,"*",i,n*i)


for i in range(1,10):
    if i%2==0:
        print('even')
    else:
        print('old')

a=[1,2,3,3,3,6,5,8,5,6]
b=list(filter(lambda l:l%2==0,a))
print(b)

'''



num=int(input("Enter the no:"))
l_num=[[ 0 for X in range(num)] for Y in range(num)]
n=1
low=0
high=num-1
count=int((num+1)/2)

for i in range(count):
    for j in range(low,high+1):
        l_num[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        l_num[j][high]=n
        n=n+1

    for j in range(high-1,low-1,-1):
        l_num[high][j]=n
        n=n+1

    for j in range(high-1,low,-1):
        l_num[j][low]=n
        n=n+1
    low=low+1
    high=high-1
        
for i in range(num):
    for j in range(num):
        print(l_num [i][j],end='\t')
    print()







'''
    
        
a="my name is salman"
print(a[::-1])

print(a[-6:],end=' ');print(a[-9:-7],end=' ');print(a[-14:-10],end=' ');
print(a[-17:-15],end=' ')





s="my name is salman"
s1=s.split()
b=s1[::-1]
print(' '.join(b))



m=s[::-1]
print(m)



b=m.split()
v=b[::-1]
print(' '.join(v))

'''

'''
s='my name is salman'
print(s[::-1])




'''
'''
s="my name is salman"
print(s[-6:],end=" ");
print(s[-9:-7],end=" ");
print(s[-14:-10],end=" ");
print(s[-17:-15],end=" ");





s='my name is salman'
b=s[::-1]
v=b.split()
c=v[::-1]
print(' '.join(c))




s=input("Enter the name : ")
a=s[::-1]
v=a.split()
b=v[::-1]
print(' '.join(b))


a='ravi'
b='teja'
print("join of name:",a+b)



'''
'''

a='my name is salman'

print(a[::-1])


b=a[::-1]
c=b.split()
m=c[::-1]
print(' '.join(m))

b=a.split()
v=b[::-1]
print(' '.join(v))



for i in range(1,10+1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()


def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1)+f(n-2)
for i in range(1,10):
    print(f(i))

    
def f(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
f(5)


for i in range(1,20):
    count=0
    for j in range(1,i+1):
        if (i%j==0):
            count+=1
    if(count==2):
        print(i)


palin=input("Enter the no:")

rev=palin[::-1]

if palin==rev:
    print("input {},rev {}".format(palin,rev))
    print("palindrom")
else:
    print("input {},rev {}".format(palin,rev))
    print("palindrom is not")


n=int(input("Entert the no :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))


a="WABIT"
print(len(a))

prime in n no
i=int(input("Entert the no :"))
count=0
for j in range(1,i+1):
    if (i%j==0):
        count+=1
if(count==2):
    print(i)




def fun(a,**b):
    print(a)
    print(b)
fun(10 ,l='lalit')


def emp(a,**b):
  print(a)
  print(b)
emp(10,b='lalit',c='kamble')

set comprehension

a=[1,2,3,4,5,6,7,8,9]
b={i*i for i in a if i%2==0}
print(b)

list comprehension
a=[i**i for i in range(1,10)if i%2==0]
prin(a)

dict comprension

a={i:i for i in range(1,10)if i%2!=0}
print(a)

filter function
a=tuple(filter(lambda a:a%2==0,range(1,11)))
print(a)


map funsion

a=tuple(map(lambda a:a**a,range(10)))
print(a)



Decorator

def outer(func):
    print("outer function")
    def inner(name):
        print("inner")
    return inner
def outer1(func):
    print("Outer1")
    def inner1(name):
        print("innert")
    return inner1
@outer
@outer1
def f(name):
    print("outter")
f('lalit')




num=int(input('Entert the no:'))
l_num=[[0 for X in range(num)] for Y in range(num)]
n=1
low=0
high=num-1
count=int((num+1)/2)

for i in range(count):
    for j in range(low,high+1):
        l_num[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        l_num[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        l_num[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        l_num[j][low]=n
        n=n+1

    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(l_num[i][j],end='\t')
    print()



    num=int(input("Enter the no:"))
l_num=[[ 0 for X in range(num)] for Y in range(num)]
n=1
low=0
high=num-1
count=int((num+1)/2)

for i in range(count):
    for j in range(low,high+1):
        l_num[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        l_num[j][high]=n
        n=n+1

    for j in range(high-1,low-1,-1):
        l_num[high][j]=n
        n=n+1

    for j in range(high-1,low,-1):
        l_num[j][low]=n
        n=n+1
    low=low+1
    high=high-1
        
for i in range(num):
    for j in range(num):
        print(l_num [i][j],end='\t')
    print()



Write a Java Program to count the number of words in a string using HashMap.

{Pvt.=1, WAB=1, Welcome=1, Software=1, to=1, IT=1}
a='Welcome to WAB IT Software Pvt. Ltd.'
v=a.split()
p=v[::]
z={i:j for i in p for j in range(2)}
print(z)


output:


    {'Welcome': 1, 'to': 1, 'WAB': 1, 'IT': 1, 'Software': 1, 'Pvt.': 1, 'Ltd.': 1}

    


a={1:'lalit',2:'kamble',3:'kalamb'}


print(a[1])




cars = ['Ford', 'BMW', 'Volvo',10]

cars.pop()


print(cars)




n=input("Enter the name:")
l=n.split()
l1=[]


while i < len(l):
    l1.append(l[i][::-1])
    i+=1
    print(' '.join(l1))




l='lalit is good boy in this society good'
p=l.split()
k=[]

for i in p:
    if i == count('good'):
        k.append(len[i])
    print(k)


def f():
    
    a=10
    print(a)

def f1():
    print(a)
f()
f1()


'''

'''
import pickle

class Emp:
    def __init__(self,eno,ename,esal,edd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.edd=edd
    def Display(self):
        print("Enter name",self.eno)
        print("Enter name",self.ename)
        print("Enter name",self.esal)
        print("Enter name",self.edd)
l=Emp(1,'lalit',1000,'kalamb')
e=open('file.dat','wb')
t=pickle.dump(l,e)
print('pickling successfull')

e=open('file.dat','rb')
h=pickle.load(e)
print('pickling not successfull')



palin=input("Entert the name :")
rev=palin[::-1]
if palin==rev:
    print("input: {},rev: {}".format(palin,rev))
    print("palindrom successfull")
else:
     print("input: {},rev: {}".format(palin,rev))
     print("palindrom is not successfull")
    


a={i:i for i in range(1,10)}
print(a)


def f(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
f(5)


def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1) +f(n-2)
for i in range(1,10):
    print(f(i))



palin=input("Enter the no:")
rev=palin[::-1]
if palin==rev:
    print("input {} rev {}".format(palin,rev))
    print("palindrom")
else:
    print("input {} rev {}".format(palin,rev))
    print("palindrom nnn")

for i in range(1,10):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(11,0,-1):
    for j in range(0,5-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
    

n=int(input("Entert the no :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))

for i in range(1,10):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if(count==2):
     print(i)

a=[1,2,3,4,5,6,7,8,9,45,5]
b=list(filter(lambda s:s%2==0,a))
print(b)


b=list(map(lambda s:s*s,a))
print(b)


a=[i*i for i in range(1,10)]
print(a)

b={i*i for i in range(1,10)}
print(b)

c={i:i for i in range(1,10)}
print(c)

'''

class emp:
    def __int__(self,eno,ename,esal,eaddress):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddress=eaddress
    def Display(self):
        print("Entert the s
        
        
    














    





























        
        
        





































    
