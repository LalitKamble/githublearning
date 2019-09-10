
'''
program practics
* print

for i in range(1,11):
    for j in range(1,i+1):
        print('*',end="")
    print("")
output:

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
'''


'''
prime or not in python
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if (count==2):
        print(i)




output-


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
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97

'''
'''
fibonacci sequence


def f(n):
    if n == 1 or n==2:
        return 1
    return f(n-1) + f(n-2)
for i in range(1,10):
    print(f(i))

output:
    1
1
2
3
5
8
13
21
34
'''




'''
for i in range(1,10):
    for j in range(1,i+1):
        print("*",end="")
    print("")



for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if (count==2):
        print(i)



def f(n):
    if n==1 or n==2:
        return 1
    return f(n-1)+f(n-2)
for i in range(1,10):
    print(f(i))

'''
'''
factorial

n= int(input("Enter the number of :"))

result=1
for i in range(n,0,-1):
    result=result*i
print("Facrorial no is",n,"of",result)


output:
    Enter the number of :5
Facrorial no is 5 of 120



n= int(input("Enter the no of :"))
result=1
for i in range(n,0,-1):
    result=result*i
print("Factorial no of ",n,"is",result)

'''
'''
def f(n):
    
    if (n==0) or (n==1):
        
        return 1
    
    else:
        
        return n*f(n-1)
    
n=int(input('Enter the no:'))
res=f(n)
print(res)
'''
'''

'''
'''
class

 
class Emp:
    name='Lalit'
    
    salary=500000
    def working(self):
        print("lalit is good Boy")
    def seepling(self):
        print("lalit is very good boy")
e=Emp()
print(e.name)
print(e.salary)
e.working()
e.seepling()
'''
'''
class Emp:
    name='lalit'
    company='Dotcom'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Display(self):
        print("Emp name is ",self.name)
        print("Emp salary is",self.salary)
        print("Emp name is ",Emp.name)
        print("Emp company is ",Emp.company)
e=Emp("lalit",58585)
e.Display()
'''
'''

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
        ]
result=[[0,0,0],
        [0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j]=matrix[i][j]

for x in result:

    print(x)


'''
'''
num=int(input("Enter the no:"))
k=1
for i in range(1,num+1):
    for j in range(i,k+1):
        print("*",end="")
    k=k+2

    print("")
'''
'''
start format 

for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

output:
  * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''
'''
for i in range(11,0,-1):
    for j in range(0,11-i):
        print(end=" ")
    for j in range(0,i):
        print('*',end=" ")
    print("")
'''
'''
output:-


* * * * * * * * * * * 
 * * * * * * * * * * 
  * * * * * * * * * 
   * * * * * * * * 
    * * * * * * * 
     * * * * * * 
      * * * * * 
       * * * * 
        * * * 
         * * 
          * 

'''
'''
for row in range(7):
    for col in range(5):
        if col==0 or (row==6 and col>0):
            print("*",end="")
        else:
            print(end=" ")
    print()

output:-

*    
*    
*    
*    
*    
*    
*****
'''
'''

for row in range(6
                 ):
    for col in range(7):
        if (row==0 and col%3!=0)or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end=" ")
        else:
            print(end=" ")
    print()

 * *  * *  
*   *   * 
*      * 
 *    *  
  *  *   
   *
'''
'''
Palindrome program

____________
lal=lal
_____________

palin =input("Enter the values:")
rev=palin[::-1]
if palin == rev:
    print ("input:{},Rev:{}".format(palin, rev))

    
    print("String is palindrome")
else:
    print ("input:{},Rev:{}".format(palin,rev))
    
    print("String is not palindrome")

output:

Enter the values:Lal
input:Lal,Rev:laL
String is not palindrome




palin= input("enter the number :")

rev=palin[::-1]


if palin==rev:
    print("Input:{},rev{}".format(palin,rev))
    print("Palindrom is string")
else:
    print("Input:{},rev{}".format(palin,rev))
    print("Palindrom is not string")
'''
'''
Def Function &lambda function 
def mx(x,y):
    if x>y:
        return x
    else:
        return y
print(mx(8,5))
'''
'''
lambda function 
ma=lambda a,b:a if a>b else b
print(ma(20,30))
'''
'''
def add(a,b):
    return a+b
print(add(10,30))
'''


'''

for i in range(0,10):
    for j in range(0,10-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for i in range (1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(10,0,-1):
    for j in range(0,10-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
'''
'''
palin=input("enter the number :")
rev=palin[::-1]
if palin==rev:
    print("input:{},rev{}".format(palin,rev))
    print("palindrom number")
else:
    print("input:{},rev{}"
          .format(palin,rev))
    print("palindrom not  number")
'''
'''
Square root 
l=[1,2,3,4,5,6]
print(tuple(map(lambda x:x**2,l)))
'''
'''
for i in range(1,21,2):
    print(i)
output:
    

1
3
5
7
9
11
13
15
17
19
'''
'''
for i in range(1,30,3):
    print(i)
'''
'''
Even Odd program
n=int(input("enter the number of :"))
if (n%2==0):
    print(n,'even')
else:
    print(n,'odd')
'''
'''
l=[1,2,3,4,5,6]
print(tuple(map(lambda x:x**2,l)))


n= int(input("Enter the Number of :"))
if (n%2==0):
    print(n,"Even")
else:
    print(n,"Odd")'''





'''
n="my name is salman"
print(n[::-1])
print(n[-6:],end=" ");print(n[-9:-7],end=" ");print(n[-14:-9],end=" ");print(n[-17:-15],end=" ")

'''

'''
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            
            count+=1
    if (count==2):
        print(i)

'''








'''



for i in range(1,100):
    count=0
    for j in range(1,i+1):
        if (i%j==0):
            count+=1
    if (count==2):
        print(i)
'''


'''
class Animal:
    def dog(self):
        print("Enter the dogs")
    def cat(self):
        print(" poikuhjg oiu")
d=Animal()
d.dog()
d.cat()
'''
'''
input


name=input("enter the name:")
if name=='lalit':
    print('hello',name)
    print("hi")

'''
'''
name=input("enter the name:")
if name=="lalit":
    print('hello',name)
else:
    print("
          name is not valid")
        '''
'''
l=int(input("enter the no:"))
for n in range(1,100):
    if n%2==0:
        print('even',n)
    else:
        print('Odd',n)
'''
'''
a=int(input("enter the no:"))
b=int(input("enter the no1:"))
if a>b:
    print("biggest No",a)
else:
    print('smallest No',b)
'''
'''
name=input("enter the name:")
age=int(input("Enter the no1:"))
if age<15:
    print(name,' you are child')
elif age<25:
    print(name,'you are young')
elif age<40:
    print(name,'you are old')
else:
    print("invalid Age")
'''
'''
username=input("Enter the name:")

pwd=int(input("Enter the password:"))
if username=="lalit":
    print(username,'successfully')
    if pwd=='358':
        print(pwd,'successfully')
    else:
        print('wrong password')
else:
    print("wrong Username ")
    '''
'''
'''
'''
for i in range(1,10,2):
    print(i)
'''
'''
for i in range(1,20):
    if i%2==0:
        print(i)
'''
'''
for i in range(10,0,-1):
    print(i)
'''
'''
padha tayar
a=int(input("Enter the no:"))
for b in range(1,10,1):
    print(a,'*',b,'=',a*b)
'''
'''
a=int(input("enter the no:"))
s=0
for i in range(1,a+1):
    s+=1
    print(s)

fact
a=int(input("enter the no:"))
s=1
for i in range(1,a+1):
    s=s*1
    print(s)
'''

'''
Factorial no
n=int(input("Enter the no:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''
'''

prime no
n=int(input("Enter the no:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print(count)
    if count==2:
        print("Enter the no",i,'is prime')
    else:
        print("not prime")
'''
'''
prime or not in python
for i in range(1,101):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if (count==2):
        print(i)
'''
'''
padhe 1to 10
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,10+1):
        c=i*j
        print(i,'*',j,"=",i*j)

'''
'''
i=1
while i<=10:
    print(i)
    i+=1
    
fabonnaci series


a=0
b=1
i=1
while i<=10:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1

output

1
2
3
5
8
13
21
34
55
89
'''
'''
while True:
    name=input("Enter the name:")
    print(name)
    
if name=="lalit":
    print(name,"is ll")
else:
    print("hello")

 '''   '''
a=['lalit','Bhimraoji','kamble']
for i in a:
    print(i,'-->',len(i))
    for j in i:
        print(j)'''

'''
list Comprehenssion


a=[i for i in range(1,10+1)]
print(a)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
'''
cube root

a=[x**x for x in range(1,10)]
print(a)

[1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
'''
'''
square root
a=[i for i in range(1,10)]
b=[j for j in a if j%2==0]
print(b)
'''

'''
a=(x**x for i in range(1,10))
print(a)'''

'''
hello print
def fun():
    print("hello")
fun()

even Odd
def fun():
    a=int(input("Enter the no:"))
    if a%2==0:
        print("even")
        
    else:
        print("odd")
fun()

addition
def fun():
    a=int(input("Enter the no:"))
    b=int(input("Enter the no1:"))
    c=a+b
    print(c)
fun()


factorial
def fact(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(s)
fact(5)
'''



'''

l=[1,2,3,4,5,6,7,8,9,7]

a=list(filter(lambda x:x%2==0,l))
print(a)
'''
'''






09/08/2019

'''
'''
pattern program
n= int(input("Enter the no:"))
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))


output:



    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 
'''
'''
def emp(func):
    print("Decorator")
    def inner():
        print("inner Decorator")
    return inner
@emp
def em():
    print("EM Decorator")
em()
'''
'''
a="my name is salman"
print(a[::-1])

print(a[-6:],end=' ');print(a[-9:-7],end=' ');print(a[-14:-10],end=' ');
print(a[-17:-15],end=' ')
'''

'''
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

output

namlas si eman ym

'''

'''
s="my name is salman"
print(s[-6:],end=" ");
print(s[-9:-7],end=" ");
print(s[-14:-10],end=" ");
print(s[-17:-15],end=" ");

output

salman is name my 
'''

'''
s='my name is salman'
b=s[::-1]
v=b.split()
c=v[::-1]
print(' '.join(c))

output


ym eman si namlas


s=input("Enter the name : ")
a=s[::-1]
v=a.split()
b=v[::-1]
print(' '.join(b))
'''

a='ravi'
b='teja'
c=a+b
v=c.split()

print("join of name:",'  '.join(v))








































































































              
              














































































    




    


    
        































    
            






















































    
    







































    





    

    


































    





    
































    



































             































          











































    



































































































                
                
                






















    








    














            
        
        
       
        
        


