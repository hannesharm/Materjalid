"""
Et kasutada teste:
1. (Eeldan et kasutad pycharmi)
2. Installi pycharmile python package "pytest"
3. Kontrolli, et see testi skript on samas koustas, kui sinu kodutöö skript
4. vaheta ära importi real importitud mooduli nimi (Kus? eraldi kommentaarina näidatud)
5. vajuta play nuppu testide ees

!! Kui kodutöö teste ei läbi, siis kaitsma ei saa tulla
Kui leiate vea, et mõni test kukub läbi, aga ei tohiks, siis andke teada!
"""

import string
import random
import datetime
import ylesanne_5 as task  # Vaata, mis su skripti nimi on ning pane see siia asemele.
                           # Kui su skripti failinimi on näiteks kodune-ylesanne.py, siis peab olema seal import kodune-ylesanne as task


only_numbers = "Isikukoodis võib olla ainult numbreid!"
length_invalid = "Pikkus ei ole õige!"
invalid_date = "Isikukoodi kuupäev ei ole korrektne!"


def test_only_numbers():
    assert task.get_info("a") in (only_numbers, length_invalid)
    assert task.get_info("aaaaaaaaaaa") == only_numbers
    assert task.get_info("-1234567890") == only_numbers
    assert task.get_info("1234.567890") == only_numbers
    for i in range(1000):
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(11))
        assert task.get_info(code) == only_numbers


def test_length():
    assert task.get_info("") == length_invalid

    for i in range(11):
        assert task.get_info("1" * i) == length_invalid

    assert task.get_info("123456789012") == length_invalid
    assert task.get_info("1234567890123") == length_invalid


def test_date():
    assert task.get_info("39909400000") == invalid_date
    assert task.get_info("39909300000") != invalid_date
    assert task.get_info("50002290000") != invalid_date

    for i in range(1000):
        date = get_random_date()
        day = str(date.day) if len(str(date.day)) == 2 else "0" + str(date.day)
        month = str(date.month) if len(str(date.month)) == 2 else "0" + str(date.month)
        year = str(date.year)[2:]
        year_id = get_year_id(date)

        assert task.get_info(year_id + year + month + day + "0000") == "{0}-{1}-{2}".format(day, month, date.year)


def test_correct():
    id_codes = [
        ("43108224720", "22-08-1931"),
        ("43608125236", "12-08-1936"),
        ("32605022755", "02-05-1926"),
        ("61106064780", "06-06-2011"),
        ("47208072760", "07-08-1972"),
        ("42605150146", "15-05-1926"),
        ("38205024782", "02-05-1982"),
        ("42404123759", "12-04-1924"),
        ("45905232713", "23-05-1959"),
        ("39412304990", "30-12-1994"),
        ("38909204962", "20-09-1989")
    ]

    for id_code in id_codes:
        assert task.get_info(id_code[0]) == id_code[1]


def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def get_random_date() -> datetime:
    d1 = datetime.datetime.strptime('1/1/1901 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
    return random_date(d1, d2)


def get_year_id(date: datetime) -> str:
    if str(date.year)[:2] == "19":
        return random.choice(("3", "4"))
    return random.choice(("5", "6"))
