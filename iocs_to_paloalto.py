#!/usr/bin/python
# encoding: utf8

import csv
import sys
import io
import os
import json
from operator import itemgetter
import time
from optparse import OptionParser
from webstart import webstart

banner="""
ヾ(　 　)ノ゛天ヾ(　°д)ノ゛际ヾ(°д°)ノ゛友ヾ(д°　)ノ゛盟ヾ(　　)
"""
print banner

# 获取脚本位置路径
path = os.path.split(os.path.realpath(__file__))[0] + '/'
os.chdir(path)

# 判断文件位置是否存在，若不存在则创建，用于存放规则文件
domainpath = 'EDL/'
if not os.path.exists(domainpath):
    os.makedirs(domainpath)
    print domainpath + ' has been created!'

# 解决错误UnicodeEncodeError: 'ascii' codec can't encode characters in position 5-6
reload(sys)
sys.setdefaultencoding('utf-8')




def transforms(iocs,minscore,count,SETNAME):
    ip_l = list()
    domain_l = list()
    url_l = list()
    csv_l = list()

    csvhead = [u'category', u'geo', u'value', u'score', u'created_time', u'type', u'source_ref']

    with io.open(iocs,"r",encoding="utf8") as f:
        dr = csv.DictReader(f, csvhead)
        # 跳过表头
        next(dr, None)
        # 格式转换
        for i in dr:
            i['score'] = float(i.get('score',0.0))

            csv_l.append(i)

    # 分值排序
    csv_l_s = sorted(csv_l,key=itemgetter('score'),reverse=True)
    # print len(csv_l_s)

    # 进行分值和类别处理
    for i in csv_l_s:
        if i['score'] >= minscore:
            if i["type"] == "feed_ipv4":
                ip_l.append(i)
            elif i["type"] == "feed_domain":
                domain_l.append(i)
            else:
                url_l.append(i)
        else:
            break

    # print len(url_l)
    # print len(domain_l)
    # print len(ip_l)
    
    print("\n--(oﾟωﾟo)---- ↓↓ 外部动态列表生成中 ↓↓ ------")

    # 外部动态列表生成
    with io.open(domainpath+SETNAME+"_ip.txt","wb") as f:
        for i in ip_l[:count]:
            f.writelines(i['value']+"\n")
        print("IP Min Value is %0.2f"%i['score'])
    
    with io.open(domainpath+SETNAME+"_domain.txt","wb") as f:
        for i in domain_l[:count]:
            f.writelines(i['value']+"\n")
        print("Domain Min Value is %0.2f"%i['score'])

    with io.open(domainpath+SETNAME+"_url.txt","wb") as f:
        for i in url_l[:count]:
            f.writelines(i['value']+"\n")
        print("URL Min Value is %0.2f"%i['score'])
    
    print("外部动态列至EDL成功！")

    webstart(SETNAME)



def main(argv=None):

    # 获取系统日期
    datestamp = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    IOCS_CSVNAME = "archive/IOCS_"+datestamp+".csv"
    # 设置参数读取
    parser = OptionParser(usage="usage: %prog -f "+IOCS_CSVNAME)
    parser.set_defaults(filepath=IOCS_CSVNAME)
    parser.set_defaults(minscore=0.0)
    parser.set_defaults(count=5000)
    parser.add_option("-f","--file",help="file path of IOCs file",dest="filepath",metavar="FILE")
    parser.add_option("-m","--min",help="minimum value of score in IOCs",dest="minscore",metavar="80.0",type="float")
    parser.add_option("-c","--count",help="number of lines in the External Dynamic Lists",dest="count",metavar="500",type="int")
    

    (options, args) = parser.parse_args()
    
    print("└(￣^￣ )┐------ ↓↓ 正在进行脚本初始化配置 ↓↓ ------")
    # 从config中获取参数
    with io.open("config","r",encoding="utf8") as f:
        j = json.load(f)
        SETNAME = str(j[u"SetName"])
        if len(SETNAME):
            print("SetName is : "+SETNAME)
        else:
            print("config文件中SetName参数缺失！")
            exit(0)

    if options.filepath:
        print "IOCs file is : %s" % options.filepath
    if options.minscore:
        print "Minimum value is : %0.2f" % options.minscore
    else:
        print "No credit value filter set"
    if options.count:
        print "Lines Counts is : %d" % options.count
    
    transforms(options.filepath,options.minscore,options.count,SETNAME)


if __name__ == '__main__':
    main()
