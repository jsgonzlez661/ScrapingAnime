#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Jose Gonzalez ~ All rights reserved.

import requests
from bs4 import BeautifulSoup


zippyshare = []
streamtape = []

for i in range(144, 207):
    # Modificar colocar el link un video
    # Eliminar el numero al final del link
    link = 'https://www3.animeflv.net/ver/one-piece-tv-{0}'.format(i)
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')

    enlaces = soup.find_all('a', class_="Button Sm fa-download")
    for enlace in enlaces:
        href = enlace.get('href')
        if('zippyshare' in href):
            zippyshare.append(href)
        if('streamtape' in href):
            streamtape.append(href)


for zippy in zippyshare:
    print(zippy)

print('\n')

for stream in streamtape:
    print(stream)
