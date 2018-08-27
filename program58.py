''' sample output
         3
       2 3
     1 2 3
   0 1 2 3
     1 2 3
       2 3
         3 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i,n)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i,n)])
