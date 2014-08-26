# -*- coding: utf-8 -*-


class GenericTagPrinter(object):
    def __init__(self, tag):
        self.tag = tag

    def to_str(self):
        return self.tag.text

    def __str__(self):
        return (self.to_str() + '\n').encode('utf-8')


class HeaderTitlePrinter(GenericTagPrinter):
    def to_str(self):
        return self.tag.span.text


class CalendarCurrentMonthPrinter(GenericTagPrinter):
    def to_str(self):
        return self.tag.text


class CalendarLinkPrinter(GenericTagPrinter):
    def to_str(self):
        return self.tag['href']


class PostContentPrinter(GenericTagPrinter):
    pass


class TabPanelPrinter(GenericTagPrinter):
    pass


class TabPrinter(GenericTagPrinter):
    def to_str(self):
        return self.tag.text
