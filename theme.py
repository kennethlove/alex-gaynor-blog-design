#!/usr/bin/env python

name = 'fetch'
version = '1.0'
website = 'https://github.com/kennethlove/alex-gaynor-blog-design'
author = {
    'name': 'Kenneth Love',
    'website': 'http://gigantuan.net'
}

lang = 'en'

analytics = None

# buttons uses a custom icon font with only 5 special characters.
# h - home icon
# t - twitter icon
# g - github icon
# r - rdio icon
# l - link icon
buttons = [
    {
        'title': 'Home',
        'link': '/',
        'icon': 'h'
    },
    {
        'title': 'GitHub',
        'link': 'https://github.com/alex',
        'icon': 'g'
    },
]

navigation = [
    {
        'name': 'Home',
        'link': '/'
    }
]

# Change this to control what shows up in the "no comments" block on post
# templates.
no_comments = "Comments are never going to happen. Stop trying to make comments happen."
