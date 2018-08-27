''' sample output
    5
   4 4
  3   3
 2     2
1       1 '''

n=int(input('Enter no of rows: '))
for i in range(n):
    if i==0:
        print(' '*(n-i),end='')
        print(n-i)
    else:
        print(' '*(n-i),end='')
        print(n-i,end='')
        print(' '*(2*i-1),end='')
        print(n-i)
