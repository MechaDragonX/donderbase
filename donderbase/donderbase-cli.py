#!/usr/bin/env python
# -*- coding: utf-8 -*-

from frontend.command import Command
from search import SearchClient
from wrangler import Wrangler


def init() -> SearchClient:
    print('Welcome to Donderbase! Please wait as all the data is loaded into the database!')

    search_client = SearchClient()
    search_client.add(Wrangler.donderful_wrangle(Wrangler.file_import('donderful')))

    print('Import successfull!')

    return search_client


# Main I suppose
# Welcome user and start import
search_client = init()

# User input loop
Command.input_loop(search_client)
