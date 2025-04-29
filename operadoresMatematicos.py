try:
    Numero1 = int(input("Escolha o primeiro número: "))
except ValueError:
    print("Por favor, digite um número.")
    exit()

try:
    Numero2 = int(input("Escolha o segundo número: "))
except ValueError:
    print("Por favor, digite um número.")
    exit()

soma = Numero1 + Numero2
subtracao = Numero1 - Numero2
multiplicacao = Numero1 * Numero2

# Tratando divisão por zero
if Numero2 != 0:
    divisao = Numero1 / Numero2
else:
    divisao = "indefinida (divisão por zero)"

print(f"Esta é a soma entre os números: {soma}")
print(f"Esta é a diferença entre os números: {subtracao}")
print(f"Este é o produto entre os números: {multiplicacao}")
print(f"Este é o quociente entre os números: {divisao}")
