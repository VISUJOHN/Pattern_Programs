''' sample output
E
E D
E D C
E D C B
E D C B A
E D C B
E D C
E D
E '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print(*[chr(j) for j in range(65+n-i,65+n)][::-1],end='')
    print('  '*(n-i))
for i in range(1,n)[::-1]:
    print(*[chr(j) for j in range(65+n-i,65+n)][::-1],end='')
    print('  '*(n-i))     
