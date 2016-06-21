#-*- coding: UTF-8 -*-
# Get latest wallpaper from https://alpha.wallhaven.cc
# Auther: fengcc
# 2016-6-20

import os
import urllib
import urllib2
import re
from time import ctime, sleep

def testNetwork():
    import subprocess

    fnull = open(os.devnull, 'w')
    ret = subprocess.call('ping www.baidu.com', shell = True, stdout = fnull, stderr = fnull)
    fnull.close()
    
    return ret

def main():
    # Wait computer establish the connection
    sleep(10)

    log = open('log.txt', 'a')

    # Test whether the network is connected
    if testNetwork():
        log.write('[%s] The network is not connected !%s' % (ctime(), os.linesep))
        log.close()
        return

    url = r'https://alpha.wallhaven.cc/search?categories=111&purity=100&ratios=16x10&sorting=date_added&order=desc&page=1'
    user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) Chrome/47.0.2526.106 Safari/537.36'
    header = {'User-Agent' : user_agent}
    
    try:
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('data-wallpaper-id="([0-9]+)"')
        number = re.search(pattern, content).group(1)
        
        url = r'https://alpha.wallhaven.cc/wallpaper/' + number
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile('id="wallpaper" src="(.+?)"')
        url = r'https:' + re.search(pattern, content).group(1)
        
        log.write('[%s] %s%s' % (ctime(), url, os.linesep))
        log.write('[%s] Downloading the wallpaper...%s' % (ctime(), os.linesep))
        path = ur'F:\图片\壁纸\\' + re.search(r'(wallhaven-.+)', url).group(1)
        request = urllib2.Request(url, headers = header)
        response = urllib2.urlopen(request)
        content = response.read()
        f = open(path, 'wb')
        f.write(content)
        log.write('[%s] The wallpaper was downloaded successfully !%s' % (ctime(), os.linesep))
    
    except (IOError, urllib2.URLError), e:
        log.write(('[%s] ' % ctime()) + e)
    
    finally:
        log.write(os.linesep)
        f.close()
        log.close()

if __name__ == '__main__':
    main()
