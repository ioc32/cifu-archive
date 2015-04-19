#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import lxml
import lxml.html
from string import Template
from datetime import datetime
import os.path
import locale
from Queue import Queue
from threading import Thread
import logging
import re

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

atj_urls = Template('http://www.rtve.es/alacarta/interno/contenttable.shtml?pbq=$i&ctx=1875&locale=es&resetFilter=true')
jpqs_urls = Template('http://www.rtve.es/alacarta/interno/contenttable.shtml?pbq=$i&orderCriteria=DESC&modl=TOC&locale=es&pageSize=15&ctx=1999')

locale.setlocale(locale.LC_TIME, 'es_ES')
invalid_chars = '*/'

q = Queue()

def save_show(d):
    (path, link), = d.items()
    logging.debug('{0}, {1}'.format(path, link))
    if os.path.isfile(path + '.mp3'):
        logging.info('{0} exists, skipping'.format(path))
    else:
        logging.info('downloading {0}'.format(link))
        r = requests.get(link)
        logging.info('downloaded {0}'.format(link))
        with open(path + '.tmp', 'wb') as fd:
            logging.info('saving to {0}'.format(path + '.tmp'))
            fd.write(r.content)
        os.rename(path + '.tmp', path + '.mp3')
        logging.info('moved to {0}'.format(path + '.mp3'))

def sanitise_filename(filename):
    return ''.join(c for c in filename if c not in invalid_chars)

def get_shows(name, urls, depth):
    ss = []
    for i in range(1, depth):
        html = lxml.html.parse(urls.substitute(i=i))
        logging.debug('fetched: ' + urls.substitute(i=i))
        shows = html.xpath('//*[@class="odd"]')
        shows.extend(html.xpath('//*[@class="even"]'))
        for show in shows:
            try:
                s = {}
                t = sanitise_filename(show.xpath('.//div[1]//span[1]//span[3]/a')[0].text.strip().encode('latin-1'))
                l = show.xpath('.//span[2]//a')[0].attrib.get('href')
                try:
                    f = datetime.strptime(show.xpath('.//*[@class="fecha"]')[0].text, '%d %b %Y').strftime('%Y-%m-%d')
                except Exception as e:
                    f = 'NA-' + show.xpath('.//*[@class="fecha"]')[0].text.strip().encode('latin-1')
                s[name + '-' + f + '-' + t] = l
                q.put(s)
            except Exception as e:
                logging.error(e)
                pass

def get_last(url):
    html = lxml.html.parse(url.substitute(i=1))
    last_url = html.xpath('//*[@class="ultimo"]/a')[0].attrib.get('href')
    m = re.search(r'pbq=(\d+)', last_url)
    last_index = int(m.group(1))
    return last_index + 1

def worker():
    while True:
        item = q.get()
        save_show(item)
        q.task_done()

#get_shows('atj', t1, 45)
#get_shows('jpqs', t2, 58)
get_shows('atj', atj_urls, get_last(atj_urls))
get_shows('jpqs', jpqs_urls, get_last(jpqs_urls))

for i in range(8):
     t = Thread(target=worker)
     t.setDaemon = True
     t.start()

q.join()
