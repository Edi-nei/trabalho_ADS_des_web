#11 - Mostrar os números pares de 0 a 50 utilizando o comando if

for numero in range(0, 51):
    if numero % 2 == 0:
        if numero < 50:
            print(numero, end=" - ") #COLOCA TRAÇO ATE ANTES DO 50
        else:
            print(numero) #MOSTRA SOMENTE O 50

