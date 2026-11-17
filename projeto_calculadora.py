import os
os.system("cls")

def pedir_numeros(minimo: int = 2) -> list[float]:
    numeros = []
    entrada = 0
    while entrada != "s":
        try:
            entrada = (input("Digite um número (s - parar): ")).lower()
            if entrada != "s":
                numero = float(entrada)
                numeros.append(numero)
            elif len(numeros) < minimo:
                print("Digite ao menos dois números!")
                entrada = "" # Variável entrada passa a ter nenhum valor
                continue
        except ValueError:
            print('Digite apenas números ou "s" para sair')
        except:
            print("Erro inesperado!")
    return numeros 

def receber_numeros(ultimo_resultado: float | None) -> list[float]:
    lista_digitados = [] # Lista para receber mais numeros

    if ultimo_resultado is not None:
            usar_resultado = input("Utilizar o último resultado? (s/n): ").lower()

            if usar_resultado == "s":
                lista_digitados.append(ultimo_resultado) # Adiciona a lista o resultado da ultima operação feita
                lista_digitados.extend(pedir_numeros(minimo=1)) # Para ao inves de transformar os novos numeros digitados em uma nova lista usa-los separadamente e adiciona-los à lista + altera a variavel minimo para que possa receber apenas um valor 
            else:
                lista_digitados = pedir_numeros() # Caso o usuario não queira reultilizar o ultimo valor, mais ainda continuar no programa

    else:
        lista_digitados = pedir_numeros() # Caso não tenha nenhum valor no resultado o usuario fará a operação com o primeiro número
    return lista_digitados

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
    ultimo_resultado = None
    while opcao != 5:
        menu()
        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas o número da opção escolhida!")
        match opcao:
            case 1:
                lista_digitados = receber_numeros(ultimo_resultado)
                resultado = somar(lista_digitados)
                print(f"\nO resultado da soma dos números = {resultado}\n")
                ultimo_resultado = resultado
            case 2: 
                lista_digitados = receber_numeros(ultimo_resultado)
                resultado = subtrair(lista_digitados)
                print(f"\nO resultado da subtração dos números = {resultado}\n")
                ultimo_resultado = resultado
            case 3:
                lista_digitados = receber_numeros(ultimo_resultado)
                resultado = multiplicar(lista_digitados)
                print(f"\nO resultado da multiplicação dos números = {resultado}\n")
                ultimo_resultado = resultado
            case 4:
                    try:
                        lista_digitados = receber_numeros(ultimo_resultado)
                        resultado = dividir(lista_digitados)
                        print(f"\nO resultado da divisão dos números = {resultado:.2f}\n")
                        ultimo_resultado = resultado
                    except ZeroDivisionError:
                        print("Não é possível dividir por zero!")
            case 5:
                break
            case _:
                print("Opção inválida\n")

chamar_funcoes()

