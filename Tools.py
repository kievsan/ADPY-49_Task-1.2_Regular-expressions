#

import csv

# import urllib.request
# _FONEBOOK = 'https://github.com/netology-code/py-homeworks-advanced/blob/master/5.Regexp/phonebook_raw.csv'
_FONEBOOK = 'phonebook_raw.csv'


def get_fonebook(refresh=False):
    if refresh:
        get_fonebook.contacts_list = {}
    if get_fonebook.contacts_list:
        return get_fonebook.contacts_list
    try:
        # with urllib.request.urlopen(_FONEBOOK) as f:
        with open(_FONEBOOK, 'r', encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=",")
            get_fonebook.contacts_list = list(rows)
    except FileNotFoundError as ex:
        print(f'File "{_FONEBOOK}" not found...\n\t{ex}\n')
    except OSError as other:
        print(f'При открытии файла "{_FONEBOOK}" возникли проблемы: \n\t{other}\n')
    return get_fonebook.contacts_list


get_fonebook.contacts_list = {}


def duplicate_person(reference_index, persons):
    number_persons = len(persons)
    duplicate_about = dict.fromkeys(["duplicate_index", "correct_person"])
    if reference_index == number_persons:
        return duplicate_about
    reference = persons[reference_index]

    # lastname,firstname,surname,organization,position,phone,email
    for person_index in range(reference_index + 1, number_persons):
        person = persons[person_index]
        if person[0] == reference[0]:
            if (reference[1] + reference[2] == '') \
                    or (person[1] + person[2] == '') \
                    or (reference[1] + reference[2] == person[1] + person[2]) \
                    or (reference[1] == person[1] and (reference[2] == '' or person[2] == '')):
                duplicate_about["duplicate_index"] = person_index
                duplicate_about["correct_person"] = make_correct_person(reference, person)
                break
    return duplicate_about


def make_correct_person(correct, person):
    for i in range(7):
        if person[i]:
            correct[i] = person[i]
    return correct
