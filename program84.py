''' sample output
         5
       5 4 5
     5 4 3 4 5
   5 4 3 2 3 4 5
 5 4 3 2 1 2 3 4 5
   5 4 3 2 3 4 5
     5 4 3 4 5
       5 4 5
         5 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i+1,n+1)][::-1],*[j for j in range(n-i+2,n+1)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i+1,n+1)][::-1],*[j for j in range(n-i+2,n+1)])
    
