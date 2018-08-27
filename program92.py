''' sample output
5       5
 4     4
  3   3
   2 2
    1 '''

n=int(input('Enter no of rows: '))
for i in range(n)[::-1]:
    if i==0:
        print(' '*(n-i),end='')
        print(i+1)
    else:
        print(' '*(n-i),end='')
        print(i+1,end='')
        print(' '*(2*i-1),end='')
        print(i+1)
