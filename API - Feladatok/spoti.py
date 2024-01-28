import spotipy
from spotipy import SpotifyClientCredentials
import random
# Direkt használok angol változóneveket


def get_artist_albums(artist_name):
    sp = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())
    result = sp.search(q=artist_name, limit=1, type='artist')

    if not result['artists']['items']:
        print(f"Nincs találat az előadóra: {artist_name}")
        return None
        # https://stackoverflow.com/questions/9191388/it-is-more-efficient-to-use-if-return-return-or-if-else-return

    artist_id = result['artists']['items'][0]['id']
    albums = sp.artist_albums(artist_id=artist_id)['items']

    if not albums:
        print(f"Nincs találat az előadóhoz tartozó albumokra: {artist_name}")
        return None

    return [{'name': album['name'], 'release_date': album['release_date']} for album in albums]


def album_name_quiz(album):
    words = album['name'].split()
    longest_word = max(words, key=len)
    # https://ioflood.com/blog/python-max-function-guide-uses-and-examples/
    longest_word = str(longest_word)
    print("Az előadó egyik albumának címe:")
    for word in words:
        if word == longest_word:
            print('_' * len(word), end=' ')
        else:
            print(word, end=' ')
    print()
    guess = input('Találja ki az album címéből hiányzó szót: ')
    if guess.lower() == longest_word.lower():
        print('Helyes! Gratulálok!')
    else:
        print(f'Sajnálom, a helyes válasz: "{longest_word}".')


def main():
    print('Spotify Kvíz')
    artist_name = input('Adja meg kedvenc előadóját: ')
    albums = get_artist_albums(artist_name)
    if albums:
        random_album = random.choice(albums)
        # https://www.w3schools.com/python/ref_random_choice.asp
        album_name_quiz(random_album)


main()
