import random
import string

password_lenght = int(input("Informe o tamanho desejado para a senha: "))


def password_generator(password_lenght):
    ascii_options = string.ascii_letters
    number_options = string.digits
    symbol_options = string.punctuation

    options = ascii_options + number_options + symbol_options

    generated_password = ""

    for i in range(0, password_lenght):
        digit = random.choice(options)
        generated_password = generated_password + digit

    return generated_password


new_password = password_generator(password_lenght)
print("Senha gerada: {}".format(new_password))
