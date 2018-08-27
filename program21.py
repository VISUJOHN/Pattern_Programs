''' sample output
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10 '''

n=int(input('Enter no of row: '))
for i in list(range(1,n+1))[::-1]:
    print(*[j for j in list(range(n-i+1,n+1))[::-1]])
