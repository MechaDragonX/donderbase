import json
import re
from song import Genre, Song

def main():
    donderful_wrangle()

def donderful_wrangle() -> list:
    filename = f'{__file__.removesuffix("donderbase/wrangler.py")}data/donderful.json'
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines.pop(0)
    lines.pop()

    songs = []
    title = ''
    subtitle = ''
    genre_list = []
    game_list = [ 'Taiko no Tatusjin: Rhythm Festival' ]

    for line in lines:
        current = json.loads(line.removesuffix(',\n'))
        genre = re.search("^[^_]*", list(current.keys())[0]).group()
        match genre:
            case 'pop':
                genre_list.append(Genre.Pop)
            case 'anime':
                genre_list.append(Genre.Anime)
            case 'vocaloid':
                genre_list.append(Genre.Vocaloid)
            case 'variety':
                genre_list.append(Genre.Variety)
            case 'classical':
                genre_list.append(Genre.Classical)
            case 'game':
                genre_list.append(Genre.GameMusic)
            case 'namco':
                genre_list.append(Genre.NamcoOriginal)
        title = current[f'{genre}_title']
        subtitle = current[f'{genre}_subtitle']
        songs.append(Song(title, subtitle, genre_list, game_list, None))

        title = ''
        subtitle = ''
        genre_list = []

    return songs

if __name__ == '__main__':
    main();
