import os

def header():
    print('******************************************')
    print('************ CAIXA ELETRÔNICO ************')
    print('******************************************')

def clear_screen():
    # if os.name == 'nt':
    #     os.system('cls') # Executa se Windows
    # else:
    #     os.system('clear') # Executa se Linux
    os.system('cls' if os.name == 'nt' else 'clear')