''' sample output
    A
   B B
  C   C
 D     D
E       E '''

n=int(input('Enter no of rows: '))
for i in range(n):
    if i==0:
        print(' '*(n-i),end='')
        print(chr(65+i))
    else:
        print(' '*(n-i),end='')
        print(chr(65+i),end='')
        print(' '*(2*i-1),end='')
        print(chr(65+i))
