''' 2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes. '''

nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20

valorDesconto = precoOriginal * (porcentagemDesconto / 100)
precoFinal = precoOriginal - valorDesconto

print(f"Nome do produto: {nomeProduto}")
print(f"Preço Original: R$ {precoOriginal:.2f}")
print(f"Porcentagem de Desconto: {porcentagemDesconto}%")
print(f"Valor do Desconto: R$ {valorDesconto:.2f}")
print(f"Preço Final: R$ {precoFinal:.2f}")

