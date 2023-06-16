#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pysolr import Solr

class SearchClient:
    __port = 8983

    __always_commit = True

    __client = None

    __core = 'donderful'

    def __init__(self, port: int = 8983, core: str = 'donderful', always_commit: bool = True):
        self.__port = port
        self.__core = core
        self.__always_commit = always_commit

        self.__client = Solr(f'http://localhost:{self.__port}/solr/{self.__core}', always_commit=self.__always_commit)


    def add(self, items: list) -> None:
        for item in items:
            loaded = json.loads(item)
            self.__client.add(loaded)


    def search(self, query: str) -> list:
        return self.__client.search(query).docs
