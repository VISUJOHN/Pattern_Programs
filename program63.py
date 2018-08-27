''' sample output
E
D D
C C C
B B B B
A A A A A
B B B B
C C C
D D
E '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print((chr(65+n-i)+' ')*i,end='')
    print('  '*(n-i))
for i in range(1,n)[::-1]:
    print((chr(65+n-i)+' ')*i,end='')
    print('  '*(n-i))
