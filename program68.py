'''sample output
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[j for j in range(1,i+1)])
