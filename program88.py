''' sample output
    E
   D D
  C   C
 B     B
A       A '''

n=int(input('Enter no of rows: '))
for i in range(n):
    if i==0:
        print(' '*(n-i),end='')
        print(chr(64+n-i))
    else:
        print(' '*(n-i),end='')
        print(chr(64+n-i),end='')
        print(' '*(2*i-1),end='')
        print(chr(64+n-i))
