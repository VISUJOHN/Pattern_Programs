''' sample output
              E
            D E
          C D E
        B C D E
      A B C D E
        B C D E
          C D E
            D E
              E '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65+n-i,65+n)])
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65+n-i,65+n)])
