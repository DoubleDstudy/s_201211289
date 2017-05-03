import os
import requests
import mylib
import re
import json

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=mylib.getKey(keyPath)
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='json'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'

_maxIter=2
_iter=0
data ='d'
while _iter<_maxIter:
    _api=_url+'/'+_key+'/'+_type+'/'+_service+'/'+str(_start_index)+'/'+str(_end_index)+'/'+_use_mon
    #print _api
    response = requests.get(_api).text
    data = response
    #print response
    _start_index+=5
    _end_index+=5
    _iter+=1



jd = json.loads(data)
#print jd['STATION_NM']
#for key,value in jd.items():
#    print "---",key,value

#print jd['CardSubwayStatisticsService']['row'][0]
#n=len(jd['SearchSTNBySubwayLineService']['row'])
#for i in range(0,n):
#    print jd['SearchSTNBySubwayLineService']['row'][i]
for item in jd['CardSubwayStatisticsService']['row']:
    #print item.keys()
    for i in item.keys():
        if i=='SUB_STA_NM':
            #print item.values()
            print 'Station Name :',item.values()[4]
            print 'Alight Num :',item.values()[5]
            print 'Ride Num :',item.values()[1]