#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Caverneiros'
SITENAME = 'Caverna de Dados'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets', 'static']


# EXTRA_PATH_METADATA = {
#     'assets/robots.txt': {'path': 'robots.txt'},
#     'assets/favicon.ico': {'path': 'favicon.ico'},
#     'assets/CNAME': {'path': 'CNAME'}
# }



# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

PLUGIN_PATHS = [
  '/home/diego/Desktop/repos/blog/plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Analytics
#GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'attila'

### Theme specific settings

# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
HEADER_COVER = 'https://raw.githubusercontent.com/hugotrigueiro/Entropy-Function/master/BG.jpg'


COLOR_SCHEME_CSS = 'github.css'

#CSS_OVERRIDE = ['assets/css/myblog.css']

CUSTOM_CSS = 'static/custom.css'

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    #"image": "assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "linkedin": "unavailable",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

# Custom Header

#HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}
HEADER_COVERS_BY_TAG = {'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}


