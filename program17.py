''' sample output
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1 '''

n=int(input('Enter no of rows: '))
for i in list(range(1,n+1)[::-1]):
    print(*[j for j in range(1,i+1)])
 
