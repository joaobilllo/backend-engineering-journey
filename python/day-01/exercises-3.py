def produto(name, quant, prec): 
    print(f"---Bem Vindo ao mercado do João---")
    print(f"Produto: {name}")
    print(f"Quantidade: {quant}")
    print(f"Valor total: {float(prec) * int(quant)}")

name = input(f"Qual o nome do produto: ")
quant = int(input("Quantidade: "))
prec = float(input("Preço do produto: "))

resultado = produto(name, quant, prec)
