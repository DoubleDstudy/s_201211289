# coding: utf-8
import lxml.html
import requests

from lxml.cssselect import CSSSelector

keyword = '비오는'
url1 = "http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0"
r = requests.get(url1)
_html = lxml.html.fromstring(r.text)

sel = CSSSelector('table > tbody > ._tracklist_move>.name>a.title')
nodes = sel(_html)

for node in nodes:
    print node.text_content()