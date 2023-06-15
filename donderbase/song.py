#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
from json import JSONEncoder
import json

class Genre(Enum):
    Pop = 0,
    Anime = 1
    Vocaloid = 2,
    Variety = 3,
    Classical = 4,
    GameMusic = 5,
    NamcoOriginal = 6

    # def __repr__(self):
    #     return f'{self.name}'


class Song:
    # Titles are in English if official Taiko translations exist. If not, romanized titles are used for consistency
    __title = ''

    # Example: TV Anime "JUJUTSU KAISEN" 1st Cour Opening Theme
    __subtitle = ''

    # Not often listed
    __artist = ''

    # Sometimes listed normally or as part of a subtitle, as in the example above
    # Example: Katamari Damacy
    __source = ''

    # Genre classification can change over time, so each entry in the list corresponds to the game in the same position of __game_list.
    # Old genre names are listed under their current genre names were applicable. For example: J-Pop to Pops
    # Before the additiona of a Vocaloid genre, some Vocaloid were in Variety. I'll decided what to do about that later
    __genre_list = []

    # Example: Listed in string form for now with games released in English using English titles
    # and Japanese only releases with romanized titles
    # Example:
    # __game_list: [
        # "Taiko no Tasujin: Drum 'n' Fun!"",
        # "Taiko no Tatsujin: Drum Session!"
        # "Taiko no Tatsujin: Rhythm Festival"
    # ]
    __game_list = []

    # Charts can change over time, so each entry in the list corresponds to the game in the same position of __game_list.
    # Each entry contains another array where each element corresponds to each difficulty in the order,
    # Easy, Normal, Hard, Oni/Extreme, Ura Oni/Extreme
    # A 0 denotes that the difficulty does not exist for that song
    # Example:
    # __difficulties = [
        # [ 3, 3, 4, 7, 0 ],
        # [ 3, 4, 5, 6, 8 ],
        # [ 3, 4, 5, 7, 8 ]
    # ]
    __difficulties = []


    def __init__(self, title: str, subtitle: str, artist: str, source: str, genre_list: list, game_list: list, difficulties: list):
        self.__title = title
        self.__subtitle = subtitle
        self.__artist = artist
        self.__source = source
        self.__genre_list = genre_list
        self.__game_list = game_list

        if difficulties != None:
            self.__difficulties = difficulties


    def to_dict(self):
        return {
            'title': self.__title,
            'subtitle': self.__subtitle,
            'artist': self.__artist,
            'source': self.__source,
            'genre_list': [g.value for g in self.__genre_list],
            'game_list': self.__game_list,
            'difficulties': self.__difficulties
        }
