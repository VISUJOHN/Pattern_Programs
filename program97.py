''' sample output
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
0 1 0 1 0 1
1 0 1 0 1 0 1 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    if i%2==0:
        print(*[0 if i%2!=0 else 1 for i in range(1,i+1)])
    else:
        print(*[1 if i%2!=0 else 0 for i in range(1,i+1)])
