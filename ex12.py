#12 - Mostrar a soma dos números pares múltiplos de 4 entre 1 e 500.
print()
print("MULTIPLOS DE 4 ENTRE 1 A 500".center(50, "-"))


soma = 0

for numero in range(1, 501):
    if numero % 4 == 0:
      soma += numero

print(f"\nA soma dos múltiplos de 4 entre 1 e 500 é: \033[31m{soma}\033[m")# \033[31m{soma}\033[m é a formula para a cor vermelha, para DESTACAR


