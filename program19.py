''' sample output
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A '''

n=int(input('Enter no of rows: '))
for i in list(range(1,n+1))[::-1]:
    print(*[chr(j) for j in range(65,65+i)])
