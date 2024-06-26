def get_numbers():
    """
    Solicita ao usuário dois numeros e retorna uma tupla.

    Returns:
        numbers: tupla que armazena os dois valores digitados pelo usuário.
    """
    try:
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
        numbers = (number1, number2)
        return numbers
    except:
        print("Entrada inválida!")
        get_numbers()

def show_result(operation, number1, number2, result):
    """
    Exibe na tela os dois números fornecidos e o resultado.

    Args:
        operation (string): Operação que foi realizada.
        number1 (float): O primeiro número.
        number2 (float): O segundo número.
        result (float): O resultado da operação. 
    """
    print("A {} de {:g} por {:g} é: {:g}".format(operation, number1, number2, result))

def subtraction():
    """
    Realiza subtração entre dois números e mostra o resultado na tela

    """

    print("-------Subtração--------")
    numbers = get_numbers()
    result = numbers[0] - numbers[1]
    show_result("subtraction", numbers[0], numbers[1], result)

def multiplication():
    """
    Realiza multiplicação entre dois números e mostra o resultado na tela
    """
    print("--------- Multiplicação ---------")
    numbers = get_numbers()
    result = numbers[0] * numbers[1]
    show_result("multiplicação", numbers[0], numbers[1], result)

def division():
    """
    Realiza divisão entre dois números e mostra o resultado na tela
    """
    print("Divisão")
    numbers = get_numbers()
    try:
        result = numbers[0] / numbers[1]
        show_result("divisão", numbers[0], numbers[1], result)
    except ZeroDivisionError:
        print("Impossível dividir por zero")
        division()

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
    resultado = valor1 + valor2    
    print('A soma dos dois valores é: ', resultado)   
    
def divisao():
    dividendo = float(input("Digite o dividendo: "))
    divisor = float(input("Digite o divisor: "))

    if divisor != 0:
        resultado = dividendo / divisor
        print("O resultado da divisão é:", resultado)
    else:
        print("Não é possível dividir por zero.")

divisao()

menu()
