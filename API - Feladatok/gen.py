from lyricsgenius import Genius
import random
import os

# Genius API beállítások
genius = Genius(os.environ.get('GENIUS_API_TOKEN'))


def get_artist_id(artist_name):
    artist = genius.search(artist_name, type_='artist')
    if not artist['sections'][0]['hits']:
        print('Nem találtam meg a kívánt előadót.')
        return None
    return artist['sections'][0]['hits'][0]['result']['id']


def get_albums(artist_id):
    albums = genius.artist_albums(artist_id)
    selected_albums_id = []
    selected_albums_list = []
    i = 0
    while i < (len(albums['albums']) - 1):
        selected_albums_list.append(albums['albums'][i]['name'])
        selected_albums_id.append(albums['albums'][i]['id'])
        i += 1
    return selected_albums_list, selected_albums_id


def get_selected_album(albums, ids):
    print('Választható albumok:')
    for i, album in enumerate(albums, start=1):
        print(f'{i}. {album}')
    selected_index = int(input('Válasszon egy sorszámot (pont nélkül) az album kiválasztásához: ')) - 1
    if 0 <= selected_index < len(albums):
        print(f'A választott album a(z) {albums[selected_index]}')
        return ids[selected_index]
    else:
        print('Érvénytelen választás.')
        return None


def clean_lyrics(lyrics):
    lines = lyrics.split('\n')[1:]
    cleaned_lines = [line for line in lines if not line.startswith('[')]
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    return '\n'.join(cleaned_lines)


def get_random_track_lyrics(selected_albums_id):
    tracks = genius.album_tracks(int(selected_albums_id))
    i = 0
    selected_tracks_id = []
    while i < (len(tracks['tracks'])):
        if not tracks['tracks'][i]['song']['instrumental']:
            selected_tracks_id.append(tracks['tracks'][i]['song']['id'])
        i += 1
    n = []
    if selected_tracks_id == n:
        return '', ''
    random_track = random.choice(selected_tracks_id)
    song_lyrics = genius.search_song(song_id=random_track)
    if song_lyrics:
        if song_lyrics and hasattr(song_lyrics, 'lyrics') and hasattr(song_lyrics, 'title'):
            # https://www.w3schools.com/python/ref_func_hasattr.asp
            return song_lyrics.lyrics, song_lyrics.title
        else:
            print(f'Nincs dalszöveg a(z) {random_track} számhoz a Genius API-ban.')
            return '', ''
    else:
        print(f'Nem található a(z) {random_track} szám a Genius API-ban.')
        return '', ''


def clean_track_title(title):
    return title.strip()


def main():
    artist_name = input('Előadó neve: ')
    artist_id = get_artist_id(artist_name)
    if not artist_id:
        return

    albums, ids = get_albums(artist_id)
    selected_album_id = get_selected_album(albums, ids)
    if selected_album_id is None:
        return
    lyrics, correct_title = get_random_track_lyrics(selected_album_id)

    if not lyrics:
        print(f'Nem sikerült megtalálni a dalszöveget, vagy a számot a Genius API segítségével.')
        return

    cleaned_lyrics = clean_lyrics(lyrics)

    print('\nSzám szövege:')
    print(cleaned_lyrics)

    guessed_title = input('\nMi a szám címe? ')
    cleaned_guessed_title = clean_track_title(guessed_title)

    if cleaned_guessed_title.lower() == clean_track_title(correct_title).lower():
        print('Gratulálok! Helyes válasz.')
    else:
        print(f'Sajnálom, rossz válasz. A helyes cím: {correct_title}')


main()
