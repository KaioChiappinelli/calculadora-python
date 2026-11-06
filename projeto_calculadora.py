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
            elif len(numeros) < 2:
                print("Digite ao menos dois números!")
                entrada = "" # Variável entrada passa a ter nenhum valor
                continue
        except ValueError:
            print('Digite apenas números ou "s" para sair')
        except:
            print("Erro inesperado!")
    return numeros 

def somar(valores: list[float]) -> float:
    soma = 0 
    for numero in valores:
        soma += numero
    return soma

def subtrair(valores: list[float]) -> float:
    subtracao = valores[0] # Para que a variavel subtracao inicia com o primeiro elemento da lista e subtrair com o proximo
    for numero in valores[1:]: # Para o loop começar do segundo elemento ja que a variavel subtracao guarda o primeiro
        subtracao -= numero
    return subtracao

def multiplicar(valores: list[float]) -> float:
    multiplicacao = 1
    for numero in valores:
        multiplicacao *= numero
    return multiplicacao

def dividir(valores: list[float]) -> float:
    divisao = valores[0]
    for numero in valores[1:]:
        divisao /= numero 
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
        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas o número da opção escolhida!")
        
        match opcao:
            case 1:
                lista_digitados = pedir_numeros()
                resultado = somar(lista_digitados)
                print(f"\nO resultado da soma dos números = {resultado}\n")
            case 2: 
                lista_digitados = pedir_numeros()
                resultado = subtrair(lista_digitados)
                print(f"\nO resultado da subtração dos números = {resultado}\n")
            case 3:
                lista_digitados = pedir_numeros()
                resultado = multiplicar(lista_digitados)
                print(f"\nO resultado da multiplicação dos números = {resultado}\n")
            case 4:
                    try:
                        lista_digitados = pedir_numeros()
                        resultado = dividir(lista_digitados)
                        print(f"\nO resultado da divisão dos números = {resultado:.2f}\n")
                    except ZeroDivisionError:
                        print("Não é possível dividir por zero!")
            case 5:
                break
            case _:
                print("Opção inválida\n")

chamar_funcoes()

