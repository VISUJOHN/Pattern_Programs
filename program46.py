''' sample output
        A 
      A B A
    A B C A B
  A B C D A B C
A B C D E A B C D
  A B C D A B C
    A B C A B
      A B A
        A  '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)],end=' ')
    print(*[chr(j) for j in range(65,64+i)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)],end=' ')
    print(*[chr(j) for j in range(65,64+i)])
