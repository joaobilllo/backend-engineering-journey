print(f"---Exercício 2---")

def calculadora(num1, num2, operation):
    if operation == "+" : 
        return num1 + num2 
    elif operation == "-":
        return num1 - num2
    elif operation == "*" or operation == "x":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else: 
        return 0

num1 = float(input(f"Digite o primeiro número: "))
num2 = float(input(f"Digite o segundo número: "))
operation = input(f"Qual é a operação: ")

resultado = calculadora(num1, num2, operation)

print(f"O resultado da sua operação é: {resultado}")
    