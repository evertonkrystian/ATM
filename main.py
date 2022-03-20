# ATM
# This code is a basic ATM implementation.
# This made as a product of a Python course.

############# Challenges to implement #############
#
# 1 - Make withdraw value debit on account user - Done
# 2 - Make option to get out of program
# 3 - Make a way to mantain a session
# 4 - Turn method to calc banknotes in a function - Done

import utils
import operations

def main():
    utils.header()
    account_auth = operations.auth_acconut()

    if account_auth:
        utils.clear_screen()
        utils.header()
        option_typed = operations.get_menu_option_typed(account_auth)
        operations.do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')

if __name__ == '__main__':
    while True:
        main()
        input('Aperte <ENTER> para continuar.')  # Pause do programa.
        utils.clear_screen()