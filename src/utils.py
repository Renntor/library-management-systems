import json
from datetime import datetime


def add_book(bd):
    """
    Добавление книги в файл json
    """
    try:
        # проверка на то что год является числовом
        data = {
            'title': str(input('Введите название книги: \n')),
            'author': str(input('Введите автора: \n')),
            'year': int(input('Год издания: \n')),
            'status': 'в наличии'
        }
        current_year = datetime.now().year
        if not 0 <= data['year'] <= current_year:
            return f'Год может быть от 0 до {current_year}'

    except ValueError:
        return 'Поле year должно быть числовым\n', add_book(bd)

    with open(bd, 'r+', encoding='utf-8') as file:
        json_data = json.load(file)
        file.seek(0)
        file.truncate()
        json.dump(json_data, file, indent=2, ensure_ascii=False)
    return f'Книга успешно добавлена{json.dumps(json_data, indent=2, ensure_ascii=False)}\n'


def get_book(bd):
    """
    Список всех книг
    """
    with open(bd, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    return f'Список книг: {json.dumps(json_data, indent=2, ensure_ascii=False)}\n'


def retrieve_book(bd):
    """
    Вывод книг по ключевому полю
    """
    key = input('Введите способ поиска(title, author, year): \n')
    value = input('Введите значение: \n')

    if key not in ['title', 'author', 'year']:
        return 'Поиск может быть только по title, author, year\n', retrieve_book(bd)

    with open(bd, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        result = []
        for data in json_data:
            if str(data[key]) == value:
                result.append(data)

    return f'Список найденных книг: {json.dumps(result, indent=2, ensure_ascii=False)}\n'


def delete_book(bd):
    """
    Удаление книги по его id
    """
    try:
        id = int(input('Введите id книги: \n'))
    except ValueError:
        return 'ID должен быть числом\n', delete_book(bd)

    with open(bd, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    data = {item['id']: item for item in json_data}
    if id in data:
        del data[id]
    updated_data = list(data.values())
    with open(bd, 'w', encoding='utf-8') as file:
        json.dump(updated_data, file, indent=2, ensure_ascii=False)
    return 'Книга удалена\n'


def update_book(bd):
    """
    Обновление статуса книги
    """
    try:
        id = int(input('Введите id книги: \n'))
    except ValueError:
        return 'ID должен быть числом\n', delete_book(bd)

    status = str(input('Введите статус книги("в наличии", "выдана"): '))

    while status not in ['в наличии', 'выдана']:
        status = input('status должен быть в наличии или выдана')

    with open(bd, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    data = {item['id']: item for item in json_data}
    if id in data:
        data[id]['status'] = status
    else:
        return 'Книга не найдена'

    updated_data = list(data.values())

    with open(bd, 'w', encoding='utf-8') as file:
        json.dump(updated_data, file, indent=2, ensure_ascii=False)

    return f'Книга обновлена {json.dumps(data[id], indent=2, ensure_ascii=False)}'
