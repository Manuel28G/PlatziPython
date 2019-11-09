

def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('contrasena es incorrecta')
    return wrapper

@protected
def protected_func():
    print('Tu contrasena es correcta.')


if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contrasena: '))
    protected_func(password)