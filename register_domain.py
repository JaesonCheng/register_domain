#!/usr/bin/env python
#-*-coding:utf8-*-
# Author JaesonCheng
# Date 2017-05-16
 
import urllib2
from multiprocessing import Pool
import itertools as its

def writelog(mfile,message):
    with open(mfile,'a+') as f:
        f.write(message)
 
def createdomain(ws,num,sfx):
    r = its.product(ws,repeat=num)
    for i in r:
        domain = ''.join(i) + sfx
        yield domain

def checkdomainstatus(domain):
    API = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain="
    url = API + domain
    try:
        xhtml = urllib2.urlopen(url,timeout=5).read()
    except:
        return
    r1 = xhtml.find('211')      # 字符串表示 已经被注册
    r2 = xhtml.find('210')      # 字符串表示 还未被注册
    if r2 != -1:
         writelog('domain_enable.txt',domain+'\n')
    #else:
    #    if r1 != -1:
    #        writelog('domain_unkown.txt',domain+'\n')
    #    else:
    #        writelog('domain_disable.txt',domain+'\n')

if __name__ == "__main__":
    words = 'abcdefghijklmnopqrstuvwxyz'
    len = 5
    suffix = '.com'
    domains = createdomain(words,len,suffix)
    task_pool = Pool(5)
    results = task_pool.map(checkdomainstatus,domains)
    task_pool.close()
    task_pool.join()
