#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from search import SearchClient


class Command:
    __commands = {
        'help': '',
        'search': 'Usage: "search <field> <query>',
        'exit': 'Exit the program'
    }

    # Valid params to search
    # Example usage:
    # search source Persona 5
    __search_params = [
        'title',
        'subtitle',
        'artist',
        'source',
        'genre',
        'game'
    ]


    def input_loop(search_client: SearchClient) -> None:
        input_str = ''
        params = []
        query = None
        while(True):
            while(True):
                input_str = input('> ')
                params = input_str.split(' ')
                if Command.__is_command(params[0]):
                    break

            match params[0]:
                case 'help':
                    print('UNIMPLEMENTED')
                case 'search':
                    query = Command.__handle_search(input_str)
                    if query != None:
                        Command.__search(search_client, query)
                case 'exit':
                    Command.__exit()
            
            print()


    def __is_command(input: str) -> bool:
        for key in Command.__commands:
            if input == key:
                return True


    def __handle_search(input_str: str):
        params = input_str.split(' ')

        if (len(params) == 1 or params[0]) != 'search':
            return None
        if not (params[1] in Command.__search_params):
            return None
        
        return f'{params[1]}:{params[2]}'


    def __search(search_client: SearchClient, input: str) -> list:
        result = search_client.search(input)
        print(json.dumps(result, indent=4))


    def __exit() -> None:
        print('Thanks for using Donderbase!')
        sys.exit()
