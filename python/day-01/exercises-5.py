def divisao(num1, num2): 
    print(f"Divisão normal: {float(num1 / num2)}")
    print(f"Divisão inteira: {float(num1 // num2)}")
    print(f"Resto da divisão: {float(num1 % num2)}")
    print(f"Exponenciação: {float(num1 ** num2)}")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = divisao(num1, num2)