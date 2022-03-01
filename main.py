# ATM
# This code is a basic ATM implementation.
# This made as a product of a Python course.


######## Problems to solve ###########
#1 - debito em conta no saque.
#2 - verificar saldo disponível.
from builtins import input

import getpass
import os


############### Variables ####################
accounts_list = {
        '0001-02': {
        'password':'123456',
        'name':'Everton Krystian',
        'value': 100,
        'admin': False
    },
        '0002-02':{
        'password':'123456',
        'name':'Krystian Rodrigues',
        'value': 50,
        'admin': False
    },
        '0003-02':{
        'password':'123456',
        'name':'Admin Rodrigues',
        'value': 1000,
        'admin': True
    }
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

def main():
    header()
    account_auth = auth_acconut()

    if account_auth:
        clear_screen()
        header()

        option_typed = get_menu_option_typed(account_auth)
        if option_typed == '1':
            clear_screen()
            print('Seu saldo é : %s .' % accounts_list[account_auth]['value'])
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado:')
            money_slips_user = {}
            value_typed_int = int(value_typed)

            if value_typed_int // 100 > 0 and value_typed_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_typed_int // 100
                value_typed_int = value_typed_int - value_typed_int // 100 * 100

            if value_typed_int // 50 > 0 and value_typed_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_typed_int // 50
                value_typed_int = value_typed_int - value_typed_int // 50 * 50

            if value_typed_int // 20 > 0 and value_typed_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_typed_int // 20
                value_typed_int = value_typed_int - value_typed_int // 20 * 20



            if value_typed_int != 0:
                print('O caixa não tem cédulas disponiveis para este valor')
            else:
                for money_bill_typed in money_slips_user:
                    money_slips[money_bill_typed] -= money_slips_user[money_bill_typed]
                print('Retire o seu dinheiro:')
                print(money_slips_user)

        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amout_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')
            money_slips[money_bill_typed] += int(amout_typed)
            print(money_slips)
            clear_screen()
        # elif option_typed == '0':
        #     continue

    else:
        print('Conta inválida')



def auth_acconut():
    account_typed = input('Digite sua conta: ')
    #print(account_typed)
    password_typed = getpass.getpass('Digite sua senha: ')
    #print(password_typed)

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False

def header():
    print('******************************************')
    print('************ CAIXA ELETRÔNICO ************')
    print('******************************************')

def get_menu_option_typed(account_auth):
    print('1 - Saldo')
    print('2 - Saque')
    if accounts_list[account_auth]['admin']:
        print('10 - Incluir cédulas')
    print('0 - Sair')
    return input('Escolha uma das opções acima: ')

# def checa_nova_opcao():
#     new_option_typed = input('Deseja ralizar outra operação? 1 - Sim / 2 - Não')
#     if new_option_typed == '1':
#         clear_screen()
#         header()
#         get_menu_option_typed()
#     elif new_option_typed == '2

def clear_screen():
    # if os.name == 'nt':
    #     os.system('cls') # Executa se Windows
    # else:
    #     os.system('clear') # Executa se Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_ballots(qt_cedulas,valor_cedula): ############ A implementar
    amount_typed = input('Digite a quantidade de cédulas:')
    money_bill_typed = input('Digite a cédula a ser incluída:')





while True:
    main()
    input('Aperte <ENTER> para continuar.')  # Pause do programa.
    clear_screen()