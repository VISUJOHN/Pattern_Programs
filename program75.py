''' sample output
E D C B A
  D C B A
    C B A
      B A
        A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1)[::-1]:
    print('  '*(n-i),end='')
    print(*[chr(j) for j in range(65,65+i)][::-1])
