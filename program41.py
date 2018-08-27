''' sample output
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(x) for x in range(65,64+2*i)])
