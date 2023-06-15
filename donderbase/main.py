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


def handle_search(input_str: str):
    params = input_str.split(' ')
    if len(params) == 1 or params[0] != 'search':
        return None
    
    return input_str[7:]


def search(search: Search, input: str) -> list:
    # return search.search(input)
    print(f'検索 {input}')


def exit() -> None:
    print('Thanks for using Donderbase!')
    sys.exit()


print('Welcome to Donderbase! Please wait as all the data is loaded into the database!')

# search = Search()
# search.add(Wrangler.donderful_wrangle(Wrangler.file_import('donderful')))
Wrangler.donderful_wrangle(Wrangler.file_import('donderful'))

print('Import successfull!')


input_str = ''
params = []
query = None
while(True):
    while(True):
        input_str = input('> ')
        params = input_str.split(' ')
        if is_command(params[0]):
            break

    match params[0]:
        case 'help':
            print('UNIMPLEMENTED')
        case 'search':
            query = handle_search(input_str)
            if query != None:
                search(search, query)
        case 'exit':
            exit()
    
    print()
