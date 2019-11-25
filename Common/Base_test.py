import unittest
import pymysql
import requests
import json
from Logs.log import log1
import getcwd
import os
import configparser
import random
import psutil,time
path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')

class webrequests(object):
    '''tool'''
    def get(self,url,params=None,headers=None,files=None):
        '''封装get方法，return响应码和响应内容'''
        try:
            r = requests.get(url,params = params,headers = headers,files=files)
            log1.info("请求的内容：%s" % params)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response_json)
            return status_code,response_json    # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！",exc_info=1)
    def post(self, url, data=None, headers=None,files=None):
        '''封装post请求，return响应码和响应内容'''
        try:
            r = requests.post(url, data=data, headers=headers,files=files)
            log1.info("请求的内容：%s" % data)
            status_code = r.status_code  # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response_json)
            return status_code,response_json    # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！",exc_info=1)
    def post_session(self,url,data=None,headers=None,files=None):
        try:
            config = configparser.ConfigParser()
            config.read(config_path, encoding="utf-8-sig")
            da = config.items('user')
            da2 = dict(da)  #入参转成字典的格式
            login_url = 'http: // admin.tjs.com / login.html'
            sess = requests.session()
            sess.post(login_url,da2)
            sess2 = sess.post(url, data)
            log1.info("请求的内容：%s" % data)
            status_code = sess2.status_code # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response_json = sess2.json() # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response_json)
            return status_code, response_json# 返回响应码，响应内容

        except BaseException as e:
            log1.error("请求失败", exc_info=1)
    def post_json(self,url,data=None,headers=None):
        '''封装post方法，并用json格式传值，return响应码和响应内容'''
        try:
            data = json.dumps(data).encode('utf-8')  # python数据类型转化为json数据类型
            r = requests.post(url, data=data, headers=headers)
            log1.info("请求的内容：%s" % data)
            status_code = r.status_code   # 获取返回的状态码
            log1.info("获取返回的状态码:%d" % status_code)
            response = r.json()   # 响应内容，json类型转化成python数据类型
            log1.info("响应内容：%s" % response)
            return status_code,response    # 返回响应码，响应内容
        except BaseException as e:
            log1.error("请求失败！",exc_info=1)
    def getdict(self,dict1,obj,default=None):
        ''' 遍历嵌套字典，得到想要的value
            dict1所需遍历的字典
            obj 所需value的键'''
        for k,v in dict1.items():
            if k == obj:
                return v
            else:
                if type(v) is dict:
                    re = webrequests.getdict(self,v,obj,default)    # 递归
                    if re is not default:
                        return re
    def getdict_hopeval(self,dic, obj):
        ''' 遍历嵌套字典，得到想要的value或key
            dict1所需遍历的字典
            obj 所需key的键

            返回最后一级字典的key的列表
            '''
        a = []
        try:
            for k, v in dic.items():
                if k == obj:
                    for k2,v2 in v.items():
                        a.append(k2)
                    return a
                elif type(v) is dict:
                    re = webrequests.getdict_hopeval(self, v, obj)
                    if re is not None:
                        return re


        except BaseException as t:
            log1.error("获取失败！", exc_info=1)
    def getdict_hopeval_value(self,dic, obj):
        ''' 遍历嵌套字典，得到想要的value或key
            dict1所需遍历的字典
            obj 所需key的键

            返回最后一级字典的value的列表
            '''
        a = []
        try:
            for k, v in dic.items():
                if k == obj:
                    for k2,v2 in v.items():
                        a.append(v2)
                    return a
                elif type(v) is dict:
                    re = webrequests.getdict_hopeval_value(self, v, obj)
                    if re is not None:
                        return re
        except BaseException as t:
            log1.error("获取失败！", exc_info=1)
    def confige_get(self,section,key,url=None):
        '''读取配置文件字段的值并返回'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        if key =='url':
            config_url = config.get(section,key)
            url = config_url
            log1.info("请求的url：%s" % url)
            return url
        else:
            config_get = config.get(section,key)
            return  config_get
    def config_write(self,section,key = None,value = None):
        '''往配置文件写入键值'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        if key is not None and value is not None:
            config.set(section,key,value)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
        else:
            config.add_section(section)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
    def config_delete(self,section,key = None):
        '''删除配置文件字段'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        if key is not None :
            config.remove_option(section,key)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
        else:
            config.remove_section(section)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
    def confige_options(self,section):
        '''读取配置文件某section下所有键'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        username = config.options(section)
        return username
    def confige_items(self,section):
        '''读取配置文件某section下所有key ,value 并转换成字典形式'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding='utf-8')
        data = dict(config.items(section))
        return data
    def get_addkey(self,user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.confige_get('addressed', i)
                L.append(emails)
                sum += 1
        return L
    def mobile_num(self):
        '''随机生成手机号'''
        try:
            lis = ['189','159','187','136','176','134']
            var = random.choice(lis)+''.join(str(random.choice(range(10)))for i in range(8))
            print('号码%s'%var)
            return var
        except BaseException as e:
            log1.error("生成失败！",exc_info=1)
    def get_identifying_code(self,sql,pram,DB):
        '''数据库中获取验证码'''
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()

        Sql = sql
        cursor.execute(Sql)
        connection.commit()
        results = cursor.fetchall()
        # print(results)
        for row in results:
            code = row[pram]
            # print(code)
        connection.close()
        return code
    def get_identifying_code2(self,sql,pram,DB):
        '''数据库中获取验证码'''
        connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()

        Sql = sql
        cursor.execute(Sql)
        connection.commit()
        results = cursor.fetchall()
        return  results
    def get_codeList(self,code):
        """ 将获取到的code验证码拆成元素放到codelist中"""
        try:
            codelist = []
            a = 10 ** (int(len(str(code))) - 1)  # 10的len(code)-1次方
            for i in range(len(str(code))):
                if a > 0:
                    codelist.append(int((code / a) % 10))
                    a /= 10
                    # print('ss', a)

                else:
                    print('运算结束')
            # print(codelist)
            return codelist
        except BaseException as e:
            log1.error('获取失败',exc_info=1)
    def CreatProduct(self,creatr_url,create_post_date):
        try:
            session = requests.Session()
            host = "http://admin.tjs.net"
            login_url = "http://admin.tjs.net/login.html"
            login_post_data = {
                "phone": "15268299107",
                "password": "aa111111"
            }
            session.post(login_url, login_post_data)
            ress2 = session.post(creatr_url, create_post_date)
            return ress2
        except BaseException as e:
            log1.error('接口访问失败',exc_info=1)
            raise
    def examine(self,examine_url,examine_date):
        '''审核产品函数'''
        try:
            session = requests.Session()
            host = "http://admin.tjs.net"
            login_url = "http://admin.tjs.net/login.html"
            login_post_data = {
                "phone": "15268299107",
                "password": "aa111111"
            }
            session.post(login_url, login_post_data)
            ress2 = session.post(examine_url, examine_date)
            print(ress2.content.decode('UTF-8'))
        except BaseException as e:
            log1.info('接口访问失败',exc_info=1)
    def Del(self,name):
        try:
            connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db='num_pro',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            sql = ("DELETE FROM n_product WHERE NAME = %s"%name)
            print (sql)
            cursor.execute(sql)
            connection.commit()
        except:
            print ("Error: fail")
    def update(self,name,DB):
        try:
            connection = pymysql.connect(host='192.168.113.116', port=3306, user='zjmax', password='zjmax.com', db=DB,charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            #随机生成一个产品名称
            num = '建设' + ''.join(str(random.choice(range(10))) for i in range(6))
            sql = ("update n_product set name = '{}' where name = '{}'".format(num,name))
            print (sql)
            cursor.execute(sql)
            connection.commit()
        except:
            print ("Error: fail")
    def kill_pids(self,name,count=None):
        '''杀进程函数
                name 进程名称
                count 无作用
                '''
        try:
            if name is None:
                return "参数不能为空"
            else:
                pids = psutil.pids()  # pids 列出所有进程号
                for pid in pids:  # 遍历进程号
                    p = psutil.Process(pid)  # 通过pid号实例进程为p以便调用
                    if p.name() == name:  # p.name()进程名称等于name时，执行cmd命令杀掉进程
                        print('pid-%s,pname-%s' % (p.pid, p.name()))
                        cmd = 'taskkill /F /IM {}'.format(name)
                        os.system(cmd)
                        print('杀第一次')
                        time.sleep(4)
                        cmd2 = 'taskkill /F /IM {}'.format(name)
                        os.system(cmd2)
                        print('杀第二次')
        except BaseException as e:
            log1.info('进程删除失败', exc_info=1)
if __name__ == "__main__":
    t = webrequests()
    a = int(1234567)
    for i in t.get_codeList(a):
        print(i)
