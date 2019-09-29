# -*- coding: utf-8 -*-
import json
import re

def get_province(string):      ##获得省
    str=re.search(("(.*?省)|(.*?自治区)|上海市|北京市|天津市|重庆市"),string)
    if str!=None:
        length=len(str.group())
    if str==None or length>=4:
        if string[0:3] == "黑龙江" or string[0:3] == "内蒙古":
            return string[0:3]
        else:
            return string[0:2]
    return str.group()

def get_city(string):           
    str=re.search("(.*?自治州)|(.*?[市])",string)
    if str!=None:
        return ""
    return str.group()

def get_county(string):            #获得县
    str=re.search("(.*?自治旗)|(.*?[县区市旗])",string)
    if str!=None:
        return ""
    return str.group()

def get_town(string):         #获得城镇
    str=re.search("(.*?[镇乡])|(.*?街道)|(.*?民族乡)|(.*?苏木)",string)
    if str==None:
        return ""
    return str.group()

def get_road(string): #获得路
    str=re.search("(.*?[路街巷道])",string)
    if str==None:
        return ""
    return str.group()

def get_doornum(string):                         #获得门牌号
    str=re.search("(.*?[号])",string)
    if str==None:
        return ""
    return str.group()

def main(inxx):
    string=inxx
    dict={}
    list=[]
    dif=0
    if string[:2]=="1!":
        dif=1
    elif string[:2]=="2!":
        dif=2
    else:
        dif=3
    string=string[2:]

    dict['姓名']=re.search('[^,]+',string).group()  #提取名字
    string=re.sub('.+,','',string)    #删除字符串中的名字

    dict['手机']=re.search('\d{11}',string).group()    #提取手机号码
    string=re.sub('\d{11}','',string)     #删除字符串中的号码
    str=re.search('.{2}',string).group() 

    province=get_province(str)
    if province in ('北京','上海','天津','重庆'):
        province=province
        str=str.replace(province,province+"市",1)
    elif province in ('北京市', '上海市', '天津市', '重庆市'):
        province=province[0:2]
    elif province=="广西":
        str=str.replace(province,"",1)
        province=province + "壮族自治区"
    elif province=="新疆":
        str=str.replace(province,"",1)
        province=province+"维吾尔自治区"
    elif province=="宁夏":
        str=str.replace(province,"",1)
        province=province+"回族自治区"
    elif province=="内蒙古" or province == "西藏":
        str=str.replace(province,"",1)
        province=province+"自治区"
    elif province[-1]!="省" and province[-1]!="区":           
        str=str.replace(province,"",1)
        province=province+"省"
    else:
        str=str.replace(province,"",1)

    city=get_city(str)

    str=str.replace(city,"",1)
    

    county = get_county(str)
    str = str.replace(county, "", 1)
    county=get_county(str)
    town=get_town(str)
    str=str.replace(town,"",1)
    five=str

    road=get_road(str)
    str=str.replace(road,"",1)

    doornum=get_doornum(str)
    str=str.replace(doornum,"",1)

    if dif=='1':
        list.append(province)
        list.append(city)
        list.append(county)
        list.append(town)
        list.append(five)
    else:
        list.append(province)
        list.append(city)
        list.append(county)
        list.append(town)
        list.append(road)
        list.append(doornum)
        list.append(str)

    dict["地址"]=list
    print(json.dumps(dict,ensure_ascii=False))
while True:
    input1=input()
    if(input1=='END'):
        break;
    main(input1)
