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

def subtraction():
    print("Você escolheu Subtração!")
    print("\n")
    num_1 = input("Digite o primeiro valor: ")
    num_2 = input("Digite o segundo valor: ")
    result = num_1 - num_2

    print(f'O resultado de {num_1} + {num_2} = {result}')