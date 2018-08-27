''' sample output
                 A
                A B
              A B C
            A B C D
          A B C D E
        A B C D E F
      A B C D E F G
    A B C D E F G H
  A B C D E F G H I
A B C D E F G H I J '''

n=int(input('Enter no of rows: '))

for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)])
