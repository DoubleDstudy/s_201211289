import os
import requests
import mylib
import re

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=mylib.getKey(keyPath)
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api=_url+'/'+_key+'/'+_type+'/'+_service+'/'+str(_start_index)+'/'+str(_end_index)+'/'+_use_mon
response = requests.get(_api).text

p=re.compile('<RIDE_PASGR_NUM>(.*)</RIDE_PASGR_NUM>')
p1=re.compile('<ALIGHT_PASGR_NUM>(.*)</ALIGHT_PASGR_NUM>')
p2=re.compile('<LINE_NUM>(.*)</LINE_NUM>')
p3=re.compile('<SUB_STA_NM>(.*)</SUB_STA_NM>')
res=p.findall(response)
res1=p1.findall(response)
res2=p2.findall(response)
res3=p3.findall(response)



for i,node in enumerate(res):
    print 'Line Num :',res2[i]
    print 'Station Name :',res3[i]
    print 'Ride Sum :',node
    print 'Alright Sum :',res1[i]
    print '----------------'