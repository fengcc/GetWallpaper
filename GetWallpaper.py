#-*- coding: UTF-8 -*-
# Get latest wallpaper from https://alpha.wallhaven.cc
# Auther: fengcc
# 2016-6-20

import urllib
import urllib2
import re

def main():
    page = 1
    url = r'https://alpha.wallhaven.cc/search?categories=111&purity=100&ratios=16x10&sorting=date_added&order=desc&page=1'
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/47.0.2526.106 Safari/537.36'
    header = {'User-Agent' : user_agent}
    try:
        print 'Connecting....'
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('data-wallpaper-id="([0-9]+)"')
        number = re.search(pattern, content).group(1)
        
        print 'Get the latest wallpaper...'
        url = r'https://alpha.wallhaven.cc/wallpaper/' + number
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('id="wallpaper" src="(.+?)"')
        url = r'https:' + re.search(pattern, content).group(1)
        
        print 'Downloading the wallpaper...'
        path = ur'F:\图片\壁纸\\' + re.search(r'(wallhaven-.+)', url).group(1)
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read()
        #path = unicode(path, 'utf8')
        f = file(path, 'wb')
        f.write(content)
        f.close()
        print 'The wallpaper was downloaded successfully !'
    except urllib2.URLError, e:
        if hasattr(e, 'code'):
            print e.code
        if hasattr(e, 'reason'):
            print e.reason

if __name__ == '__main__':
    main()
