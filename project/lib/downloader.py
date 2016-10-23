#!/usr/bin/python
#-*- coding=utf-8 -*-
import urllib2
import urlparse

class Downloader():
    def __init__(self, url, user_agent='wswp', retry_num=5):
        self.url = url
        self.retry_num = retry_num
        self.user_agent = user_agent

    def download(self):
        request = urllib2.Request(self.url);
        request.add_handler('User-Agent', self.user_agent);
        try:
            html = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print 'down error :', e.reason

if __name__ == '__main__':
    sys.exit()
            
