import requests
import random


def valasz_kerese(vicc_tartalma):
    payload = {
        'term': vicc_tartalma
    }
    url = 'https://icanhazdadjoke.com/search'
    headers = {"Accept": "application/json"}
    return requests.get(url, params=payload, headers=headers)


def valasz_kiiratasa(valasz):
    if 'results' in valasz and valasz['results']:
        random_valasz = valasz["results"][random.randint(0, len(valasz["results"]) - 1)]
        print(random_valasz["joke"])
    else:
        print('Nincs találat a keresésre, ezért itt egy random vicc:')
        vicc_tartalma = None
        valasz = valasz_kerese(vicc_tartalma).json()
        valasz_kiiratasa(valasz)


def valasz_parameterei():
    vicc_tartalma = input('Adjon meg egy angol szót a vicc kereséséhez! > ')
    valasz = valasz_kerese(vicc_tartalma).json()
    valasz_kiiratasa(valasz)


def main():
    valasz_parameterei()


main()
