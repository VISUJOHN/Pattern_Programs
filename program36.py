''' sample output
         1
       2 2 2
     3 3 3 3 3
   4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5 5 '''

n=int(input('Enter no of rows: '))

for i in range(1,n+1):
    print('  '*(n-i),end='')
    print((str(i)+' ')*(2*i-1))
