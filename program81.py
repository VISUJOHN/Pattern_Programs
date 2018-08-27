''' sample output
        A
      B B
    C C C
  D D D D
E E E E E
  D D D D
    C C C
      B B
        A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print((chr(64+i)+' ')*i)
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print((chr(64+i)+' ')*i)
