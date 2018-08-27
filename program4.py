''' sample output
A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J'''

n=int(input('Enter no of rows: '))
a=65
for i in range(n):
    print((chr(a)+' ')*n)
    a+=1
