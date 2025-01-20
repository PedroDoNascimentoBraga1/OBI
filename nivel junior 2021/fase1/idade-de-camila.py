idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

if idade1 >= 5 and idade1 <= 100 and idade2 >= 5 and idade2 <= 100 and idade3 >= 5 and idade3 <= 100:
    if idade1 < idade2 and idade1 > idade3 or idade1 > idade2 and idade1 < idade3: ##idade1
        print(idade1)

    elif idade2 < idade1 and idade2 > idade3 or idade2 > idade1 and idade2 < idade3: ##idade2
        print(idade2)

    elif idade3 < idade2 and idade3 > idade1 or idade3 > idade2 and idade3 < idade1: ##idade3
        print(idade3)