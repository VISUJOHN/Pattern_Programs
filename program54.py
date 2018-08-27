''' sample output
A B C D E F G H I
  A B C D E F G
    A B C D E
      A B C
        A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)],*[chr(j) for j in range(65+i,64+2*i)])
