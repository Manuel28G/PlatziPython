


def run():
    isPalindrome = False
    while not isPalindrome:
        word = raw_input('Ingrese una palabra palindrome')
        if(word == word[::-1]):
            print('{} es una palbra palindrome'.format(word))
            isPalindrome = True
        else:
            print('{} no es palindrome, vuelve a intentar'.format(word))

if __name__ == "__main__":
    run()