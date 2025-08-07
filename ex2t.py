# EX 1 - Escreva um programa que solicite ao usuário as horas trabalhadas e o
# valor pago por cada hora para calcular o valor a ser pago por suas horas de serviço.


nome = input("Digite seu nome: ")
horas = float(input("Digite quantidade de horas trabalhadas: ")) #Quantidade de horas
valHora = float(input("Digite o valor da hora: ")) #VAlor da hora
valTotal = horas*valHora #calcula o valor

print(f"{nome} voce deve receber: R${valTotal}") # MOSTRA O VALOR TOTAL

print("Programa finalizado.")
input("Pressione Enter para sair...")