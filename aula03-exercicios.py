# EX 2

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# EX 3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais")

# EX 4

nota_final = 4

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")

# EX 5

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

if A % B == 0 or B % A == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")

# EX 6

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        resultado = None
else:
    print("Operação inválida")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)



