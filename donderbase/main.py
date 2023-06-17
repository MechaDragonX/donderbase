#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from search import SearchClient
from wrangler import Wrangler


commands = {
    'help': '',
    'search': 'Usage: "search <query>',
    'exit': 'Exit the program'
}


def init() -> SearchClient:
    print('Welcome to Donderbase! Please wait as all the data is loaded into the database!')

    search_client = SearchClient()
    search_client.add(Wrangler.donderful_wrangle(Wrangler.file_import('donderful')))

    print('Import successfull!')


def input_loop(search_client: SearchClient) -> None:
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
                    search(search_client, query)
            case 'exit':
                exit()
        
        print()


def is_command(input: str) -> bool:
    for key in commands:
        if input == key:
            return True


def handle_search(input_str: str):
    params = input_str.split(' ')
    if len(params) == 1 or params[0] != 'search':
        return None
    
    return input_str[7:]


def search(search_client: SearchClient, input: str) -> list:
    result = search_client.search(input)
    print(json.dumps(result, indent=4))


def exit() -> None:
    print('Thanks for using Donderbase!')
    sys.exit()


# Main I suppose
# Welcome user and start import
search_client = init()

# User input loop
input_loop(search_client)
