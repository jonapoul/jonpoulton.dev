from __future__ import unicode_literals
from datetime import datetime

# Basic config
AUTHOR = "Jon Poulton"
FAVICON = "/images/favicon.ico"
PATH = "content"
RELATIVE_URLS = True
SITELOGO = "/images/avatar.jpg"
SITENAME = "Jon Poulton"
SITESUBTITLE = "Android Software Engineer"
SITETITLE = "Jon Poulton"
SITEURL = "https://jonpoulton.dev"
USE_LESS = True

# Theme
THEME = "./Flex/"
THEME_COLOR = "dark"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = False
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

# Time
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_DATE_FORMAT = "%d %b %Y"
DEFAULT_LANG = "en"
I18N_TEMPLATES_LANG = "en"
LOCALE = "en_US"
OG_LOCALE = "en_US"
TIMEZONE = "Europe/London"

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
USE_GOOGLE_FONTS = False

# Plugins
PLUGIN_PATHS = [
    "pelican-plugins",
    "plugins",
]
PLUGINS = [
    "always_modified",
    "i18n_subsites",
    "post_stats",
]

# Plugin Conf
ALWAYS_MODIFIED = True
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 175

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Menu
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Tags", "/tags.html"),
)

# Social widgets
SOCIAL = (
    ("envelope", "mailto:jpoulton (AT) pm.me"),
    ("github", "https://github.com/jonapoul"),
    ("linkedin", "https://www.linkedin.com/in/jon-poulton-6a59111a4/"),
)

# License
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
    "local_icons": True,
}

# Don't generate category pages
CATEGORIES_SAVE_AS = None
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False
