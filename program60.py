''' sample output
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* * 
* '''

n=int(input('Enter no of rows: '))
for i in range(1,n+1):
    print('* '*i,end='')
    print('  '*(n-i))
for i in range(1,n)[::-1]:
    print('* '*i,end='')
    print('  '*(n-i))
