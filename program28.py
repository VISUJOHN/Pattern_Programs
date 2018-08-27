''' sample output
                  A

                 B B

               C C C

             D D D D

           E E E E E

         F F F F F F

       G G G G G G G

     H H H H H H H H '''
     
n=int(input('Enter no of rows: '))

for i in range(1,n+1):
    print('  '*(n-i),end='')
    print((chr(64+i)+' ')*i)
