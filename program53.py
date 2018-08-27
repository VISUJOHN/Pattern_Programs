''' sample output
I  I   I  I   I   I   I   I  I
   G   G  G   G   G   G   G
       E  E   E   E   E
          C   C   C
              A '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1)[::-1]:
    print('   '*(n-i),end='')
    print(((chr(63+2*i)+'  ')*i),end='')
    print((chr(63+2*i)+'  ')*(i-1))
    
