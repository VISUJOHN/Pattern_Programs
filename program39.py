''' sample output
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[x for x in range(1,2*i)])
