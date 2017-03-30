# coding: utf-8

import urllib
import re

uResponse = urllib.urlopen('http://python.org/')
_html = uResponse.read()

p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "http url Count?",len(nodes)
for i, node in enumerate(nodes):
    print i,"th", node
    
