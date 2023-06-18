#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
from song import Genre, Song

class Wrangler:
    def file_import(path: str) -> list:
        lines = []
        with open(path, 'r') as file:
            lines = file.readlines()
        lines.pop(0)
        lines.pop()

        return lines


    def serialize_list(songs: list) -> list:
        json_list = []
        for song in songs:
            json_list.append(json.dumps(song.to_dict()))

        return json_list


    def donderful_wrangle(raw_input: list) -> list:
        source_pattern = re.compile(r"(?<!\")[^\"]+(?!\")")

        songs = []
        title = ''
        subtitle = ''
        artist = ''
        source = ''
        genre_list = []
        game_list = [ 'Taiko no Tatusjin: Rhythm Festival' ]

        for line in raw_input:
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
            if not "From" in subtitle:
                artist = subtitle
            else:
                source = re.findall(source_pattern, subtitle)[1]

            songs.append(Song(title, subtitle, artist, source, genre_list, game_list, None))

            title = ''
            subtitle = ''
            artist = ''
            source = ''
            genre_list = []

        return Wrangler.serialize_list(songs)
