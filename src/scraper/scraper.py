'''
Created on Apr 27, 2013


@author: Christopher
'''

import urllib2

from bs4 import BeautifulSoup # To get everything

c=urllib2.urlopen('http://kiwitobes.com/wiki/Programming_language.html')

soup=BeautifulSoup(c.read())

links=soup('a')

links[10]