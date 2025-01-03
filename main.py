import re
import csv


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


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
        phone_sample = re.compile('(\+7|8)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*')
        new_format_phone = phone_sample.sub(r'+7(\3)\6-\8-\10 \12\13', contact[5])
        new_contact.append(new_format_phone)
        new_contact.append(contact[6])
        new_contacts_list.append(new_contact)
    return new_contacts_list


def remove_duplicates(new_contacts_list):
    phone_book = dict()
    for contact in new_contacts_list:
        if contact[0] in phone_book:
            contact_value = phone_book[contact[0]]
            for i in range(len(contact_value)):
                if contact[i]:
                    contact_value[i] = contact[i]
        else:
            phone_book[contact[0]] = contact
    return list(phone_book.values())


# код для записи файла в формате CSV
def write_data(new_contacts_list):
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)



if __name__ == '__main__':
    created_list = created_contact_list(contacts_list)
    remove_duplicates(created_list)
    write_data(created_list)
