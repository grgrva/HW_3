import datetime
import math


email1 = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

email2 = {
    "subject": " Weekend plans ",
    "from": "  katya_yan@yandex.ru ",
    "to": "  friend@mail.ru ",
    "body": "\tHey!\nLet's go hiking this weekend.\nBring snacks!\n",
}

email3 = {
    "subject": "Reminder: Meeting",
    "from": "  ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": "   ",
}

email4 = {
    "subject": "   ",
    "from": "   alex@business.net ",
    "to": "   hr@company.ru ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!",
}

email5 = {
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam",
}


# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}


# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_email = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_email

print(f'2. дата отправки: {email["date"]}')


# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email["from"] = email["from"].lower().strip()
email["to"] = email["to"].lower().strip()

print(f"3. нормализация email:\n" f' from - {email["from"]}\n' f' to - {email["to"]}')


# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login, domain = email["from"].split("@")

print(f"4. логин: {login}, \n" f"домен: {domain}")


# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

email["short_body"] = email["body"][:10] + "..."

print(f'5. Сокращенное body: {email["short_body"]}')


# 6. Списки доменов: создайте список личных доменов
# и список корпоративных доменов. с учетом того что там должны быть только уникальные значение

personal_domens = list(
    set(
        [
            "gmail.com",
            "list.ru",
            "yahoo.com",
            "outlook.com",
            "hotmail.com",
            "icloud.com",
            "yandex.ru",
            "mail.ru",
            "list.ru",
            "bk.ru",
            "inbox.ru",
        ]
    )
)

corporat_domens = list(
    set(
        [
            "company.ru",
            "corporation.com",
            "university.edu",
            "organization.org",
            "company.ru",
            "business.net",
        ]
    )
)

print(
    f"6. корпоративные домены: \n {corporat_domens} \n"
    f"личные домены: \n {personal_domens}"
)


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.

common_domens = set(personal_domens) & set(corporat_domens)
if not common_domens:
    print(f"7. нет пересечений в доменах")
else:
    print(f"7. пересечения есть: {common_domens}")


# 8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.

is_corporate = domain in corporat_domens


print(f'8. "корпоративность" отправителя: {is_corporate}')


# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].

email["clean_body"] = email["body"].replace("\t", " ")
email["clean_body"] = email["clean_body"].replace("\n", " ")

print(f'9. Чистый body: \n {email["clean_body"]}')


# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

email["sent_text"] = (
    f'Кому: {email["to"]}, \n '
    f'От {email["from"]}, \n '
    f'Тема: {email["subject"]}, \n '
    f'Дата: {email["date"]}, \n '
    f'Текст сообщения: {email["clean_body"]}'
)

print(f'10. Отпрвленное письмо: \n {email["sent_text"]}')


# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = math.ceil(len(email["clean_body"]) / 500)

print(f"11. Количество страниц для печати == {pages}")


# 12. создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.

is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

print(
    f"12. Пустой заголовок письма == {is_subject_empty} \n"
    f"Пустое тело письма == {is_body_empty} "
)


# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

email["masked_from"] = login[:2] + "***@" + domain

print(f'13. Маска email отправителя: {email["masked_from"] }')


# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".

personal_domens.remove("list.ru")
personal_domens.remove("bk.ru")

print(f'14. без "list.ru" и "bk.ru": \n {personal_domens}')
