n=9
for i in range(n//2,-1,-1):
    z=1
    for j in range(0,n//2+1):
        if(j<i):
            print(" ",end='')
        else:
            print(z,end=' ')
            z+=1
    print()

for i in range(0,n//2):
    for j in range(0,n//2+1):
        print(j+1,end=" ") if j>i else print(" ",end='') 
    print()       