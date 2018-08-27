''' sample output
9 9 9 9 9 9 9 9 9
  7 7 7 7 7 7 7
    5 5 5 5 5
      3 3 3
        1 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1)[::-1]:
    print('  '*(n-i),end='')
    print(((str(2*i-1)+' ')*i).rstrip(),(str(2*i-1)+' ')*(i-1))
