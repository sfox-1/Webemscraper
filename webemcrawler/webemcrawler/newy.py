#!/usr/bin/env python

from bs4 import BeautifulSoup
import sqlite3
import urllib
import itertools
import re


def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in
            itertools.chain.from_iterable(itertools.product(charset, repeat=i)
                                          for i in range(1, maxlength + 1)))

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()
conn.text_factory = str

cur.executescript('''

CREATE TABLE IF NOT EXISTS Domain (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      URL TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Email (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      email TEXT UNIQUE
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
            print urls, "dead link or empty domain!"
            continue
        else:
            print urls, "Is a valid and working site"
            cur.execute('''INSERT OR IGNORE INTO Domain (URL) VALUES ( ? )''',
                        (urls, ))
            emails = re.findall('[aA-zZ]+?@[aA-zZ]+[.][aA-zZ]+', str(bs))
            for mail in emails:
                print mail, "going into database"
                cur.execute(
                    '''INSERT OR IGNORE INTO Email (email) VALUES ( ? )''',
                    (mail, ))
            conn.commit()
            continue
    except Exception as e:
        print urls, "no address associated with hostname"
        pass
cur.close()
