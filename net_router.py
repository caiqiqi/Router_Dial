#!/usr/bin/env python
# coding: utf-8

"""
各个型号的路由器登陆模块
"""
import urllib2

class model:

    def __init__(self):
        pass

    @staticmethod
    def TL_WR740N(self, auth, pin, pwd): # dial process for TP_Link
        # 用来连接的
        con_url = '''http://192.168.1.1/userRpm/PPPoECfgRpm.htm?
&wan=0&wantype=2&VnetPap=201&linktype=4&waittime=&Connect=%%C1%%AC+%%BD%%D3
&acc=%s&psw=%s'''.replace('\n','') # Dial url

        # 用来断开连接的
        discon_url='''http://192.168.1.1/userRpm/PPPoECfgRpm.htm?
wan=0&wantype=2&acc=%s&psw=%s&confirm=%s&specialDial=100&SecType=0&
sta_ip=0.0.0.0&sta_mask=0.0.0.0&linktype=4&waittime2=0
&Disconnect=%%B6%%CF+%%CF%%DF'''.replace('\n','') # Disconnect Url

        # str[0:-1]就是原字符串去掉最后一个字符的结果(其实就是去掉由encode(base64)生成的字符串尾的"\n")
        auth = auth.encode("base64")[0:-1]
        # % (pin,pwd)就是用这个tuple来替换掉con_url中的两处 %s
        dial_url = con_url % (pin, pwd)
        # 同理这里的 % 也是用来替换discon_url中出现的三个%s
        dis_url = discon_url % ("admin", "pass", "pass")


        print dis_url

        # At first stop the auto dial function
        dis_req = urllib2.Request(url = dis_url, headers = {'Authorization': 'Basic ' + auth})
        dis_res = urllib2.urlopen(dis_req, timeout=200)     # 200秒的超时时长
        dis_res.close()

        print dial_url
        # Then dial
        dial_req = urllib2.Request(url = dial_url, headers = {'Authorization': 'Basic ' + auth})  # 用户名和密码
        dial_res = urllib2.urlopen(dial_req, timeout=200)
        dial_res.close()

    @staticmethod
    def TL_WR740N5_3_16(self, auth, pin, pwd): # dial process for TP_Link
        # replace('\n','')是将换行符替换成空字符(因为，为了阅读方便而将一个字符串拆成了四行，然后再写一句replace换回来)
        con_url = '''http://192.168.1.1/userRpm/PPPoECfgRpm.htm?
wan=0&wantype=2&specialDial=100&SecType=0&sta_ip=0.0.0.0&
sta_mask=0.0.0.0&linktype=1&waittime=2&Connect=%%C1%%AC+%%BD%%D3
&acc=%s&psw=%s&confirm=%s'''.replace('\n','') # Dial url


        discon_url='''http://192.168.1.1/userRpm/PPPoECfgRpm.htm?
wan=0&wantype=2&acc=%s&psw=%s&confirm=%s&specialDial=100&SecType=0&
sta_ip=0.0.0.0&sta_mask=0.0.0.0&linktype=4&waittime2=0
&Disconnect=%%B6%%CF+%%CF%%DF'''.replace('\n','') # Disconnect Url

        auth = auth.encode("base64")[0:-1]
        #print auth
        dial_url = con_url % (pin, pwd, pwd)
        dis_url = discon_url % ("admin", "pass", "pass")


        print dis_url
        # At first stop the auto dial function
        dis_req = urllib2.Request(url = dis_url, headers = {'Authorization': 'Basic ' + auth, 'Referer':' http://192.168.1.1/userRpm/PPPoECfgRpm.htm'})
        dis_res = urllib2.urlopen(dis_req, timeout=200)
        #print dis_res.read()
        dis_res.close()

        print dial_url
        # Then dial
        dial_req = urllib2.Request(url = dial_url, headers = {'Authorization': 'Basic ' + auth, 'Referer':' http://192.168.1.1/userRpm/PPPoECfgRpm.htm'})  # 用户名和密码
        dial_res = urllib2.urlopen(dial_req, timeout=200)
        #print dial_res.read()
        dial_res.close()


