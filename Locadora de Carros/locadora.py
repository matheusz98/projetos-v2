import os

# lista de carros
carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]

alugados = []


# mostrar carros
def mostrar_carros(lista_carros):
    # percorre a lista de carros
    for i, car in enumerate(lista_carros):
        print("[{}] {} - R$ {} / dia.".format(i, car[0], car[1]))


while True:
    os.system("cls")
    print("Bem-vindo à locadora de carros!")
    print("0 - Listar carros | 1 - Alugar um carro | 2 - Devolver um carro")
    print("O que deseja fazer?")
    opcao = int(input())

    os.system("cls")

    # lista
    if opcao == 0:
        mostrar_carros(carros)

    # aluga
    elif opcao == 1:
        mostrar_carros(carros)
        print("Qual carro deseja alugar?")

        carro_escolhido = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())

        os.system("cls")

        print("Você escolheu {} por {} dias.".format(carros[carro_escolhido][0], dias))
        print("Total do aluguel: R$ {}. Deseja continuar?".format(dias * carros[carro_escolhido][1]))
        
        print("0 - SIM | 1 - NÃO")
        confirma = int(input())
        if confirma == 0:
            print("Parabéns! Você alugou o {} por {} dias".format(carros[carro_escolhido][0], dias))
            alugados.append(carros.pop(carro_escolhido))

    # devolve
    elif opcao == 2:
        if len(alugados) == 0:
            print("Não há carros a serem devolvidos.")
        else:
            print("Lista de carros alugados:")
            mostrar_carros(alugados)

            print("Qual carro deseja devolver?")
            print("Digite o código referente ao carro alugado: ")
            cod_alugado = int(input())

            if confirma == 0:
                print("Obrigado por devolver o carro {}".format(alugados[cod_alugado][0]))
                carros.append(alugados.pop(carro_escolhido))

    print("0 - CONTINUAR | 1 - SAIR ")
    if int(input()) == 1:
        os.system("cls")
        break
