''' sample output
        0
      1 0 1
    2 1 0 1 2
  3 2 1 0 1 2 3
4 3 2 1 0 1 2 3 4 '''

n=int(input('Enter no of rows: '))
for i in range(n):
    print('  '*(n-i-1),end='')
    print(*[str(x) for x in range(i+1)[::-1]],end=' ')
    print(*[str(x) for x in range(1,i+1)])
