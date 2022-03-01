import bank_account_variables
import utils
import getpass


def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '2':
        withdraw()
    elif option_typed == '10' and bank_account_variables.accounts_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '0':
        pass

def show_balance(account_auth):
    print('Seu saldo é : %s .' % bank_account_variables.accounts_list[account_auth]['value'])

def withdraw():
    value_typed = input('Digite o valor a ser sacado:')
    bank_account_variables.money_slips_user = {}
    value_typed_int = int(value_typed)

    if value_typed_int // 100 > 0 and value_typed_int // 100 <= bank_account_variables.money_slips['100']:
        bank_account_variables.money_slips_user['100'] = value_typed_int // 100
        value_typed_int = value_typed_int - value_typed_int // 100 * 100

    if value_typed_int // 50 > 0 and value_typed_int // 50 <= bank_account_variables.money_slips['50']:
        bank_account_variables.money_slips_user['50'] = value_typed_int // 50
        value_typed_int = value_typed_int - value_typed_int // 50 * 50

    if value_typed_int // 20 > 0 and value_typed_int // 20 <= bank_account_variables.money_slips['20']:
        bank_account_variables.money_slips_user['20'] = value_typed_int // 20
        value_typed_int = value_typed_int - value_typed_int // 20 * 20

    if value_typed_int != 0:
        print('O caixa não tem cédulas disponiveis para este valor')
    else:
        for money_bill_typed in bank_account_variables.money_slips_user:
            bank_account_variables.money_slips[money_bill_typed] -= bank_account_variables.money_slips_user[money_bill_typed]
        print('Retire o seu dinheiro:')
        print(bank_account_variables.money_slips_user)

def insert_money_slips():
    amout_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser incluída: ')
    bank_account_variables.money_slips[money_bill_typed] += int(amout_typed)
    print(bank_account_variables.money_slips)
    utils.clear_screen()

def auth_acconut():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in bank_account_variables.accounts_list and password_typed == bank_account_variables.accounts_list[account_typed]['password']:
        return account_typed
    else:
        return False

def get_menu_option_typed(account_auth):
    print('1 - Saldo')
    print('2 - Saque')
    if bank_account_variables.accounts_list[account_auth]['admin']:
        print('10 - Incluir cédulas')
    print('0 - Sair')
    return input('Escolha uma das opções acima: ')

