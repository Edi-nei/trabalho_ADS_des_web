# 7 - Escreva um programa que recebe o número de horas trabalhadas de um funcionário e o
# valor pago por cada hora
# 8 - Calcule quanto ele deverá receber, considerando que se ele trabalhou mais que 40
# horas devemos pagá-lo 1.5 vezes o valor da taxa horária.
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')



horas = float(input("Digite a horas trabalhadas: "))
valor = float(input("Digite o valor da hora: "))
valorpago = 0

if horas > 40:
    valorpago = (valor * horas) * 1.50
    print(f"o valor a ser pago é: ", locale.currency(valorpago, grouping=True))

else:
    valorpago = (valor * horas)
    print(f"o valor a ser pago é: ", locale.currency(valorpago, grouping=True))

