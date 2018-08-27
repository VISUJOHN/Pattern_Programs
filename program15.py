''' sample output
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
* '''

n=int(input("Enter no of row: "))
for i in list(range(1,n+1))[::-1]:
    print(('* '*i).strip())
