# API for domain register

## 新网

    url = 'http://panda.www.net.cn/cgi-bin/check.cgi'
    data = {'area_domain':'itdhz.com'}

浏览器直接请求

    http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=itdhz.com

返回结果： xml 格式

    <?xml version="1.0" encoding="gb2312"?>
    <property>
    <returncode>200</returncode>
    <key>itdhz.com</key>
    <original>211 : Domain name is not available</original>
    </property>
