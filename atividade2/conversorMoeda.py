''' 1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais. '''

valorReais = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

valorEmDolar = valorReais / taxaDolar
valorEmEuro = valorReais / taxaEuro

print(f"Valor em Dólares: U$ {valorEmDolar:.2f}")
print(f"Valor em Euros: € {valorEmEuro:.2f}")
