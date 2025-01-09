import re
import csv


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# Функция преобразования исходных данных в требуемый формат
def created_contact_list(contacts_list):
    new_contacts_list = list()
    for contact in contacts_list:
        new_contact = list()
        join_name = ",".join(contact[:3])
        result = re.findall(r'(\w+)', join_name)
        while len(result) < 3:
            result.append('')
        new_contact += result
        new_contact.append(contact[3])
        new_contact.append(contact[4])
        phone_pattern = r"(\+7|8)?\s?[\(]?(\d{3})[\)]?[-\s]?(\d{3})[-\s]?(\d{2})[-]?(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
        phone_sub = r"+7(\2)\3-\4-\5 \6\7"
        new_format_phone = re.sub(phone_pattern, phone_sub, contact[5])
        new_contact.append(new_format_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    # print(new_contacts_list)
    return new_contacts_list


# Функция по объединению данных с одинаковыми Фамилией и именем и удаление дубликатов
def remove_duplicates(new_contacts_list):
    for contact in new_contacts_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in new_contacts_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                for i in range(2, 7):
                    if contact[i] == '': 
                        contact[i] = new_contact[i]
    result_list = []
    for j in new_contacts_list:
        if j not in result_list:
            result_list.append(j)

    return result_list


# код для записи файла в формате CSV
def write_data(new_list):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)



if __name__ == '__main__':
    created_list = created_contact_list(contacts_list)
    duplicates = remove_duplicates(created_list)
    write_data(duplicates)
