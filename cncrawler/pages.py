# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from elements import Calendar, Post, Header, TabPanel
from printers import CalendarCurrentMonthPrinter, CalendarLinkPrinter,\
                     PostContentPrinter, HeaderTitlePrinter, TabPanelPrinter, TabPrinter


class Page(object):
    elements = []

    def __init__(self, url):
        response = requests.get(url)

        self.url = url
        self.html = BeautifulSoup(response.text)

        elements_tmp = [klass(self.html, printers) for klass, printers in self.elements]
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


class LiturgiaIndexPage(SantosIndexPage):
    pass


class LiturgiaPage(Page):
    elements = [
        (TabPanel, [TabPanelPrinter, TabPrinter])
    ]

    @property
    def tabs(self):
        [tab.load_content(self.html) for tab in self.elements[0].tabs]
        return self.elements[0].tabs
