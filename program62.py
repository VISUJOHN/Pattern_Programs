''' sample output
4
3 4
2 3 4
1 2 3 4
0 1 2 3 4
1 2 3 4
2 3 4
3 4
4 '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print(*[j for j in range(n-i,n)],end='')
    print('  '*(n-i))
for i in range(1,n)[::-1]:
    print(*[j for j in range(n-i,n)],end='')
    print('  '*(n-i))
