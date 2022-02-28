# ATM
# This code is basic ATM implementation.
# This made as a product of a Python course.


######## Problems to solve ###########
#1 - debito em conta no saque.
#2 - verificar saldo disponível.
from builtins import input

import getpass
import os


############### Functions ####################
def cabecalho():
    print('******************************************')
    print('************ CAIXA ELETRÔNICO ************')
    print('******************************************')

def menu():
    print('1 - Saldo')
    print('2 - Saque')
    if accounts_list[account_typed]['admin']:
        print('10 - Incluir cédulas')
    print('0 - Sair')

# def checa_nova_opcao():
#     new_option_typed = input('Deseja ralizar outra operação? 1 - Sim / 2 - Não')
#     if new_option_typed == '1':
#         limpar_tela()
#         cabecalho()
#         menu()
#     elif new_option_typed == '2

def limpar_tela():
    # if os.name == 'nt':
    #     os.system('cls') # Executa se Windows
    # else:
    #     os.system('clear') # Executa se Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def incluir_cedulas(qt_cedulas,valor_cedula):
    amount_typed = input('Digite a quantidade de cédulas:')
    money_bill_typed = input('Digite a cédula a ser incluída:')


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

############### Program ####################
while True:
    cabecalho()
    account_typed = input('Digite sua conta: ')
    print(account_typed)
    password_typed = getpass.getpass('Digite sua senha: ')
    print(password_typed)



    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        limpar_tela()
        cabecalho()
        menu()
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            #print('Seu saldo é :' + accounts_list[account_typed]['value'])
            limpar_tela()
            print('Seu saldo é : %s .' % accounts_list[account_typed]['value'])
            #checa_nova_opcao()
            input('Aperte <ENTER> para continuar.') #Pause do programa.
            limpar_tela()
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
                input('Aperte <ENTER> para continuar.')  # Pause do programa.
            else:
                for money_bill_typed in money_slips_user:
                    money_slips[money_bill_typed] -= money_slips_user[money_bill_typed]
                print('Retire o seu dinheiro:')
                print(money_slips_user)
                input('Aperte <ENTER> para continuar.')  # Pause do programa.

            
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amout_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser incluída: ')
            #money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amout_typed)
            money_slips[money_bill_typed] += int(amout_typed)
            print(money_slips)
            limpar_tela()
        elif option_typed == '0':
            continue

    else:
        print('Conta inválida')
        input('Aperte <ENTER> para continuar.') #Pause do programa.