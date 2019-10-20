# -*- coding: utf-8 -*-

def run():
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
    number_to_find = int(raw_input('ingresa un número'))
    result = binary_search(numbers, number_to_find ,0 , len(numbers) -1)
    if(result):
        print('Tu numero fue encontrado')
    else:
        print('Tu numero no fue encontrado')
    pass


def binary_search(numbers,number_to_find, low, high ):
        mid = (low + high) / 2
        if low > high:
            return False
        if numbers[mid] == number_to_find:
            return True
        elif numbers[mid] < number_to_find:
            return binary_search(numbers, number_to_find, mid + 1, high)
        else:
            return binary_search(numbers, number_to_find, low, mid - 1)

if __name__ == '__main__':
    run()