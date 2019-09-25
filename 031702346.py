import re   #正则表达式
import json
string=input()
dict={}   #字典
list=[]   #列表

dict['姓名']=re.search('[^,]+',string).group()  #提取名字
string=re.sub('.+,','',string)    #删除字符串中的名字

dict['手机']= re.search('\d{11}',string).group()    #提取手机号码
string=re.sub('\d{11}','',string)     #删除字符串中的号码

str=re.search('.{2}',string).group()  #省
flag=re.search('.+?省',string)   #标记flag判断是否需要加省
if str=='北京'or str== '天津'or str=='上海'or str=='重庆':    #四个直辖市不需加省
    list.append(str)
elif flag!=None:  
    str=re.search('.+?省', string).group() 
    string = string.replace(str, '', 1)
    list.append(str)
else:      
    str = re.search('..', string).group()
    string = string.replace(str, '', 1)
    list.append(str+'省')

flag = re.search('.+?市', string)  #市
if flag != None :
    str = re.search('.+?市', string).group()
    string = string.replace(str, '', 1)
    list.append(str)
else:
    str = re.search('..', string).group()
    string = string.replace(str, '', 1)
    list.append(str+'市')

flag = re.search('.+?(?:县|区)', string)  #县/区
if flag != None :
    str = re.search('.+?(?:县|区)', string).group()
    string = string.replace(str, '', 1)
    list.append(str)
else:
    list.append('')

flag = re.search('..+?(?:镇|街道)', string)  #镇/街道/乡
if flag != None :
    str = re.search('..+?(?:镇|街道|乡)', string).group()
    string = string.replace(str, '', 1)
    list.append(str)
else:
    list.append('')

flag = re.search('.+?(?:路|巷|街|道|乡)', string)  #路/巷/街
if flag != None :
    str = re.search('.+?(?:路|巷|街|道|乡)', string).group()
    string = string.replace(str, '', 1)
    list.append(str)
else:
    list.append('')

flag = re.search('.+?(?:号|村)', string)  #号
if (flag != None) :
    str = re.search('.+?(?:号|村)', string).group()
    string = string.replace(str, '', 1)
    list.append(str)
else:
    list.append('')

flag = re.search('[^\.]+', string)  #具体地址
if flag != None :
    str = re.search('[^\.]+', string).group()
    list.append(str)
else:
    list.append('')

dict['地址'] = list
json_str = json.dumps(dict,ensure_ascii=False)
print(json_str)  