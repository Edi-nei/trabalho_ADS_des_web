#4 - Escreva um programa que solicite ao usuário uma temperatura Celsius, converta para
#Fahrenheit, e mostre a temperatura convertida.

print("SEJA BEM VINDO, AO NOSSO PROGRAMA CELSIUS -> FAHRENHEIT\n")
temp = float(input("Digite a temperatura em °C: "))

farenheit = (temp * 1.8) + 32

print(f"\nA temperatura é: {farenheit:.1f}°F.")