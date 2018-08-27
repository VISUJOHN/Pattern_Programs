''' sample output
    1
   2 2
  3   3
 4     4
5       5 '''

n=int(input('Enter no of rows: '))
for i in range(n):
    if i==0:
        print(' '*(n-i),end='')
        print(i+1)
    else:
        print(' '*(n-i),end='')
        print(i+1,end='')
        print(' '*(2*i-1),end='')
        print(i+1)
