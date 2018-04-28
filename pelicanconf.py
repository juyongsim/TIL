#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import glob

AUTHOR = 'Yunseop Song'
SITENAME = '전지적 송윤섭시점 TIL'
SITEURL = 'https://til.songyunseop.com'
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'
RELATIVE_URLS = True

PAGE_PATHS = [os.getcwd()+"/README.md"]
ARTICLE_PATHS = glob.glob(os.getcwd()+"/*/*.md")
STATIC_PATHS = ['static']

DEFAULT_PAGINATION = 4
DEFAULT_CATEGORY='uncategorized'
USE_FOLDER_AS_CATEGORY=True
DISPLAY_PAGES_ON_MENU=True
DISPLAY_CATEGORIES_ON_MENU=True
FILENAME_METADATA = '(?P<title>.*)'

OUTPUT_PATH = 'public/'

DISQUS_SITENAME = 'songyunseop'
GITHUB_URL = 'https://github.com/songyunseop/til'

LINKS = (
    ('전지적 송윤섭시점 블로그', 'https://songyunseop.com/'),
    ('전지적 송윤섭시점 기술블로그', 'https://tech.songyunseop.com/'),
)

SOCIAL = (
    ('Github', 'https://github.com/songyunseop'),
    ('Facebook', 'https://facebook.com/yunseop.song.9'),
    ('LinkedIn', 'https://www.linkedin.com/in/yunseop-song-698226110'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

PLUGIN_PATHS = ["custom-plugins", "pelican-plugins"]
PLUGINS = ["auto-title", "filetime_from_git", "sitemap"]

SITEMAP = {
    'format': 'xml'
}
