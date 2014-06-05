# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from elements import Calendar, Post, Header
from printers import CalendarCurrentMonthPrinter, CalendarLinkPrinter,\
                     PostContentPrinter, HeaderTitlePrinter


class Page(object):
    elements = []

    def __init__(self, url):
        response = requests.get(url)

        self.url = url
        self.html = BeautifulSoup(response.text)

        elements_tmp = []
        for elementClass, printers in self.elements:
            elements_tmp.append(elementClass(self.html, printers))

        self.elements = elements_tmp


class SantosIndexPage(Page):
    elements = [
        (Calendar, [CalendarCurrentMonthPrinter, CalendarLinkPrinter])
    ]

    @property
    def calendar(self):
        return self.elements[0]


class SantoPage(Page):
    elements = [
        (Post, [PostContentPrinter]),
        (Header, [HeaderTitlePrinter])
    ]

    @property
    def post(self):
        return self.elements[0]

    @property
    def header(self):
        return self.elements[1]
