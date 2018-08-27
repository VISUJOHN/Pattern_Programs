''' sample output
        A
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print(*[chr(x) for x in range(65,64+2*i)[::-1]])
