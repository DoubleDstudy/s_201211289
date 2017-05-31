# coding: utf-8
import urllib2
import re
from lxml.cssselect import CSSSelector
import lxml.html
import datetime
import webbrowser
from datetime import date,timedelta

def number1():
    url = "http://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=reserve"

    op = urllib2.urlopen(url)
    information = op.read()
    temp = lxml.html.fromstring(information)

    sel2 = CSSSelector("#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(n) > dl > dd.star > dl.info_exp > dd > div > span.num")
    sel1 = CSSSelector("#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(n) > dl > dd.star > dl.info_star > dd > div > a > span.num")
    sel = CSSSelector('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(n) > dl > dt > a')
    result = sel(temp)
    result1 = sel1(temp)
    result2 = sel2(temp)

    print u"영화 예매순 1-20위"
    print "----------"
    for i, node in enumerate(result):
        if(i<20):
            print i+1,u"위 : ",node.text_content()
            if(result1[i].text_content()):
                print u"네티즌 평점 : ",result1[i].text_content(),u"점"

            if(type(result2[i].text_content()) == lxml.etree._ElementStringResult):      
                print u"예매율 : ",result2[i].text_content(),"%"
            print "------------------"

    
def number2():
        #예매순
    url = "http://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=point"

    op = urllib2.urlopen(url)
    information = op.read()
    temp = lxml.html.fromstring(information)

    sel4 = CSSSelector("#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(n) > dl ")

    result = sel4(temp)
    print "******"
    print u"평점순 1-20위"
    print "******"
    for i, node in enumerate(result):
        if(i<20):
            print i+1,u"위 : ",node.cssselect("dt>a")[0].text_content()
            print u"평점 : ",node.cssselect("dd.star>dl>dd>div>a>span.num")[0].text_content(),u"점"
            print u"참여인원 : ",node.cssselect("dd.star>dl>dd>div>a>span.num2>em")[0].text_content(),u"명"
            print "-------------------"

def number3():
        #i 를 줌으로써 페이지를 넘겨서있는 리뷰도 받아올 수 있게 함
    i=0

    score = input('Select score :')
    print u"최신 리뷰 평점",score,u"이상의 영화"
    print "---------------------------"

    #20페이지까지

    while(i<20):
        i = i+1
        reg = re.compile('<br>(.*)')
        _num=str(i)
        #url 페이지 바꾸기
        url = "http://movie.naver.com/movie/point/af/list.nhn?&page="+_num
        op = urllib2.urlopen(url)
        information = op.read()
        temp = lxml.html.fromstring(information)
        sel5 = CSSSelector("#old_content > table > tbody > tr:nth-child(n)")
        result = sel5(temp)


        for node in result:
            #평점 거르기
            pointChange = lxml.html.tostring(node.cssselect('td.point')[0])
            #print lxml.html.tostring(node.cssselect('td.point')[0])
            #print type(pointChange)
            pointRex = re.compile('>(.*)<') 
            pointStr = pointRex.findall(pointChange)[0]
            compare = int(pointStr)
            #평점 기준 9점으로 바꿈
            if(compare >= score):        
                #print node.cssselect('a.movie')[0].text_content()
                print u"영화 : ",node.cssselect('td.title>a.movie')[0].text_content()

                print u"평점 : ",node.cssselect('td.point')[0].text_content(),u"점"
                #print type(node.cssselect('td.point')[0].text_content())

                # review만 빼오기위해서 노드를 다시 str로 변환하고 <br>다음값 정규식으로 추출
                review = reg.findall(lxml.html.tostring(node.cssselect('td.title')[0]))

                #추출된 리뷰는 다시 lxml.html.fromstring으로 변환시켜주기 그냥 쓰면
                # 알아보지 못하는 이상한 값들나옴

                rechange = lxml.html.fromstring(review[0]) 
                print u"리뷰 : ", rechange.text_content()
                print "----------------------------------"

def number4():
    minusDay = 1
    i=0
    print u"20일 동안의 박스오피스 현황 보기"
    print "============================"

    recent = datetime.datetime.now() - timedelta(days=minusDay)

    #정규식을 통해 공백까지 다없애기해서 값 추출
    reg = re.compile('>\s*(.*)\s*<')
    while(True):
        if(i<=20):
            i = i+1
            #print recent
            startDate = str(date(recent.year,recent.month,recent.day)) #"2017-04-07"



            print '-----------'
            print startDate
            print '-----------'
            url = "http://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do?loadEnd=0&searchType=search&sSearchFrom="+startDate+"&sSearchTo="+startDate+"&sMultiMovieYn=&sRepNationCd=&sWideAreaCd="
            op = urllib2.urlopen(url)
            result = op.read()
            change = lxml.html.fromstring(result)
            #sel1 = CSSSelector("#tbody_0 > tr:nth-child(1) > td.title > a")
            #시장에서 영화판도의 흐름 데이터
            sel = CSSSelector("#tbody_0 > tr:nth-child(n)") #> td:nth-child(4)")
            nodes = sel(change)

            #print type(nodes)






            for node in nodes:
                movie = node.cssselect('td.title>a')[0]
                print u"영화 : ",movie.get('title'),"***"

                sell = node.cssselect('td:nth-child(4)')[0]
                a = lxml.html.tostring(sell)    
                store = reg.findall(a)
                print u"매출액 : ", store[0]

                sell = node.cssselect('td:nth-child(7)')[0]
                a = lxml.html.tostring(sell)    
                store = reg.findall(a)
                print u"누적매출액 : ", store[0]

                sell = node.cssselect('td:nth-child(8)')[0]
                a = lxml.html.tostring(sell)    
                store = reg.findall(a)
                print u"관객수 : ", store[0]

                sell = node.cssselect('td:nth-child(10)')[0]
                a = lxml.html.tostring(sell)    
                store = reg.findall(a)
                print u"누적 관객수 : ", store[0]
                print "-----------"
            recent = recent - timedelta(days=minusDay)
        else:
            break    
        #날짜 바꿔주기
        
    #recent = recent - timedelta(days=minusDay)
    
def number5():
    print u'최근 몇년까지의 박스오피스를 볼까요 ?'
    select = input()

    print u"매년 영화 순위 (최근",select,u"년)"
    print "========================="
    now = datetime.datetime.now()
    intYear = now.year
    index = 0
    while(index !=select):
        year = str(intYear)
        print year,u"년 전체 영화 순위 1~50"
        print '--------------------------------'
        url = 'http://www.kobis.or.kr/kobis/business/stat/offc/findYearlyBoxOfficeList.do?loadEnd=0&searchType=search&sSearchYearFrom='+year+'&sMultiMovieYn=&sRepNationCd='

        op = urllib2.urlopen(url)
        r = op.read()
        result = lxml.html.fromstring(r)
        sel = CSSSelector("#td_movie > a")
        sel1 = CSSSelector("#td_totAudiAcc")
        nodes = sel(result)
        nodes1 = sel1(result)
        reg = re.compile('\s*(.*)')
        for i,node in enumerate(nodes):
            movie = reg.findall(node.text_content())[0]
            watchNumber = reg.findall(nodes1[i].text_content())[0]
            print i+1,u"위 :",movie
            print u"관객 수 :",watchNumber
            print 
        index = index+1
        intYear = intYear -1


while(True):
    print
    print u'***********영화 추천 방법***********'
    print u'1 : 박스오피스 영화 예매순 1~20위 조회'
    print u'2 : 박스오피스 영화 평점순 1~20위 조회'
    print u'3 : 입력한 평점 이상의 영화, 최신리뷰 조회(20page)'
    print u'4 : 20일동안의 박스오피스 현황 조회'
    print u'5 : 입력값만큼의 최신 년도 박스오피스 순위 조회'
    print '**********************************'
    print u'0 : 종료'
    select = input()
    print
    if (select==1):
        number1()
    
    elif (select==2):
        number2()
        
    elif(select ==3):
        number3()
    elif(select ==4):
        number4()
    elif(select ==5):
        number5()
    elif(select ==0):
        print 'Bye~'
        break;
