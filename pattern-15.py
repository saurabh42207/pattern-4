n=5
for i in range(n,-1,-1):
    z=0
    for j in range(0,n,1):
        if (j<i):
            print(" ",end='')
        else:
            print(chr(65+z),end=' ')
            z+=1
    print()