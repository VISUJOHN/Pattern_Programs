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
    print('  '*(n-i),end='')
    print('* '*i)
for i in range(1,n)[::-1]:
    print('  '*(n-i),end='')
    print('* '*i)
