#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from search import Search
from wrangler import Wrangler


commands = {
    'help': '',
    'search': 'Usage: "search <query>',
    'exit': 'Exit the program'
}


def is_command(input: str) -> bool:
    for key in commands:
        if input == key:
            return True


def search(search: Search) -> list:
    # return search.search(input('> '))
    print('検索')


def exit() -> None:
    print('Thanks for using Donderbase!')
    sys.exit()


print('Welcome to Donderbase! Please wait as all the data is loaded into the database!')

# search = Search()
Wrangler.donderful_wrangle(Wrangler.file_import('donderful'))
# search.add()

print('Import successfull!')


input_str = ''
while(True):
    while(True):
        input_str = input('> ')
        if is_command(input_str):
            break

    match input_str:
        case 'help':
            print('UNIMPLEMENTED')
        case 'search':
            search(search)
        case 'exit':
            exit()
    
    print()
