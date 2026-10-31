import os
os.system("cls")
'''
Criando as funções passando como parâmetro dois valores e retornando o resultado do calculo pra que possa ser usa posteriormente com o "evoluir" do projeto.

O pedido dos dois valores serão pedidos dentro da função chamar funções (o menu) e as variaveis preenchidas pelo usuario serão passadas como parametro 
'''
def somar(a: float, b: float) -> float:
    soma = a + b                    
    return soma 

def subtrair(a: float, b: float) -> float:
    subtracao = a - b
    return subtracao

def multiplicar(a: float, b: float) -> float:
    multiplicacao = a * b
    return multiplicacao

def dividir(a: float, b: float) -> float:
    divisao = a / b
    return divisao

def menu():
    print(""" ===== CALCULADORA =====

    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
""")
    opcao = input("Escolha: ")

    match opcao:
        case "1":
            n1 = float(input("\nNúmero 1: "))
            n2 = float(input("Número 2: "))
            resultado = somar(n1, n2)
            print(f"\nO resultado da soma de {n1} + {n2} = {resultado}")
        case "2":
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
            resultado = subtrair(n1, n2)
            print(f"\nO resultado da subtração de {n1} - {n2} = {resultado}")
        case "3":
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
            resultado = multiplicar(n1, n2)
            print(f"\nO resultado da multiplicação de {n1} x {n2} = {resultado}")
        case "4":
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
            resultado = dividir(n1, n2)
            print(f"\nO resultado da divisão de {n1} ÷ {n2} = {resultado}")
        case _:
            print("Opção inválida")

            
menu()