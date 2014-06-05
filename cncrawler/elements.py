# -*- coding: utf-8 -*-


class Element(object):
    """
    Esta classe representa um elemento genérico da página.
    """
    def __init__(self, root, printers):
        self.root = root
        self.printers = printers

    def find(self, element):
        return self.root.find(element)

    def select(self, selector, all=False):
        selected_items = self.root.select(selector)

        if not all and selected_items:
            return selected_items.pop(0)
        else:
            return selected_items


class Calendar(Element):
    @property
    def current_month(self):
        month_tag = self.select('div#nav-calendar span.mes-atual')
        return self.printers[0](month_tag)

    @property
    def links(self):
        a_tags = self.select('table#wp-calendar tbody td a', True)
        return [self.printers[1](a_tag) for a_tag in a_tags]


class Header(Element):
    @property
    def title(self):
        title_tag = self.select('hgroup.content-header h1.entry-title')
        return self.printers[0](title_tag)


class Post(Element):
    @property
    def content(self):
        content_tag = self.select('#content-post div.entry-content')
        content_tag = self.clean_up(content_tag)
        return self.printers[0](content_tag)

    def clean_up(self, content_tag):
        scripts = content_tag.find_all('script')
        social_top = content_tag.find_all('div', {'class': 'socialmedia-top'})
        social_bottom = content_tag.find_all('div', {'class': 'socialmedia-bottom'})

        for tags in [scripts, social_top, social_bottom]:
            for tag in tags:
                tag.decompose()

        return content_tag
