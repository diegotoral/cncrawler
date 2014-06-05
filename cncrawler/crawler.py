#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from pages import SantosIndexPage, SantoPage


SANTOS_URL = 'http://santo.cancaonova.com/'
LITURGIAS_URL = 'http://liturgia.cancaonova.com/'


def usage(basename):
    print """Usage: {0} (liturgias|santos)""".format(basename)


def start_santos():
    index_page = SantosIndexPage(SANTOS_URL)

    with open('santos', 'w') as f:
        for link in index_page.calendar.links:
            url = str(link)
            page = SantoPage(url)

            f.write('Dia: ' + link.tag.text + '\n')
            f.write(str(page.header.title))
            f.write(str(page.post.content))
            f.write('\n\n')


def start_liturgias():
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage(sys.argv[0])
        sys.exit(1)

    if sys.argv[1] == 'liturgias':
        print 'liturgias'
    elif sys.argv[1] == 'santos':
        start_santos()
    else:
        print u'Opção inválida! Opções possíveis são liturgias ou santos.'
        usage(sys.argv[0])
        sys.exit(1)
