#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Scott Butters'
SITENAME = "Bits 'n' Bots"
SITEURL = ''
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

OUTPUT_PATH = '../output'
NOTEBOOK_DIR = 'notebooks'
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['img', 'pdf']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
    },
    'output_format': 'html5',
}

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

PLUGIN_PATHS = ['plugins/pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'post_stats', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook', 'tag_cloud']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# THEME = 'theme/pelican-themes/pelican-bootstrap3'
THEME = 'theme'
BOOTSTRAP_THEME = 'spacelab'

# Syntax Highlighting
PYGMENTS_STYLE = 'default'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article info
SHOW_DATE_MODIFIED = False

# Social widget
SOCIAL = (('Github', 'https://github.com/BotScutters'),
          ('LinkedIn', 'https://www.linkedin.com/in/scott-butters/'),)

# Blogroll
LINKS = (('Metis', 'https://www.thisismetis.com'),)

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['CNAME', '.git']

# Tag cloud
TAG_CLOUD_STEPS=1 #number of different sizes of fonts in the tag cloud
TAG_CLOUD_MAX_ITEMS=15 #number of different tags that can appear in tag cloud
TAG_CLOUD_SORTING='size' #how tags will be ordered in the tag cloud. Valid values: random, alphabetically, alphabetically-rev, size and size-rev
TAG_CLOUD_BADGE=True #If True, displays the number of articles in each tag

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
