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
        ___|___''', '''        _______
        |      |
        |     (_)
        |     /|\
        |      |
        |     / 
        |
     ___|___''', '''        _______
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

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print(hidden_word)
    print('---- * -----' * 3)


def run():
    word = random_word()
    hidden_word = ['-'] * len(WORDS)
    tries = 0
    while(True):
        display_board(hidden_word,tries)
        user_word = raw_input('escoge una letra:')
        if(word)
        break


if __name__ == '__main__':
    print('A H O R C A D O')
    run()