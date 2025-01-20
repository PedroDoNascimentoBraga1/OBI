idades = input() , input() , input() #cria uma tuple
idades = list(idades) #transforma a tuple em array


for cont in range (len(idades)):idades[cont] = int(idades[cont]) #loop para transformar em int, criado no ordenacaonumerica.py em exercícios

if idades[0] >= 5 and idades[0] <= 100 and idades[1] >= 5 and idades[1] <= 100 and idades[2] >= 5 and idades[2] <= 100:

    if idades[0] >= 5 and idades[0] <= 100 and idades[1] >= 5 and idades[1] <= 100 and idades[2] >= 5 and idades[2] <= 100:

        if idades[0] < idades[1] and idades[0] > idades[2] or idades[0] > idades[1] and idades[0] < idades[2]: #idades[0]
            print(idades[0])

        elif idades[1] < idades[0] and idades[1] > idades[2] or idades[1] > idades[0] and idades[1] < idades[2]: #idades[1]
            print(idades[1])

        elif idades[2] < idades[1] and idades[2] > idades[0] or idades[2] > idades[1] and idades[2] < idades[0]: #idades[2]
            print(idades[2])