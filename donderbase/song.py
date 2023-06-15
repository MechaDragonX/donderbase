#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum

class Genre(Enum):
    Pop = 0,
    Anime = 1
    Vocaloid = 2,
    Variety = 3,
    Classical = 4,
    GameMusic = 5,
    NamcoOriginal = 6

    # resultDesc = Should the result be an enum?
    # If true, return an enum
    # else, return the oppoiste type (int if given sting, and vice versa)
    @classmethod
    def convert(input, resultEnum: bool = False):
        if isinstance(input, int):
            if bool:
                match input:
                    case 0:
                        return Genre.Pop
                    case 1:
                        return Genre.Anime
                    case 2:
                        return Genre.Vocaloid
                    case 3:
                        return Genre.Variety
                    case 4:
                        return Genre.Classical
                    case 5:
                        return Genre.GameMusic
                    case 6:
                        return Genre.NamcoOriginal

            else:
                match input:
                    case 0:
                        return 'Pop'
                    case 1:
                        return 'Anime'
                    case 2:
                        return 'Vocaloid'
                    case 3:
                        return 'Variety'
                    case 4:
                        return 'Classical'
                    case 5:
                        return 'GameMusic'
                    case 6:
                        return 'NamcoOriginal'
        elif isinstance(input, str):
            if bool:
                match input:
                    case 'Pop':
                        return Genre.Pop
                    case 'Anime':
                        return Genre.Anime
                    case 'Vocaloid':
                        return Genre.Vocaloid
                    case 'Variety':
                        return Genre.Variety
                    case 'Classical':
                        return Genre.Classical
                    case 'GameMusic':
                        return Genre.GameMusic
                    case 'NamcoOriginal':
                        return Genre.NamcoOriginal
            else:
                match input:
                    case 'Pop':
                        return 0
                    case 'Anime':
                        return 1
                    case 'Vocaloid':
                        return 2
                    case 'Variety':
                        return 3
                    case 'Classical':
                        return 4
                    case 'GameMusic':
                        return 5
                    case 'NamcoOriginal':
                        return 6


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
            'genre_list': [item.name for item in self.__genre_list],
            'game_list': self.__game_list,
            'difficulties': self.__difficulties
        }
