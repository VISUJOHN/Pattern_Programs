''' sample output
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10
    1 2 3 4 5 6 7 8 9 10'''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print(*range(1,n+1))
