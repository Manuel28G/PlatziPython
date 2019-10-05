# -*- coding: utf-8 -*-


def run():
    print('Verificar si es primo')
    number = int(raw_input('Escribe un numero:'))
    result = is_prime(number)
    if result is True:
        print('El número es primo')
    else:
        print('El número no es primo')


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True
    


if __name__ == '__main__':
    run()