#!/usr/bin/env python

from bs4 import BeautifulSoup
import sqlite3
import urllib
import itertools


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in
            itertools.chain.from_iterable(itertools.product(charset, repeat=i)
                                          for i in range(1, maxlength + 1)))

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()
conn.text_factory = str

cur.executescript('''

CREATE TABLE IF NOT EXISTS Valid (
      URL TEXT UNIQUE
)
''')
url = list(bruteforce('abcdefghijklmnopqrstuvwxyz', 2))
# domain = list(bruteforce('abcdefghijklmnopqrstuvwxyz', 3))
for urls in url:
    # urls = ".".join((urls, com))
    try:
        urls = 'http://{0}.{1}'.format(urls, 'com')
        bs = BeautifulSoup(urllib.urlopen(urls).read(), "html.parser")
        if 'FailedURI' in str(bs):
            print urls, 'dead link or empty domain!'
            continue
        else:
            print urls, "THIS ONE WORKS"
            cur.execute('''INSERT OR IGNORE INTO Valid (URL) VALUES ( ? )''',
                        (urls, ))
            conn.commit()
            continue
    except Exception as e:
        print urls, "no address associated with hostname"
        pass
cur.close()
