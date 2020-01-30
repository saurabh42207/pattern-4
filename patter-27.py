n=9
for i in range(n//2,-1,-1):
    z=0
    for j in range(0,n//2+1):
        if(j<i):
            print(" ",end='')
        else:
            print(chr(65+z),end=' ')
            z+=1
    print()

for i in range(0,n//2):
    for j in range(0,n//2+1):
        print(chr(65+j),end=" ") if j>i else print(" ",end='') 
    print()       