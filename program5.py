''' Sample output
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J'''

n=int(input('Enter no of rows: '))
a=65
for i in range(n):
    print(*[chr(j) for j in list(range(65,65+n))])
