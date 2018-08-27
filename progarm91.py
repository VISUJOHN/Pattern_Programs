''' sample output
1       1
 2     2
  3   3
   4 4
    5 '''

n=int(input('Enter no of rows: '))
for i in range(n)[::-1]:
    if i==0:
        print(' '*(n-i),end='')
        print(n-i)
    else:
        print(' '*(n-i),end='')
        print(n-i,end='')
        print(' '*(2*i-1),end='')
        print(n-i)
