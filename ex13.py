#13 - Solicitar um número para o usuário e mostrar a tabuada desse número.


print("TABUADA".center(50, "-"))

numero = int(input("\nDigite o numero da tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}".center(30, "-"))
