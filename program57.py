''' sample output
            4
          4 3
        4 3 2
      4 3 2 1
    4 3 2 1 0
      4 3 2 1
        4 3 2
          4 3
            4 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i,n)][::-1])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[j for j in range(n-i,n)][::-1])
