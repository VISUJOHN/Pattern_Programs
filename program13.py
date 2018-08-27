''' sample output
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J '''

n=int(input('Enter no of rows: '))
a=65
for i in range(1,n+1):
    print((chr(a)+' ')*i)
    a+=1
#    print(*[chr(j) for j in range(65,65+i+1)])
