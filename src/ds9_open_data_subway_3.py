import os
import src.mylib
import urlparse
import re
import requests

n = 1

    
while(n<10):
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=src.mylib.getKey(keyPath)
    KEY=str(key['dataseoul'])
    TYPE='xml'
    SERVICE='SearchSTNBySubwayLineService'

    START_INDEX=str(1) 
    END_INDEX=str(10)
    LINE_NUM=str(n)

    params=KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX+'/'+LINE_NUM


    _url='http://openAPI.seoul.go.kr:8088/'
    url=urlparse.urljoin(_url,params)

    data=requests.get(url).text
    p=re.compile('<STATION_NM>(.*)</STATION_NM>')
    res=p.findall(data)
    print '-----------'
    print n,"line"
    for item in res:
        
        print item
    n = n+1

