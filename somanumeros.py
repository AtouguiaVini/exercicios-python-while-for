# João recebeu uma lista de valores representando as receitas de sua loja de roupas. Ele quer calcular a soma total dessas receitas para entender o desempenho financeiro semanal.

valores = [10, 20, 30, 40, 50]

# Crie um programa que ajude João a calcular o valor total.

resultado = 0

for valor in valores:
    resultado += valor

print(f'A soma das receitas é: {resultado}')
