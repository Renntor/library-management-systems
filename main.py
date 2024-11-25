import os.path

from utils import add_book, get_book, retrieve_book, delete_book, update_book

if __name__ == '__main__':
    bd = 'bd.json'
    if os.path.exists(bd) is False:
        with open('bd.json', 'w', encoding='utf-8') as file:
            file.write(
                '[]'
            )

    action = input(
        '\nВведите действие, которое хотите сделать.'
        '\n1: Добавить книгу'
        '\n2: Все книги'
        '\n3: Найти книгу'
        '\n4: Удалить книгу'
        '\n5: Обновить книгу'
        '\n6: Закрыть программу\n'

    )
    if action == '1':
        print(add_book(bd))
    elif action == '2':
        print(get_book(bd))
    elif action == '3':
        print(retrieve_book(bd))
    elif action == '4':
        print(delete_book(bd))
    elif action == '5':
        print(update_book(bd))
    elif action == '6':
        print('Программ завершена\n')
    else:
        print('Неверная команда\n')
