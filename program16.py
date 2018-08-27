''' sample output
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6
7 7 7 7
8 8 8
9 9
10 '''

n=int(input('Enter no of rows: '))
a=1
for i in list(range(1,n+1))[::-1]:
    print(((str(a)+' ')*i).strip())
    a+=1
