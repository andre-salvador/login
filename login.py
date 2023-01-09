from os import system
from time import sleep

from stdiomask import getpass


def login():
    username = input('Usuário: ')
    password = getpass('Senha: ', mask='*')

    return username, password


def checagem(username, password):
    usuarios = []
    with open('conta.txt', 'r+', encoding='UTF-8', newline='') as arquivo:  # noqa E501
        for linha in arquivo:
            linha = linha.strip(',')
            usuarios.append(linha.split())

        if len(usuarios) == 0:
            return False

        for usuario in usuarios:
            user = usuario[0]
            code = usuario[1]

            if user == username and code == password:
                return username
            else:
                return False


def cadastro():
    username, password = login()

    if username == password:
        print('\nNome de usuário e senha não podem ser iguais!\n')

    elif username == '':
        print('\nDigite um usuário válido!\n')

    elif password == '':
        print('\nDigite uma senha válida!\n')

    else:
        teste = checagem(username, password)
        if teste:
            print('\nUsuário já está cadastrado\n')
            sleep(2)

        else:
            with open('conta.txt', 'a+', encoding='UTF-8', newline='') as arquivo:  # noqa E501
                arquivo.writelines(f'{username} {password}\n')
                print('\nUsuário cadastrado com sucesso!!\n')
                sleep(2)


if __name__ == '__main__':

    while True:
        system('cls')

        print('-=' * 10)
        print('1- Cadastro \n2- Login\n3- Sair\n')
        print('-=' * 10)

        escolha = int(input('Digite uma opção: '))

        try:
            if escolha == 1:
                cadastro()

            elif escolha == 2:
                usuario, senha = login()
                entrar = checagem(usuario, senha)

                if entrar:
                    print(f'Bem- Vindo {usuario}')
                    sleep(2)

                else:
                    print('Senha e/ou usuário inválido!!')
                    sleep(2)

            elif escolha == 3:
                print('Obrigado por testar meu Programa! Tchau!!')

            else:
                print('Digite um número de 1 à 3!')

        except ValueError:
            print('Digite apenas as opções validas!!!')
