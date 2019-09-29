import re
import cpca
import json
while(1):
    string = input()
    if(string=='END'):
        break 
    temp = 2
    if (string[0] == '1'):  # 判断难度
        temp = 1
    elif (string[0] == '2'):
        temp = 2
    string = string[2:]
    string = string[:-1]
    pattern1 = re.compile(r'(.*),')
    namelist = pattern1.findall(string)
    name = ''.join(namelist)  # 名字
    string = string.split(',')[1]
    pattern2 = re.compile(r'\d{11}')
    tellist = pattern2.findall(string)
    tel = ''.join(tellist)  # 电话
    string1 = str(tellist[0])
    string2 = string.split(string1)[0]
    string3 = string.split(string1)[1]
    string = string2 + string3
    list1 = string.split(',')
    add123 = cpca.transform(list1)
    add1 = add123.values[0][0]
    add2 = add123.values[0][1]
    add3 = add123.values[0][2]
    string = add123.values[0][3]
    if (add1 != ''):
        if (string[0] != add1[0] or string[1] != add1[1]):
            add123 = cpca.transform(list1, cut=False)
            add1 = add123.values[0][0]
            add2 = add123.values[0][1]
            add3 = add123.values[0][2]
            string = add123.values[0][3]
    else:
        add123 = cpca.transform(list1, cut=False)
        add1 = add123.values[0][0]
        add2 = add123.values[0][1]
        add3 = add123.values[0][2]
        string = add123.values[0][3]
    if (add1 == '重庆市' or '天津市' or '上海市' or '北京市'):
        add1 = add1.split('市')[0]
    if '街道' in string:  # 四级地址判断
        add4 = string.split('街道')[0] + '街道'
        string = string.split(add4)[1]
    elif '镇' in string:
        add4 = string.split('镇')[0] + '镇'
        string = string.split(add4)[1]
    elif '乡' in string:
        add4 = string.split('乡')[0] + '乡'
        string = string.split(add4)[1]
    elif '民族乡' in string:
        add4 = string.split('民族乡')[0] + '民族乡'
        string = string.split(add4)[1]
    elif '苏木' in string:
        add4 = string.split('苏木')[0] + '苏木'
        string = string.split(add4)[1]
    elif '南山区' in string:
        add4 = '南山区'
        string = string.split(add4)[1]
    else:
        add4 = ''
    add1list = add1.split(',')
    add2list = add2.split(',')
    add3list = add3.split(',')
    add4list = add4.split(',')
    addresslist = add1list + add2list + add3list + add4list
    if (temp == 1):  # 难度一与二的分界
        add5list = string.split(',')
        addresslist = addresslist + add5list
    elif (temp == 2):
        if '街' in string:  # 五级地址判断
            add5 = string.split('街')[0] + '街'
            string = string.split(add5)[1]
        elif '路' in string:
            add5 = string.split('路')[0] + '路'
            string = string.split(add5)[1]
        elif '巷' in string:
            add5 = string.split('巷')[0] + '巷'
            string = string.split(add5)[1]
        elif '胡同' in string:
            add5 = string.split('胡同')[0] + '胡同'
            string = string.split(add5)[1]
        elif '道' in string:
            add5 = string.split('道')[0] + '道'
            string = string.split(add5)[1]
        elif '弄' in string:
            add5 = string.split('弄')[0] + '弄'
            string = string.split(add5)[1]
        else:
            add5 = ''
        if '号' in string:  # 六级地址
            add6 = string.split('号')[0] + '号'
            string = string.split(add6)[1]
        else:
            add6 = ''
        add5list = add5.split(',')
        add6list = add6.split(',')
        add7list = string.split(',')
        addresslist = addresslist + add5list + add6list + add7list
    a = {"姓名": name, "手机": tel, "地址": addresslist}
    answer = json.dumps(a, ensure_ascii=False)
    print(answer)
