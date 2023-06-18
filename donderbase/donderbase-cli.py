#!/usr/bin/env python
# -*- coding: utf-8 -*-

from frontend.command import Command
from search import SearchClient


search_client = SearchClient()

args = Command.add_args()
if args.upload:
    search_client = Command.upload(search_client, args.upload)
elif args.search:
    if Command.is_field(args.search[0]):
        Command.search(search_client, f'{args.search[0]}:{args.search[1]}')
