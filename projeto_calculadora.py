import os
os.system("cls")

def pedir_numeros() -> list[float]: 
    numeros = []
    entrada = 0
    while entrada != "s":
        try:
            entrada = (input("Digite um número (s - parar): ")).lower()
            if entrada != "s":
                numero = float(entrada)
                numeros.append(numero)
        except ValueError:
            print('Digite apenas números ou "s" para sair')
        except:
            print("Erro inesperado!")
    return numeros

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
    5 - Sair
""")
                
def chamar_funcoes():
    opcao = 0
    
    while opcao != 5:
        menu()
        opcao = int(input("Escolha: "))
        match opcao:
            case 1:
                n1, n2 = pedir_numeros()
                resultado = somar(n1, n2)
                print(f"\nO resultado da soma de {n1} + {n2} = {resultado}\n")
            case 2:
                n1, n2 = pedir_numeros()
                resultado = subtrair(n1, n2)
                print(f"\nO resultado da subtração de {n1} - {n2} = {resultado}\n")
            case 3:
                n1, n2 = pedir_numeros()
                resultado = multiplicar(n1, n2)
                print(f"\nO resultado da multiplicação de {n1} x {n2} = {resultado}\n")
            case 4:
                while True:
                    try:
                        n1, n2 = pedir_numeros()
                        resultado = dividir(n1, n2)
                        print(f"\nO resultado da divisão de {n1} ÷ {n2} = {resultado:.2f}\n")
                    except ZeroDivisionError:
                        print("Não é possível dividir por zero!")
            case 5:
                break
            case _:
                print("Opção inválida\n")

chamar_funcoes()

