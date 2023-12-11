from functions import *

while True:
    num1 = float(input("Digite o primeiro valor: "))

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    ask1 = int(input("Digite o número do tipo de operação que deseja realizar: "))

    if ask1 not in [1, 2, 3, 4]:
        print("O valor informado não está disponível na calculadora, favor digitar novamente:")
    else:
        num2 = float(input("Digite o segundo valor: "))

        if ask1 == 1:
            answer = sum(num1, num2)
            print(f"O resultado da soma é {answer}")

        elif ask1 == 2:
            answer = sub(num1, num2)
            print(f"O resultado da subtração é {answer}")

        elif ask1 == 3:
            answer = times(num1, num2)
            print(f"O resultado da multiplicação é {answer}")

        elif ask1 == 4:
            answer = division(num1, num2)
            print(f"O resultado da divisão é {answer}")

        ask2 = input("Deseja realizar mais alguma operação (Sim ou Não)? ")
        if ask2.lower() != "sim":
            break 