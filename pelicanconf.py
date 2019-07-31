#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



AUTHOR = 'Caverneiros'
SITENAME = 'Caverna de Dados (Este blog ainda está em contrução)'
SITEURL = 'https://cavernadedados.com'
# SITEURL = ''
SITE_LOGO = '/assets/img/logo.png'

PATH = 'content/'

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
SOCIAL = (
          # ('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/caverna-de-dados'),
          ('facebook','https://www.facebook.com/myprofile/'),
          # ('flickr','https://www.flickr.com/myprofile/'),
          # ('envelope','mailto:my@mail.address')
          )


DEFAULT_PAGINATION = 10

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']


EXTRA_PATH_METADATA = {
#     'assets/robots.txt': {'path': 'robots.txt'},
    'assets/img/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}


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
  'plugins'
]

# PLUGINS = [
#   'sitemap',
#   'neighbors',
#   'assets'
# ]

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
GOOGLE_ANALYTICS = "UA-136764041-1"

THEME = 'attila'

### Theme specific settings


HEADER_COVER = 'assets/img/BG.jpg'


AUTHORS_BIO = {
  # "zutrinken": {
  #   "name": "Zutrinken",
  #   "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
  #   # "image": "assets/images/avatar.png",
  #   "website": "http://blog.arulraj.net",
  #   "linkedin": "unavailable",
  #   "github": "arulrajnet",
  #   "location": "Chennai",
  #   "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  # }, 
  "hugo": {
    "name": "Hugo Trigueiro",
    "cover": "assets/img/bg-hugo.jpg",
    "image": "assets/img/hugo.jpg",
    # "website": "http://blog.arulraj.net",
    "linkedin": "hugo-trigueiro",
    "github": "hugotrigueiro",
    "location": "São Paulo/SP",
    "bio": "É graduando em Economia na Universidade Federal do ABC e trabalha como Analista de Captação de Recursos em uma instituição do terceiro setor."
  }, 
  "diego": {
    "name": "Diego Zurita",
    "cover": "assets/img/bg-zurita.jpg",
    "image": "assets/img/diego.jpg",
    # "website": "http://blog.arulraj.net",
    "linkedin": "diego-zurita-067775110",
    "github": "DiegoZurita",
    "location": "São Paulo/SP",
    "bio": "Gosto de F1, dados, matemática, programação e aprendo frameworks por diversão"
  },
  "leonam": {
    "name": "Leonam Mendonça",
    "cover": "assets/img/bg-leonam.jpg",
    "image": "assets/img/leonam.jpg",
    #"website": "http://blog.arulraj.net",
    "linkedin": "leonammendonca",
    "github": "leonammp",
    "location": "Campos do Jordão/SP",
    "bio": "É graduando em Análise e Desenvolvimento de Sistemas no Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP), freelancer de desenvolvimento web e encantado por segurança da informação e perícia computacional."
  }
}

# Custom Header

#HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}
# HEADER_COVERS_BY_TAG = {'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}
SITESUBTITLE = 'Um Blog sobre Data Science, Estatística, Economia e Programação.'
HEADER_COVER_OG = 'assets/img/LOGO_OG.jpg'

COLOR_SCHEME_CSS = 'monokai.css'

CSS_OVERRIDE = ['assets/css/custom.css']
JS_OVERRIDE = ['assets/js/custom.js']
