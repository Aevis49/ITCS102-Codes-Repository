n = 5
i = 8

for x in range(n):
    for y in range(n-1-x):
        print(" ", end=" ")
    for o in range(i):
        if x==0 or x==n-1 or o==0 or o==i-1:
         print("*", end=" ")
        else:
           print(" ",end=" ")
    print()

print(' ')
for x in range(n):
    for y in range(n):
        if x==y or x+y==n-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

print(' ')

for x in range(n,0,-1):
    for y in range(1,x+1):
        print("m", end=" ")
    for o in range(1,x+1):
        print("*",end=" ")
    print()