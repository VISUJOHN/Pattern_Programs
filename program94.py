''' sample output
A       A
 B     B
  C   C
   D D
    E '''
    
n=int(input('Enter no of rows: '))
for i in range(n)[::-1]:
    if i==0:
        print(' '*(n-i),end='')
        print(chr(64+n-i))
    else:
        print(' '*(n-i),end='')
        print(chr(64+n-i),end='')
        print(' '*(2*i-1),end='')
        print(chr(64+n-i))
