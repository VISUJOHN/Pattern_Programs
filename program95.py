''' sample output
* * * * *
  * * * * *
    * * * * *
      * * * * *
        * * * * * '''
n=int(input('Enter no of rows: '))
for i in range(n):
    print(' '*i,end='')
    print('* '*n)
