''' sample output
J I H G F E D C B A
J I H G F E D C B
J I H G F E D C
J I H G F E D
J I H G F E
J I H G F
J I H G
J I H
J I
J '''

n=int(input('Enter no of row: '))
for i in list(range(1,n+1))[::-1]:
    print(*[chr(j) for j in list(range(65+n-i,65+n))[::-1]])

 
