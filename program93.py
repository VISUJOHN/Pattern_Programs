''' sample output
E       E
 D     D
  C   C
   B B
    A '''

n=int(input('Enter no of rows: '))
for i in range(n)[::-1]:
    if i==0:
        print(' '*(n-i),end='')
        print(chr(65+i))
    else:
        print(' '*(n-i),end='')
        print(chr(65+i),end='')
        print(' '*(2*i-1),end='')
        print(chr(65+i))
