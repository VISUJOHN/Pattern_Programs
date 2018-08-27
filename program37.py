''' sample output
         A
       B B B
     C C C C C
   D D D D D D D
 E E E E E E E E E '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('  '*(n-i),end='')
    print((chr(64+i)+' ')*(2*i-1))
