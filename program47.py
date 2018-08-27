''' sample output
    5
   5 4
  5 4 3
 5 4 3 2
5 4 3 2 1
 5 4 3 2
  5 4 3
   5 4
    5 '''

n=int(input("Enter no of rows: "))

for i in range(1,n+1):
    print(' '*(n-i),end='')
    print(*[j for j in range(n-i+1,n+1)[::-1]])
for i in range(1,n)[::-1]:
    print(' '*(n-i),end='')
    print(*[j for j in range(n-i+1,n+1)[::-1]])    



