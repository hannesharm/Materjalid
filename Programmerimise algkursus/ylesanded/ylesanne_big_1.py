"""
Check if given ID code is valid.
"""

def get_full_date(id_code: str) -> str:
    """
    Find a full date from given id code.
    Return date with format: dd.mm.yyyy (ex: 28.09.2021)
    """
    return '28.09.2021'

def get_birth_place(id_code: str) -> str:
    """
    Find the place where the person was born.
    Place identifiers:
    Kuressaare: 001-010
    Tartu: 011-020
    Tallinn: 021-220
    Kohtla-Järve: 221-270
    Tartu: 271-370
    Narva: 371-420
    Pärnu: 421-490
    Tallinn: 471-490
    Paide: 491-520
    Rakvere: 521-570
    Valga: 571-600
    Viljandi: 601-650
    Võru: 651-710
    Undefined: 711-999
    """
    return "Undefined"

def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).
    Id code should only contain numbers.
    The length of id_code should be 11.
    The day, month and year should be valid.
    Check if gender number is valid, currently only numbers from 1 to 6 are used.
    Check for valid control number, using method is_valid_control_number()
    
    returns a boolean, true if id code is valid, false if not valid.


    preferably create a function for every check, for example:
    a function, that checks, if the control number is correct
    a function, that checks, if the date is valid,
    a function, that checks the length and so on.
    """

    return False


def get_gender(id_code: str) -> str:
    """Return a gender based on the gender identifier."""
    return "undefined"


def get_data_from_id(id_code: str) -> str:
    """Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    """
    if not is_id_valid(id_code):
        return "Given invalid ID code!"
    else:
        gender = get_gender(id_code)
        birth_place = get_birth_place(id_code)
        full_date = get_full_date(id_code)
        message = f"This is a {gender} born on {full_date} in {birth_place}."
        return message


'''
When defending, explain, why one should use this if clause in main script.
'''
if __name__ == '__main__':
    id_codes = [
        "43108224720",
        "43608125236",
        "32605022755",
        "61106064780",
        "47208072760",
        "42605150146",
        "38205024782",
        "42404123759",
        "45905232713",
        "39412304990",
        "38909204962"
    ]

    for id_code in id_codes:
        print(get_data_from_id(id_code))
