import requests
from pprint import pprint as pp


def valasz_kerese(orszag, nev):
    payload = {
        'country': orszag,
        'name': nev
    }
    url = 'http://universities.hipolabs.com/search'
    return requests.get(url, params=payload)


def valasz_parameterei():
    orszag = None
    nev = None
    while orszag != ' ' and nev != ' ':
        print('Ha ki szeretne lépni, üssön egy SPACE-t.')
        print('Ha nem szeretne az adott kérdésre válaszolni, üssön ENTER-t.')
        print('------------------------------------------------------------')
        orszag = input('Adja meg az ország hivatalos nevét angolul! > ')
        nev = input('Adja meg az egyetem nevét! > ')
        valasz = valasz_kerese(orszag, nev)
        pp(valasz.json())


def main():
    valasz_parameterei()


main()
