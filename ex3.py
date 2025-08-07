#3 - Escreva um script que leia 4 notas de um aluno e imprima a média dele.


nome = input ("Digite seu nome: ")
print("\nSeja bem vindo, vamos calcular sua media!!\n")


n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print  (f"\nSua media é {media:}")

if media >= 7:
    print (f"{nome} você foi aprovado!")
else:
    print (f"{nome} você foi reprovado!")