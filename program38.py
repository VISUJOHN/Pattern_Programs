''' sample output
         A
       C C C
     E E E E E
   G G G G G G G
 I I I I I I I I I '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print((chr(63+2*i)+' ')*(2*i-1))
