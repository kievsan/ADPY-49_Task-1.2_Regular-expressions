# This is a sample Python script.

from pprint import pprint
from Tools import *
import re

_FONEBOOK = 'phonebook_new.csv'

if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    contacts_list = get_fonebook()

    # TODO 1: выполните пункты 1-3 ДЗ
    # lastname,firstname,surname,organization,position,phone,email

    for person in contacts_list:
        for p in range(len(person)):
            person[p] = person[p].strip()

        # ДЗ пункт 1:
        for p in range(2):
            names_list = re.split(r'\s', person[p])
            for n in range(len(names_list)):
                person[p + n] = names_list[n]

        # ДЗ пункт 2:
        if person[5]:
            phone = re.sub(r"([+]7|^8)?\s*([(]|)(\d{3})([)]|)\s*([-]|)(\d{3})([-]|)(\d{2})([-]|)(\d{2}|)"  # основной
                           r"($|(\s*([(]|))(\w*[.?])\s*(\d*)([)]|$))",  # добавочный
                           r"+7(\3)\6-\8-\g<10> \g<14>\g<15>",
                           person[5]).strip()
            '''
            # или так:
            phone = person[5]
            main_number = re.search(r"([+]7|^8)?\s*([(]|)(\d{3})([)]|)\s*([-]|)(\d{3})([-]|)(\d{2})([-]|)(\d{2}|)", phone)
            extension_number = re.search(r'((?<=\. )|(?<=\.))\d+', phone)
            if main_number:
                phone = '+7(' + main_number.group(3) \
                       + ')' + main_number.group(6) \
                       + '-' + main_number.group(8) \
                       + '-' + main_number.group(10)
                if extension_number:
                    phone += ' доб.' + extension_number.group(0)
            '''
            person[5] = phone

    # ДЗ пункт 3:
    len_contacts_list = len(contacts_list)
    print('\nВСЕГО записей в списке:\t', len_contacts_list)
    cursor_contacts_list = 0
    while cursor_contacts_list < len_contacts_list:
        duplicate = duplicate_person(cursor_contacts_list, contacts_list)
        if duplicate["duplicate_index"]:
            contacts_list[cursor_contacts_list] = duplicate["correct_person"]
            del_person = contacts_list.pop(duplicate["duplicate_index"])
            print('Удалена запись как ДУБЛИКАТ:\t', del_person)
            len_contacts_list -= 1
            print('Осталось записей в списке:\t', len_contacts_list)
        cursor_contacts_list += 1

    print('\n\n\t\tОТРЕДАКТИРОВАННАЯ ТЕЛЕФОННАЯ КНИГА:')
    pprint(contacts_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open(_FONEBOOK, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
