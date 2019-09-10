n=int(input("Enter the number:"))
for i in range(n):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
    if (count==2):
        print(i)
'''
a=0
b=1
i=1
while i<=10:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1'''
def f(n):
    
    if (n==0) or (n==1):
        
        return 1
    
    else:
        
        return n*f(n-1)
