# Configuration file for the Sphinx documentation builder.

project = 'disneyplusguide'
author = 'disneyplusguide'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

# Theme
html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

# Language
language = 'en'

# Browser Title
html_title = "disneyplusguide"

# Sitemap
html_baseurl = "https://login-ancestrycom-login.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"
