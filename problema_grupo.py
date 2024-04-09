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


def sum():
    valor1 = float(input("Digite o primeiro valor: "))
    
    valor2 = float(input("Digite o segundo valor: "))
    
    print(f'A soma dos dois valores é: {valor1 + valor2}')   
    
    return None