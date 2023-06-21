import re
import csv

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Приводим ФИО к одному формату:
for contact in contacts_list:
    full_name = contact[0].split()
    if len(full_name) == 3:
        contact[0] = full_name[0]
        contact[1] = full_name[1]
        contact[2] = full_name[2]
    elif len(full_name) == 2:
        contact[0] = full_name[0]
        contact[1] = full_name[1]
        contact.insert(2, '')
    else:
        contact.insert(1, '')
        contact.insert(2, '')

# Приводим номера телефонов к единому формату:
for contact in contacts_list:
    contact[5] = re.sub(r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*доб\.\s*(\d+))?', r'+7(\2)\3-\4-\5 \6', contact[5])

# Объединяем дублирующиеся записи:
unique_contacts = {}
for contact in contacts_list:
    key = (contact[0], contact[1], contact[2])
    if key in unique_contacts:
        unique_contact = unique_contacts[key]
        for i in range(3, 7):
            if not unique_contact[i] and contact[i]:
                unique_contact[i] = contact[i]
    else:
        unique_contacts[key] = contact

# Преобразуем словарь в список:
unique_contacts_list = list(unique_contacts.values())

# Сохраняем получившиеся данные в новый файл:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(unique_contacts_list)