#!/usr/bin/python
#!-*- coding=utf-8 -*-
import sys
import urllib2
import urlparse
import re
import itertools


def download(url, user_agent='wswp', try_num=2):
    '''打开网页下载'''
    print 'download...:', url
    heards = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=heards)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "Error:", e.reason
        html = None
        if try_num > 0:
            if hasattr(e, 'code') and (500 <= e.code <= 600):
                return download(url, user_agent, try_num-1)
    return html

#网站地图下载
def downsitemap(url):
    xml = download(url)
    links = re.findall('<loc>(.*?)</loc>', xml)
    print "links ..:", links
    for link in links:
        print link
        html = download(link)

#遍历id下载
def downforid(url, maxError=5):
    maxNum = maxError;
    for page in itertools.count(1):
        idUrl = '{0}/view/-{1}'.format(url, page)
        print idUrl
        html = download(idUrl)
        if html is None:
            maxNum -= 1
        else:
            maxNum = maxError;
        if maxNum <= 0:
            break

def down_by_link(seekUrl, linkRegex):
    crawlQueue = [seekUrl]
    while crawlQueue:
        url = crawlQueue.pop()
        html = download(url)
        if html is None: continue
        for link in get_links(html):
            crawlQueue.append(link)

def get_links(html):
    webpageRex = re.compile('<a[^>]+href=["\'](.*?)')


if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit()
    url = str(sys.argv[1]) 
    downforid(url)
