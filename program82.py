''' sample output
        A
      A B
    A B C
  A B C D
A B C D E
  B C D E
    C D E
      D E
        E'''
n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65+n-i,65+n)])
