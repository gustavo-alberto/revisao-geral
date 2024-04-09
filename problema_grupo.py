def menu():
    print("--------------------------------")
    print("Calculadora simples")
    print("--------------------------------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("--------------------------------")
    
    try:
        option = int(input("Digite a opção desejada: "))
        if option == 1:
            sum()
        elif option == 2:
            subtraction()
        elif option == 3:
            multiplication()
        elif option == 4:
            division()
        elif option == 0:
            print("Obrigado por utilizar a calculadora")
            print("\n")
        else:
            raise Exception
    except:
        print("Opção inválida")
        print("\n")


def somar(a, b):
    """
    Esta função calcula a soma de dois valores.
    
    Argumentos:
    a (float or int): O primeiro número a ser somado.
    b (float or int): O segundo número a ser somado.
    
    Retorna:
    float or int: A soma de a e b.
    """
    resultado = a + b
    return resultado