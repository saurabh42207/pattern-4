n=5
for i in range(0,n-1):
    for j in range(n,-1,-1):
        if j<=i:
            print('*',end=' ')
        else:
            print(' ',end='')        
    for j in range(n,-1,-1):
        if j<=i:
            print('*',end=' ')
        else:  
            print('  ',end='')
    
    print()
for j in range(0,2*n+2):
    print('*',end=' ')