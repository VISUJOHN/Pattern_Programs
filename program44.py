
''' sample output
        A 
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
  D C B A B C D
    C B A B C
      B A B
        A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(x) for x in range(65,65+i)[::-1]],end=' ')
    print(*[chr(x) for x in range(66,64+i+1)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(x) for x in range(65,65+i)[::-1]],end=' ')
    print(*[chr(x) for x in range(66,64+i+1)])
