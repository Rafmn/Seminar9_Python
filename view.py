

# показать меню


def show_menu():
    return '/show_all - Показать все\nФормат добавления записи: "/add Фамилия Имя Отчество Телефон"\nФормат удаления записи: "/delete нужный индекс"\n/import_txt - Импортировать базу в txt-файл'
    # return int(input('Введите цифру: '))


# def delete():
#     print('Введите индекс для удаления')
#     return int(input())


# def change_tel():
#     print('Введите индекс для изменения')
#     print('Введите новый телефон')
#     return int(input()), input()


# def show_res(res):
#     for i, row in enumerate(res):
#         print(i, ' '.join(row))


# def add_info():
#     print('Введите ФИО и тел через пробел')
#     in_info = input().split()
#     return in_info

# def add_info_again():      # Добавление повторного запроса на ввод информации
#     print('Добавить новую информацию?')
#     print('Введите 1 - чтобы закончить, или 2 - для добавления новой информации')
#     new_info = int(input())
#     return new_info

# def show_export_txt():
#     print('Выполнен экспорт файла в txt формат')