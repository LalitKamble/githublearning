import functools
l=[1,2,3,5,4,7,8]


j=reduce(lambda x,y:x>y,l)

print(j)


