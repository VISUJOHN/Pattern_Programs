''' sample output
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1 '''

n=int(input('Enter no of rows: '))

for i in range(1,n+1):
    print('  '*(i-1),end='')
    print((str(n-i+1)+' ')*(n-i+1))
