#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pysolr import Solr

class Search:
    __port = 8983

    __always_commit = True

    client = None

    def __init__(self, port: int = 8983, always_commit: bool = True):
        self.__port = port
        self.__always_commit = always_commit

        self.client = Solr(f'http://localhost:{port}/solr/', always_commit=self.__always_commit)


    def add(self, items: list) -> None:
        self.client.add(items)


    def search(self, query: str) -> list:
        return self.client.search(query)
