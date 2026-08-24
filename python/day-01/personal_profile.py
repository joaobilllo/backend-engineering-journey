def resumo(name, age, city, profession, available_hours):
    print(f"Olá, {name}")
    print(f"Você tem {int(age)} anos e mora em {city}.")
    print(f"Você possui {available_hours} horas disponíveis para estudar por semana.")
    print(f"Você trabalha como {profession}.")
    print(f"Daqui 5 anos você terá: {int(age) + 5}")


print("--- RESPONDA ÀS PERGUNTAS ---")

name = input("Qual é o seu nome? ")
age = int(input("Quantos anos você tem? "))
profession = input("Com o que você trabalha? ")
city = input("Em que cidade você mora? ")
available_hours = input("Quantas horas por semana você tem disponíveis para estudar? ")

resumo(name, age, city, profession, available_hours)