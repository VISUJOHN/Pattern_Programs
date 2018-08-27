''' sample output
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J '''

n=int(input('Enter no of row: '))
a=65
for i in list(range(1,n+1))[::-1]:
    print((chr(a)+' ')*i)
    a+=1
