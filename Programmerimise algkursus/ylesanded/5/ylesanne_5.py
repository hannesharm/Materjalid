"""
Printida välja info iga isikukoodi kohta.
Kui isikukood ei ole korras:
    Kui pikkus on paigast ära: tagasta "Pikkus ei ole õige!"
    Kui isikukoodis muid asju kui numbrid: tagasta "Isikukoodis võib olla ainult numbreid!"
    Kui kuupäeva ei eksisteeri näiteks on märgitud 35 päev või 14. kuu või 29 veebruar 2019: tagasta "Isikukoodi kuupäev ei ole korrektne!"
Kui isikukood on korras:
    Tagasta kuupäev stringina sellises formaadis: dd-mm-yyyy
                                               nt 03-05-1999

"""


def get_info(code: str) -> str:
    ##TODO code here!
    return "Isikukoodis võib olla ainult numbreid!"


if __name__ == '__main__':
    id_codes = [
        "43108224720",
        "4360812523",
        "32605022755",
        "61106064780",
        "4720807276a",
        "42605150146",
        "382050247",
        "42404123759",
        "45905232713442d",
        "39412304990",
        "389092049622"
    ]

    for id_code in id_codes:
        print(get_info(id_code))