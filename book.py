import pickle
import os

class Contact(object):

    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone

    def __str__(self):
        return "{} {}".format(self.name, self.phone)


class Data(object):

    def __init__(self, database):
        self.database = database
        self.contacts = {}
        if not os.path.exists(self.database):
            f = open(self.database, 'wb')
            pickle.dump({}, f)
            f.close()
        else:
            with open(self.database, 'rb') as contacts_list:
                self.contacts = pickle.load(contacts_list)

    def add_contact(self):

        name = input("Имя: ")
        phone = input("Телефон:")
        if name not in self.contacts:
            self.contacts[name] = Contact(name, phone)
        else:
            print('Такой контакт уже есть')


    def show_book(self):
        if self.contacts:
            print('{} {}'.format('name', 'phone'))
            for contact in self.contacts.values():
                print(contact)

    def search_name(self):
        name = input("Напишите имя: ")
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print('Такого абонента нет')

    def change_contact(self):
        name = input("Напишите имя: ")
        if name in self.contacts:
            print('Этот абонент существует')
            name = input("Имя: ")
            phone = input("Телефон:")
            self.contacts[name].__init__(name, phone)
            print('Успешно изменен')



    def delete(self):
        name = input("Введите имя абонента для удаления")
        if name in self.contacts:
            del self.contacts[name]
            print('Удалить контакт')
        else:
            print('Такого абонента здесь нет')

    def __del__(self):
        with open(self.database, 'wb') as db:
            pickle.dump(self.contacts, db)

    def reset(self):
        self.contacts = {}

    def __str__(self):
        print('''
1. Добавить контакт
2. Просмотреть справочник
3. Поиск по имени
4. Изменить контакт
5. Удалить контакт
''')



def main():
    app = Data('abonents.data')
    act = ''
    while act != '7':
        print(app)
        act = input('Выберите ')
        if act == '1':
            app.add_contact()
        elif act == '2':
            app.show_book()
        elif act == '3':
            app.search_name()
        elif act == '4':
            app.change_contact()
        elif act =='5':
            app.delete()
        else:
            print('Такой опции нет')


if __name__ == '__main__':
    main()


