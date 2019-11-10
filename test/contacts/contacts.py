# -*- coding: utf-8 -*-
from test.contacts.contact_book import ContactBook
from test.contacts.contact import Contact


def run():
    contact_book = ContactBook()
    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Cual es el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            contact_book.add(Contact(name, phone, email))

        elif command == 'ac':
            name = str(raw_input('Cual usuario desea actualizar:'))
            contact_book.update(name)

        elif command == 'b':
            name = str(raw_input('Ingrese el nombre que desea buscar:'))
            contact_book.search(name)

        elif command == 'e':
            name = str(raw_input('Escriba el nombre que desea eliminar: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()