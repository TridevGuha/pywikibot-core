# -*- coding: utf-8 -*-
"""Family module for Wikimedia chapter wikis."""
from __future__ import unicode_literals

__version__ = '$Id$'

from pywikibot import family


class Family(family.Family):

    """Family for Wikimedia chapters hosted on wikimedia.org."""

    def __init__(self):
        """Constructor."""
        family.Family.__init__(self)
        self.name = 'wikimediachapter'

        self.countries = [
            'ar', 'br', 'bd', 'co', 'dk', 'fi', 'mk', 'mx', 'nl', 'no',
            'nyc', 'pl', 'rs', 'ru', 'se', 'ua', 'uk', 've',
        ]

        self.langs = dict([(country, '%s.wikimedia.org' % country)
                           for country in self.countries])
