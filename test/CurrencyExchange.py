

def run ():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos Mexicanos a pesos colombianos')
    print('')
    ammount = float(raw_input('Cantidad de pesos Mexicanos:'))
    result = foreign_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * ammount

if __name__ == '__main__':
    run()