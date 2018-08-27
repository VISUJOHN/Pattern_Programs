''' sample output
  5 4 3 2 1
   4 3 2 1
    3 2 1
     2 1
      1 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1)[::-1]:
    print(' '*(n-i),end='')
    print(*[j for j in range(n-i+1,n+1)])
    
