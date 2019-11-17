import csv

from test.contacts.contact import Contact


class ContactBook:

    def __init__(self):
        self._contacts = []
        self._read_contacts()

    def add(self, contact):
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('-- * -- * -- * -- * -- * -- * -- *')
        print('Nombre: {}'.format(contact.name))
        print('Correo: {}'.format(contact.email))
        print('Telefono: {}'.format(contact.phone))

    def _not_found(self):
        print('-- * -- * -- * -- * -- * -- * -- *')
        print('Contacto no encontrado')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                return
        self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _read_contacts(self):
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                else:
                    self.add(Contact(row[0], row[1], row[2]))

    def _get_response(self):
        print('-- * -- * -- * -- * -- * --')
        print('[s]i')
        print('[n]o')
        response = str(raw_input())
        if response.lower().__contains__('s') or response.lower().__contains__('y'):
            return True
        if response.lower().__contains__('n'):
            return False
        else:
            print('no se entiende la respuesta por favor repitala')

    def update(self,name):
        for contact in self._contacts:
            if  contact.name.lower() == name.lower():
                    print('desea cambiar  el nombre de {}'.format(contact.name))
                    if self._get_response():
                        contact.name = str(raw_input('Ingrese el nuevo nombre: '))
                    print('desea cambiar  el email : {}'.format(contact.email))
                    if self._get_response():
                        contact.email = str(raw_input('Ingrese el nuevo email: '))
                    print('desea cambiar  el telefono: {}'.format(contact.phone))
                    if self._get_response():
                        contact.phone = str(raw_input('Ingrese el nuevo telefono: '))
