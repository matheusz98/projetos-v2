import os

print("0: Adição")
print("1: Subtração")
print("2: Multiplicação")
print("3: Divisão")
print("4: Exponenciação")

os.system("cls")
opcao = int(input("Digite a opção desejada: "))

if opcao == 0:
    os.system("cls")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("Resultado: ", num1 + num2)

elif opcao == 1:
    os.system("cls")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("Resultado: ", num1 - num2)

elif opcao == 2:
    os.system("cls")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("Resultado: ", num1 * num2)

elif opcao == 3:
    os.system("cls")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    if num2 == 0:
        print("Não é possível dividir por 0")
    else:
        print("Resultado: ", num1 / num2)

elif opcao == 4:
    os.system("cls")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    print("Resultado: ", num1 ** num2)
else:
    print("Opção inválida")
