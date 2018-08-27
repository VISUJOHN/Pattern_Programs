''' sample output
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A '''

n=int(input('Enter no of rows: '))
a=65+n-1
for i in range(n):
    print((chr(a)+' ')*n)
    a-=1
