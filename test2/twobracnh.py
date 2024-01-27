import json

def zapisz_fakture():
    kwota = float(input("Podaj kwotę faktury: "))
    data_faktury = input("Podaj datę faktury (w formacie YYYY-MM-DD): ")
    waluta = input("Podaj walutę: ")

    faktura = {
        "Kwota": kwota,
        "Data_faktury": data_faktury,
        "Waluta": waluta
    }

    with open("faktury.txt", "a") as plik:
        json.dump(faktura, plik)
        plik.write('\n')

# Wywołanie funkcji
zapisz_fakture()

# HELLO MSFCK
