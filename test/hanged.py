import random

IMAGES = [
     '''        _______
        |      |
        |     
        |     
        |     
        |     
        |
     ___|___''',
     '''        _______
        |      |
        |     (_)
        |     
        |     
        |     
        |
     ___|___''',
     '''        _______
        |      |
        |     (_)
        |     /|
        |     
        |     
        |
     ___|___''',
     '''        _______
        |      |
        |     (_)
        |     /|\
        |     
        |     
        |
     ___|___''',
     '''        _______
        |      |
        |     (_)
        |     /|\
        |      |
        |     /
        |
     ___|___''',
     '''        _______
        |      |
        |     (_)
        |     /|\
        |      |
        |     / \
        |
     ___|___'''

 ]

WORDS = ['palabras',
         'lavadora',
         'secadora',
         'diputado',
         'venezuela',
         'chile']


def random_word():
    index = random.randint(0, len(WORDS) - 1)
    return WORDS[index]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print(hidden_word)
    print('---- * -----' * 3)


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while(True):
        display_board(hidden_word,tries)
        user_word = raw_input('escoge una letra:')
        letter_indexes = []
        for index in range(len(word)):
            if word[index] == user_word:
                letter_indexes.append(index)
        if letter_indexes == []:
            tries += 1
        else:
            for index in letter_indexes:
                hidden_word[index] = user_word

        if tries == len(IMAGES):
            print('Has perdido!')
            print('La palabra correcta era {}'.format(word))
            break
        elif not hidden_word.__contains__('-'):
            print('Has ganado!')
            print('Felicitaciones! la palabra es {}'.format(word))
            break

if __name__ == '__main__':
    print('A H O R C A D O')
    run()