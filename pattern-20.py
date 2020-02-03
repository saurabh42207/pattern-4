n=5
for i in range(n,0,-1):
    z=0
    for j in range(n,0,-1):
        if j>i:
            print(" ",end='')
        else:
             print(chr(65+z),end=' ')
             z+=1
    print()