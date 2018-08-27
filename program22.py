''' sample output
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A '''

n=int(input('Enter no of rows: '))
a=65+n-1
for i in list(range(1,n+1))[::-1]:
    print((chr(a)+' ')*i)
    a-=1
