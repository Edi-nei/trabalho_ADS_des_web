#14 - Mostrar os números primos de 2 até o número digitado pelo usuário.

print("BEM VINDO".center(30, "-"))

n = int(input("Digite um número: "))# Solicita o número ao usuário



def n_primo(n):
    if n < 2:
        print(" Números menores que 2 não são primos.")
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#VERIFICA SE O NUMERO É MAIOR QUE DOIS
if n < 2:
    print(" Números menores que 2 não são primos...")
else: # SE É MAIOR SEGUE AQUI
    print(f"Números primos de 2 até {n}:")
    for num in range(2, n + 1):
        if n_primo(num):
            print(num)