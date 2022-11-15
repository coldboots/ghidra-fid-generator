#!/usr/bin/env python


# get directory listing from http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/
# for reach a html tag extract the href attribute.
# If the href value ends with .deb, then print the href value and starts with libc6-dev,
# download the file to the directory 'debs'

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

#url = 'http://no.archive.ubuntu.com/ubuntu/pool/main/g/glibc/'
url = 'http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/'
page = urlopen(url)
soup = BeautifulSoup(page, features="html.parser")

for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.deb'):
        if href.startswith('libssl-dev'): # libc6-dev
            print(href)
            urlretrieve(url + href, 'debs/' + href)
