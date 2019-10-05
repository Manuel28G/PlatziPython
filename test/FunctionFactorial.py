# -*- coding: utf-8 -*-


def factorial(number):
    if(number == 0):
        return 1
    else:
        return number * factorial(number - 1)


def run():
    number = int(raw_input('Ingrese el numero que desee calcular su factorial:'))
    print(factorial(number))


if __name__ == '__main__':
    run()