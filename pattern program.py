
'''09/08/2019

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
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

'''
'''

n=int(input("Enter the no:"))
for i in range(n):
    print((str(i+1)+' ')*n)


output:
    
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 

'''

'''
 Q 1)
python pattern program printing numkber in square shape
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
output:


1	2	3	4	5	
16	17	18	19	6	
15	24	25	20	7	
14	23	22	21	8	
13	12	11	10	9

'''
'''
num=int(input("Entert the name:"))
l_num=[[0 for x in range(num)]for y in range(num)]
n=1
low=0
high=num-1
count=int((num+1)/2)

for i in range(count):
    for j in range(low,high+1):
        l_num[i][j]=n
        n+=1
    for j in range(low+1,high+1):
        l_num[j][high]=n
        n+=1
    for j in range(high-1,low-1,-1):
        l_num[high][j]=n
        n+=1
    for j in range(high-1,low,-1):
        l_num[j][low]=n
        n+=1
    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(l_num[i][j],end='\t')
    print()




'''

'''

num=int(input("Enter the no:"))
l_num=[[0 for X in range(num)]for Y in range(num)]
low=0
high=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        l_num=[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        l_num=[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        l_num=[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        l_num=[j][high]=n
        n=n+1
    low=low+1
    high=high-1
    

for i in range(num):
    for j in range(num):
        print(l_num[i][i],end='\t')
    print()


'''
'''

a=int(input("Enter the radius: "))
area=3.14*a*a
print("The radius",area)

output:

    Enter the radius: 2
The radius 12.56

'''

'''

a='lalit'

print(a[::-1])

output:
tilal

a=input("Enter the name:")
r=reversed(a)
print(''.join(r))

output:
    
Enter the name:lalit kamble
elbmak tilal

'''

'''
s='my name is salman'
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)

output:
tilal

'''


'''
s="my name is salman"
l=s.split()
l1=l[::-1]
out=' '.join(l1)
print(out)

output:
    salman is name my

'''
'''
s="salman is name my"
l=s.split()
l1=[]
for w in l:
    l1.append(w[::-1])
    a=' '.join(l1)
print(a)

output:
    namlas si eman ym
'''

'''
n="my name is salman"
print(n[::-1])
print(n[-6:],end=" ");print(n[-9:-7],end=" ");print(n[-14:-9],end=" ");print(n[-17:-15],end=" ")

output:

namlas si eman ym
salman is name  my
'''

'''

s='one two three four five six'
l=s.split()
i=0
l1=[]
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
    out=' '.join(l1)
print(out)


output:
    one owt three ruof five xis
'''
'''
even Odd

s="lalitkamble"
i=0
while i<len(s):
    print(s[i])
    i=i+2
output

l
l
t
a
b
e
'''
'''
s='lalitkamble'
i=1
while i<len(s):
    print(s[i])
    i=i+2
output:

s='lalit'
print(s[1::2])


a
i
k
m
l
'''
'''
s='A1B2C3'
l=s.split()
out=' '.join(l)
print(sorted(out))

s='B1A2C3'
a=[]
b=[]
for ch in s:
    if ch.isalpha():
        a.append(ch)
    else:
        b.append(ch)
out=' '.join(sorted(a)+sorted(b))
print(out)
output:
    
['1', '2', '3', 'A', 'B', 'C']
A B C 1 2 3

'''
'''
s='a4b3c2'
out=''
for ch in s:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        out=out+x*d
print(out)

output:

aaaabbbcc
'''
'''

a='ABBCCDDDE'
l=''
for ch in a:
    if ch not in l:
        l+=ch
      
print(l)

output: ABCDE
'''


'''
a='abbccddeeffg'
l=[]
for ch in a:
    if ch not in l:
        l.append(ch)
        b=' '.join(l)
print(b)
    
s='aabbccddeef'
a=(set(s))
l=' '.join(a)
print(l)
'''
n=int(input("Enter the no :"))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
'''

'''



    
s='zzccddaaddrrgfgtt'
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} accoure,{} time'.format(ch,s.count(ch)))
'''
output
a accoure,2 time
b accoure,2 time
c accoure,2 time
d accoure,2 time
e accoure,2 time
f accoure,12 time
'''


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
    





































































































































    



















        




















