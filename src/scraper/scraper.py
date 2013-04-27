'''
Created on Apr 27, 2013


@author: Christopher
'''

import urllib2
import re
from bs4 import BeautifulSoup # To get everything

c=urllib2.urlopen('http://pc-pdx.com/venues/')

soup=BeautifulSoup(c.read())

divs=soup('div')



# CLAS OF INTEREST IS venue-listing-item
i=0
chare = re.compile(r'[!-\.&]')
for div in soup('div'):
    i=i+1
    #CATCH THE KEYERROR FOR div['class']
    try:
        #print div['class']
        for div_class in div['class']:
            #print a
            if( div_class=='venue-listing-item'):
                #THIS GETS THE NAME OF THE VENUES
                print divs[i].a.get_text()
    except KeyError:
        pass # or some other fallback action
        #print "KEYERROR"
    

    
    if ('class' in dict(div.attrs) and div['class']=='venue-listing-item'):
        items=[re.sub(chare,'',div)]
        print div('a')