''' sample output
    *
   * *
  *   *
 *     *
*       * '''

n=int(input('Enter no of rows: '))
for i in range(n):
    if i==0:
        print(' '*(n-i),end='')
        print('*')
    else:
        print(' '*(n-i),end='')
        print('*',end='')
        print(' '*(2*i-1),end='')
        print('*')
