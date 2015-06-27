"""
network-related utils for npmanager
"""
import timeit
try:
    from httplib import HTTPConnection, HTTPSConnection
except ImportError:
    from http.client import HTTPConnection, HTTPSConnection
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


def ping(url):
    urlparts = urlparse(url)
    total = 0
    try:
        if urlparts[0] == 'https':
            h = HTTPSConnection(urlparts[1])
        else:
            h = HTTPConnection(urlparts[1])
        start = timeit.default_timer()
        h.request('GET', urlparts[2])
        total = timeit.default_timer() - start
    except (HTTPError, URLError):
        total = None
    else:
        h.close()

    return total
