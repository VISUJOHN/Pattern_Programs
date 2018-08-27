
''' sample output
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A '''

n=int(input('Enter no of rows: '))
a=n
while a>0:
    print(*[chr(i) for i in list(range(65,65+n))[::-1]])
    a-=1
