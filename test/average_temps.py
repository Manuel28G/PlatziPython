 # -*- coding: utf-8 -*-


def average_temps(temps):
    sum_of_temps = 0
    for temp in temps:
        sum_of_temps += temp
    return sum_of_temps/len(temps)


if __name__ == '__main__':
    temps = list()
    isAdding = True
    arrayLen = int(raw_input('Cuantos números desea agregar: '))
    i = 0
    while(i < arrayLen):
        number = int(raw_input('Ingrese un numero:'))
        temps.append(number)
        i += 1
    average = average_temps(temps)
    print('La temperatura promedio es: {}'.format(average))