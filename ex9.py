#9 - Uma determinada loja está fazendo promoções de vendas. Qualquer compra que um
# cliente fizer até R$ 100,00 receberá 5% de descontos. Se a compra for maior que R$
#100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior ou igual a R$
#200,00, o desconto será de 20%
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print()
print("CALCULO DE DESCONTOS".center(40, "-"))

valorCompra = float(input("\nDigite o valor da compra: "))
print()
if valorCompra < 100:
    valordesconto = valorCompra * 0.05
    valorCompra =  valorCompra - valordesconto
    print(f"O valor da compra com desconto é: ", locale.currency(valorCompra, grouping=True))
elif valorCompra < 200:
    valordesconto = valorCompra * 0.1
    valorCompra = valorCompra - valordesconto
    print(f"O valor da compra com desconto é: ", locale.currency(valorCompra, grouping=True))
else:
    valordesconto = valorCompra * 0.2
    valorCompra = valorCompra - valordesconto
    print(f"O valor da compra com desconto é: ", locale.currency(valorCompra, grouping=True))
print()
print("FIM DO CALCULO".center(40, "-"))









