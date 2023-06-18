#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import sys
from search import SearchClient
from wrangler import Wrangler

class Command:
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


    def add_args():
        parser = argparse.ArgumentParser(prog='Donderbase CLI' , 
                                         description='Upload data for and search a "Taiko no Tatsujin" song database.',
                                         usage='DonderbaseCLI [option] parameters...',
                                         add_help=False)
        
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
        parser.add_argument('-u','--upload', type=str, metavar=('<path>'), help='Upload a document to the Solr server')
        parser.add_argument('-s','--search', type=str, nargs=2, metavar=('<field>', '<value>'), help='Search for something in the Solr server')
        
        args = parser.parse_args()

        return args


    def upload(search_client: SearchClient, path: str) -> SearchClient:
        print('Please wait while all the data is loaded into the database!')
        search_client.add(Wrangler.donderful_wrangle(Wrangler.file_import(path)))
        print('Import successfull!')
        return search_client


    def is_field(field: str):
        if not (field in Command.__search_params):
            print('The field you specified does not exist!')
            return False
        
        return True


    def search(search_client: SearchClient, input: str) -> list:
        result = search_client.search(input)

        if len(result) == 0:
            print('No results found!')
        else:
            print(json.dumps(result, indent=4))
