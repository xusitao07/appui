import time
import random
import unittest
from Logs.log import log1
from Common.Base_test import webrequests

class weather(unittest.TestCase):

    # def test_1_login(self):
    #     '''查询天气'''
    #     case_name = '登录云钱包'
    #     log1.info("执行测试用例：%s" % case_name)
    #     try:
    #         weather = webrequests()
    #         url = weather.confige_get('test','url',url='')
    #         payloda = {'city':'上海'}
    #         status_code,response_json =weather.get(url,params=payloda)
    #         message = weather.getdict(response_json,'message')
    #         test1 = self.assertEqual(status_code,403)
    #         test2 = self.assertEqual(message,'None')
    #         if test1 == None and test2 ==None:
    #             log1.info("测试通过")
    #     except BaseException as f :
    #         log1.error("测试用例执行出错: %s" % case_name,exc_info=1)
    #         raise

    def test_1_login100(self):
        '''登录钱包'''
        case_name = '登录云钱包'
        log1.info("执行测试用例：%s" % case_name)
        try:
            wr = webrequests()
            url = 'http://192.168.111.113:9060/app/100'
            data1 = wr.confige_items('login_data1')
            data2 = wr.confige_items('login_data2')
            data3 = wr.confige_items('login_data3')
            a = []
            a.append(data1)
            a.append(data2)
            a.append(data3)
            header = wr.confige_items('login_header')
            b,c = 0,0
            for i in a:
                status_code, response_json = wr.post(url,i,header)
                self.assertEqual(status_code,200)
                message = wr.getdict(response_json,'msg')
                if message == '成功':
                    print('登录测试成功')
                    log1.info("测试通过")
                elif message == '请输入正确的手机号' :

                    b +=1
                elif message == '请填写正确的密码':
                    c +=1

            print(b)
            self.assertEqual(b,1)#校验账号错误登录是否正常
            self.assertEqual(c,1)#校验密码错误登录是否正常
            log1.info("登录异常测试通过")

        except BaseException as f:
            log1.info("测试用例执行出错: %s" % case_name,exc_info=1)
            raise
    def test_2_register101(self):
        '''注册账号'''
        case_name = '注册账号'
        log1.info('执行测试用例：%s'% case_name)
        try:
            reg = webrequests
            mobile_num = reg.mobile_num(self)
            mobile_num2 = reg.mobile_num(self)
            url = 'http://192.168.111.113:9060/app/101'
            heade = reg.confige_items(self,'register_header')
            reg.config_write(self,'register_data', key='mobile', value=mobile_num)
            reg.config_write(self,'register_data2', key='mobile', value=mobile_num2)
            reg.config_write(self, 'register_data3', key='mobile', value='17612159836')
            data = reg.confige_items(self,'register_data')
            data2 = reg.confige_items(self,'register_data2')
            data3 = reg.confige_items(self, 'register_data3')
            a = []
            a.append(data)
            a.append(data2)
            a.append(data3)
            for i in a:
                status_code, response_json = reg.post(self,url,data=i, headers=heade)
                self.assertEqual(status_code, 200)
                message = reg.getdict(self,response_json,'msg')
                if message == '成功':
                    self.assertEqual(message, '成功')
                    log1.info("注册测试通过")
                elif message == '参数不能为空':
                    self.assertEqual(message, '参数不能为空')
                    log1.info("注册失败测试通过")
                elif message == '用户已存在':
                    self.assertEqual(message, '用户已存在')
                    log1.info("测试用户已存在通过")
                else:log1.info("请打开大ios手机钱包app解锁")
        except BaseException as f:
            log1.info("测试用例执行出错: %s" % case_name, exc_info=1)
            raise
    def test_3_logout102(self):
        '''退出登录'''
        case_name = '退出登录'
        log1.info('退出登录：%s'% case_name)
        try:
            logout = webrequests()
            url = 'http://192.168.111.113:9060/app/102'
            header = logout.confige_items('logout_header')
            data = logout.confige_items('logout_data')

            status_code, response_json = logout.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('接口响应通过%s' % status_code)
            if response_json is not None:
                result = self.assertEqual(logout.getdict(response_json, 'msg'), '成功')
                log1.info('退出成功')
            else:
                log1.info('接口未返回数据请查看服务是否正常')
        except BaseException as l:
            log1.info('测试用例执行出错：%s'%case_name,exc_info=1)
            raise
    def test_4_collectInformation103(self):
        '''收集用户信息'''
        case_name = '收集用户信息'
        try:
            col = webrequests()
            url = 'http://192.168.111.113:9060/app/103'
            header = col.confige_items('collectInformation_header')
            data= col.confige_items('collectInformation_data')
            print(data)
            status_code, response_json = col.post(url, data, header)
            self.assertEqual(status_code,200)
            log1.info('响应码校验通过')
            self.assertEqual(col.getdict(response_json,'msg'),'成功')
            log1.info('msg校验通过')
            response_value_key = ['mobile', 'register_time', 'safe_level', 'status_lock', 'status_sms', 'status_trade', 'uid']
            self.assertEqual(col.getdict_hopeval(response_json,'data'),response_value_key)#校验返回的字段是不是预期的字段
            log1.info('校验返回的字段是不是预期的字段通过')
        except BaseException as e:
            log1.info('测试用例执行出错：%s'%case_name,exc_info=1)
            raise
    def test_5_ResetTheTransactionPassword104(self):
        '''收集用户信息104'''
        case_name = '收集用户信息'
        try:
            data = []
            reset = webrequests()
            url = 'http://192.168.111.113:9060/app/104'
            for i in ['ResetTheTransactionPassword_data','ResetTheTransactionPassword_data2','ResetTheTransactionPassword_data3','ResetTheTransactionPassword_data4','ResetTheTransactionPassword_data5','ResetTheTransactionPassword_data6','ResetTheTransactionPassword_data7']:
                data.append(reset.confige_items(i))
            headers = reset.confige_items('ResetTheTransactionPassword_header')
            a,b,c,d,e,f = 0,0,0,0,0,0
            for j in data:
                status_code, response_json = reset.post(url, j, headers)
                self.assertEqual(status_code, 200)
                log1.info('获取信息接口响应正常')
                messg = reset.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1#'成功'次数计数
                    re = reset.getdict_hopeval(response_json,'data')
                    self.assertEqual(re[0],'res')
                    log1.info('校验响应data数据的位数是否正确')
                elif messg == '参数不能为空':
                    b +=1#'参数不能为空'次数计数
                elif messg == '用户不存在':
                    c += 1#'用户不存在'次数计数
                elif messg == '两次密码输入不一致':
                    d += 1#'两次密码输入不一致'次数计数
                elif messg == '密码只能是数字':
                    e += 1#'密码只能是数字'次数计数
                elif messg == '密码长度为6':
                    f += 1#'密码长度为6'次数计数
                else:
                    log1.info('请查看服务是否响应')
            self.assertEqual(a,1)
            log1.info('参数校验msg=成功1次通过')
            self.assertEqual(b,2)
            log1.info('参数校验msg=参数不能为空2次通过')
            self.assertEqual(c,1)
            log1.info('参数校验msg=用户不存在1次通过')
            self.assertEqual(d,1)
            log1.info('参数校验msg=两次密码输入不一致1次通过')
            self.assertEqual(f, 1)
            log1.info('参数校验msg=密码长度为6 1次通过')
            self.assertEqual(e,1)
            log1.info('参数校验msg=密码只能是数字1次通过')

        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_6_ResetTheLoginPassword105(self):
        '''重置登录密码'''
        case_name = '重置登录密码'
        try:
            data = []
            reset = webrequests()
            url = 'http://192.168.111.113:9060/app/105'
            for i in ['ResetTheLoginPassword_data','ResetTheLoginPassword_data2','ResetTheLoginPassword_data3','ResetTheLoginPassword_data4','ResetTheLoginPassword_data5','ResetTheLoginPassword_data6','ResetTheLoginPassword_data7']:
                data.append(reset.confige_items(i))
            headers = reset.confige_items('ResetTheLoginPassword_header')
            a,b,c,d = 0,0,0,0
            for j in data:
                status_code, response_json = reset.post(url, j, headers)
                self.assertEqual(status_code, 200)
                log1.info('获取信息接口响应正常')
                messg = reset.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1#'成功'次数计数
                    re = reset.getdict_hopeval(response_json,'data')
                    self.assertEqual(re[0],'res')
                    log1.info('校验响应data数据的位数是否正确')
                elif messg == '参数不能为空':
                    b +=1#'参数不能为空'次数计数
                elif messg == '请填写正确的密码':
                    c += 1#'请填写正确的密码'次数计数
                elif messg == '两次输入密码不一致':
                    d += 1#'两次密码输入不一致'次数计数
                else:
                    log1.info('请查看服务是否响应')
            self.assertEqual(a,1)
            log1.info('参数校验msg=成功1次通过')
            self.assertEqual(b,4)
            log1.info('参数校验msg=参数不能为空4次通过')
            self.assertEqual(c,1)
            log1.info('参数校验msg="请填写正确的密码"1次通过')
            self.assertEqual(d,1)
            log1.info('参数校验msg=两次密码输入不一致1次通过')

        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_7_CheckPassword107(self):
        '''校验密码107'''
        case_name = '校验密码'
        try:
            data = []
            reset = webrequests()
            url = 'http://192.168.111.113:9060/app/107'
            for i in ['CheckPassword_data','CheckPassword_data2','CheckPassword_data3','CheckPassword_data4','CheckPassword_data5','CheckPassword_data6']:
                data.append(reset.confige_items(i))
            headers = reset.confige_items('CheckPassword_header')
            a,b,c,d,e = 0,0,0,0,0
            for j in data:
                status_code, response_json = reset.post(url, j, headers)
                self.assertEqual(status_code, 200)
                log1.info('获取信息接口响应正常')
                messg = reset.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1#'成功'次数计数
                    re = reset.getdict_hopeval(response_json,'data')
                    self.assertEqual(re[0],'res')
                    log1.info('校验响应data数据的位数是否正确')
                elif messg == '参数不能为空':
                    b +=1#'参数不能为空'次数计数
                elif messg == '密码不正确':
                    c += 1#'密码不正确'次数计数
                elif messg == '账号还没有登录':
                    d += 1#'账号还没有登录'次数计数
                elif messg == '系统繁忙，请稍后再试':
                    e += 1  # '系统繁忙，请稍后再试'次数计数
                else:
                    log1.info('请查看服务是否响应')
            self.assertEqual(a,1)
            log1.info('参数校验msg=成功1次通过')
            self.assertEqual(b,2)
            log1.info('参数校验msg=参数不能为空2次通过')
            self.assertEqual(c,1)
            log1.info('参数校验msg="密码不正确"1次通过')
            self.assertEqual(d,1)
            log1.info('参数校验msg="账号还没有登录"1次通过')
            self.assertEqual(e, 1)
            log1.info('参数校验msg="系统繁忙，请稍后再试"1次通过')
        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    @staticmethod
    def get_code(self,domain):
        '''获取验证码，用途域：register注册|login登录|login_pass重置登录密码|
        pay_pass重置支付密码|lock_pass重置应用锁密码|
        payment确认转账|valid开启短信验证'''
        try:
            code = webrequests()
            url = 'http://192.168.111.113:9060/app/401'
            data = {'local': '1', 'domain': domain, 'is_voice': '0', 'user_id': '1b13efa1-14d5-430b-95e0-65d512ff5419',
                    'source': 'coinpay'}
            haders = {
                'User-Agent': 'ios_Simulator;11.4;6BC7AA24-D8D5-4BA7-92BA-B3740ECDCFB2;10010_v1_401;b22d502937bbdf4bdbb20a707765498a'}
            status_code, response_json = code.post(url,data,haders)  # 通过接口发送验证码
            self.assertEqual(status_code, 200)
            self.assertEqual(code.getdict(response_json, 'msg'), '成功')
            time.sleep(2)
            return code.get_identifying_code(
                'SELECT CODE FROM n_valid a ORDER BY a.add_time DESC LIMIT 1', 'CODE',
                'num_sms')
        except BaseException as e:
            log1.info('验证码获取异常',e)
            raise
    def test_7_swithMessage108(self):
        '''切换短信验证开关'''
        case_name = '切换短信验证开关'
        try:
            swith = webrequests()
            data = []
            url = 'http://192.168.111.113:9060/app/108'
            code = weather.get_code(self,'valid')
            swith.config_write('swithMessage_data',key='sms_code',value=code)
            for i in ['swithMessage_data', 'swithMessage_data2']:
                data.append(swith.confige_items(i))
            headers = swith.confige_items('swithMessage_header')
            a = 0
            for j in data:
                status_code, response_json = swith.post(url, j, headers)
                self.assertEqual(status_code, 200)
                log1.info('获取信息接口响应正常')
                messg = swith.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1  # '成功'次数计数
                    re = swith.getdict_hopeval(response_json, 'data')
                    self.assertEqual(re[0], 'res')
                    log1.info('校验响应data数据的位数是否正确')
                else:
                    log1.info('请查看服务是否响应')
            self.assertEqual(a, 2)
            log1.info('参数校验msg=成功1次通过')
        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_7_GetAddressBook109(self):
        '''获取用户地址簿'''
        case_name = '获取用户地址簿'
        try:
            Address = webrequests()
            data = []
            url = 'http://192.168.111.113:9060/app/109'
            data = Address.confige_items('GetAddressBook_data')
            headers = Address.confige_items('GetAddressBook_header')
            status_code, response_json = Address.post(url, data, headers)
            self.assertEqual(status_code, 200)
            log1.info('获取信息接口响应正常')
            messg = Address.getdict(response_json, 'msg')
            self.assertEqual(messg,'成功')
            list1 = Address.getdict(response_json, 'list')
            expected = ['address','alias','coin_code','coin_icon','coin_id','id'] #期望值
            Actual = [] # 实际值
            #遍历出list1中的key校验地址字段是否正确
            for k,v in list1[0].items():
                if k is not None:
                    Actual.append(k)
                else:
                    log1.info('list1中没有返回值')
            self.assertEqual(Actual,expected)
            log1.info('校验地址字段期望值和实际值相等测试通过')
        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_8_AddAddress110(self):
        '''新增用户地址'''
        case_name = '新增用户地址'
        try:
            list = []
            addaddress = webrequests()

            ADDRESS = addaddress.get_identifying_code2('SELECT address FROM `xl_user_coin_account` WHERE coin_code = "DASH"','address','w_user')
            for i in ADDRESS: #取出列表ADDRESS中嵌套字典的vale并存放在lis里面
                for k, v in i.items():
                    if k is not None:
                        if v != '':  #去除列表的空元素
                            list.append(v)
            address = random.choice(list) # 从lis中随机取一个地址
            addaddress.config_write('AddAddress_data','address',address)#将生成的地址写入测试参数中
            url = 'http://192.168.111.113:9060/app/110'
            header = addaddress.confige_items('AddAddress_header')
            data = []
            for i in ['AddAddress_data','AddAddress_data2','AddAddress_data3','AddAddress_data4','AddAddress_data5']:
                data.append(addaddress.confige_items(i))
            a,b,c = 0,0,0
            for i in data: #用data中的数据发送请求
                status_code, response_json = addaddress.post(url, i, header)
                self.assertEqual(status_code,200)
                log1.info('code响应正常')
                messg = addaddress.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1  # '成功'次数计数
                    res = addaddress.getdict_hopeval(response_json,'data')
                    self.assertEqual(res[0],'address_id')
                    log1.info('返回data中的第一位数据符合期望')
                    log1.info('计数1次通过')
                elif messg == '参数不能为空':
                    b += 1
                    self.assertEqual(messg,'参数不能为空')
                    log1.info('计数3次通过')
                elif messg == '请先登录':
                    c += 1
                    self.assertEqual(messg, '请先登录')
                    log1.info('计数1次通过')
                else:log1.info('请检接口是否正常')
            self.assertEqual(a,1)
            log1.info('a计数1次通过')
            self.assertEqual(b,3)
            log1.info('b计数3次通过')
            self.assertEqual(c,1)
            log1.info('c计数1次通过')
        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_9_DeleteAddress111(self):
        '''删除用户地址'''
        case_name = '删除用户地址'

        try:
            deleteAddress = webrequests()
            url = 'http://192.168.111.113:9060/app/111'
            header = deleteAddress.confige_items('DeleteAddress_header')
            data = []
            for i in ['DeleteAddress_data','DeleteAddress_data2']:
                data.append(deleteAddress.confige_items(i))
            for j in data:
                status_code, response_json = deleteAddress.post(url, j, header)
                self.assertEqual(status_code,200)
                log1.info('code响应正常')
                messg = deleteAddress.getdict(response_json,'msg')
                if messg == '成功':
                    self.assertEqual(messg, '成功')
                    log1.info('成功测试正常')
                    re = deleteAddress.getdict_hopeval_value(response_json,'data')
                    self.assertEqual(re[0],'success')
                    log1.info('success测试正常')
                elif messg == '参数不能为空':
                    self.assertEqual(messg, '参数不能为空')
                    log1.info('参数不能为空测试正常')
                else: log1.info('成功和参数不能为空的校验失败，请检查接口是否正常。。。。')
        except BaseException as e :
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_10_GetAccountInformation150(self):
        '''获取账户信息'''
        case_name = '获取账户信息'

        try:
            Information = webrequests()
            url = 'http://192.168.111.113:9060/app/150'
            header = Information.confige_items('GetAccountInformation_header')
            data = Information.confige_items('GetAccountInformation_data')
            status_code, response_json = Information.post(url,data,header)
            self.assertEqual(status_code,200)
            log1.info('响应码正常')
            messg = Information.getdict(response_json,'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg打印成功')
                list1 = Information.getdict(response_json,'coin_list')
                self.assertEqual(len(list1), 3)
                log1.info('coin_list返回3条数据')
                Expected = []
                for k,v in list1[0].items():#获取嵌套字典的key作为期望值
                    if k is not None:
                        Expected.append(k)
                Actual = ['account_id','coin_amount','coin_amount_trans','coin_code','coin_icon','coin_id']
                self.assertEqual(Expected,Actual)
                log1.info('coin_list返回字段正确')
            else:
                log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s'%case_name,exc_info=1)
            raise
    def test_11_ModifyCurrencyDisplay151(self):
        '''修改用户币种展示'''
        case_name = '修改用户币种展示'
        try:
            modify = webrequests()
            url = 'http://192.168.111.113:9060/app/151'
            data = modify.confige_items('ModifyCurrencyDisplay_data')
            header = modify.confige_items('ModifyCurrencyDisplay_header')
            status_code , response_json = modify.post(url,data,header)
            self.assertEqual(status_code,200)
            messg = modify.getdict(response_json,'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正常')
                res = modify.getdict(response_json,'res')
                self.assertEqual(res,'success')
                log1.info('res返回正常')
            else: log1.info('查看接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_12_GetWalletAssets152(self):
        '''获取钱包资产详情'''
        case_name = '修改用户币种展示'
        try:
            Assets = webrequests()
            url = 'http://192.168.111.113:9060/app/152'
            data = Assets.confige_items('GetWalletAssets_data')
            header = Assets.confige_items('GetWalletAssets_header')
            status_code , response_json = Assets.post(url,data,header)
            self.assertEqual(status_code,200)
            messg = Assets.getdict(response_json,'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正常')
                res = Assets.getdict(response_json,'data')
                #data数据返回的期望值
                DataExpected = ['balance','coin_code','coin_icon','coin_id','conversion','count','currency_code','list']
                # list数据返回的期望值
                ListExpected = ['address','amount','dateline','id','request_no','schedule','status','status_desc','type','type_desc']
                # data数据返回的实际值
                DataActual = []
                # List数据返回的实际值
                ListActual = []
                for k , v in res.items():
                    if k is not None:
                        DataActual.append(k)
                self.assertEqual(DataActual,DataExpected)
                log1.info('data数据返回的字段符合预期')
                lis = Assets.getdict(response_json,'list')
                self.assertEqual(len(lis),5)
                log1.info('list中返回的数据条数符合预期')
                for k2,v2 in lis[0].items():
                    if k2 is not None:
                        ListActual.append(k2)
                self.assertEqual(ListActual, ListExpected)
                log1.info('List数据返回的字段符合预期')
            else: log1.info('查看接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_13_GetTransactionRecords153(self):
        '''获取交易记录详情'''
        case_name = '获取交易记录详情'
        try:
            Transaction = webrequests()
            url = 'http://192.168.111.113:9060/app/153'
            data = Transaction.confige_items('GetTransactionRecords_data')
            header = Transaction.confige_items('GetTransactionRecords_header')
            status_code, response_json = Transaction.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = Transaction.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = Transaction.getdict(response_json,'data')
                Expected = {
                    "amount": "-0.01000000DASH",
                    "coin_code": "DASH",
                    "fee_amount": "0.00000000DASH",
                    "final_time": "2019-01-28 14:00:54",
                    "from_address": "ydwdcFELka3UZnX2LjWx8z3MyM4hfomK6K",
                    "remark": "红包发送支出",
                    "schedule": 0,
                    "to_address": "",
                    "tx_code": "",
                    "type": "11",
                    "type_desc": "转账"}#期望返回值
                self.assertEqual(data1,Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_14_TransferPage154(self):
        '''转账页面'''
        case_name = '转账页面'
        try:
            TransferPage = webrequests()
            url = 'http://192.168.111.113:9060/app/154'
            data = TransferPage.confige_items('TransferPage_data')
            header = TransferPage.confige_items('TransferPage_header')
            status_code, response_json = TransferPage.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = TransferPage.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = TransferPage.getdict(response_json,'data')
                Expected = {
                    "balance": "0.00000000",
                    "coin_code": "GTC",
                    "fee_code": "ETH",
                    "fee_double": 10000,
                    "fee_end": 10,
                    "fee_start": 2,
                    "nonce": ""}#期望返回值
                self.assertEqual(data1,Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_15_TransferAccounts156(self):
        '''转账'''
        case_name = '转账'
        try:
            Account = webrequests()
            url = 'http://192.168.111.113:9060/app/156'
            data = Account.confige_items('TransferAccounts_data')
            header = Account.confige_items('TransferAccounts_header')
            status_code , reponse_json = Account.post(url,data,header)
            self.assertEqual(status_code,200)
            log1.info('返回码正常')
            msg = Account.getdict(reponse_json,'msg')
            if msg is not None:
                self.assertEqual(msg,'成功')
                log1.info('msg返回成功')
                res = Account.getdict(reponse_json,'res')
                self.assertEqual(res,'success')
                log1.info('res返回正确')
            else: log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_16_TransferChecking155(self):
        '''转账检测'''
        case_name = '转账检测'
        try:
            Checking = webrequests()
            url = 'http://192.168.111.113:9060/app/155'
            data = Checking.confige_items('TransferChecking_data')
            header = Checking.confige_items('TransferChecking_header')
            status_code, reponse_json = Checking.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('返回码正常')
            msg = Checking.getdict(reponse_json, 'msg')
            if msg is not None:
                self.assertEqual(msg, '成功')
                log1.info('msg返回成功')
                res = Checking.getdict(reponse_json, 'need_sms')
                self.assertEqual(res, 0)
                log1.info('need_sms返回正确')
            else:
                log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_17_ScanningCode157(self):
        '''扫码付款'''
        case_name = '扫码付款'
        try:
            TransferPage = webrequests()
            url = 'http://192.168.111.113:9060/app/157'
            data = TransferPage.confige_items('ScanningCode_data')
            header = TransferPage.confige_items('ScanningCode_header')
            status_code, response_json = TransferPage.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = TransferPage.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = TransferPage.getdict(response_json,'data')
                Expected = {
                    "address": "0xf99812cd1d05d51e2febe11152c1e671214d3b27",
                    "amount": "0",
                    "coin_code": "SIPC",
                    "coin_id": "59738ebd-706f-4cbd-b4ab-deda04794f31",
                    "is_pay": 0,
                    "pay_info": {}
                }#期望返回值
                self.assertEqual(data1,Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_18_CollectionInterface158(self):
        '''收款界面'''
        case_name = '收款界面'
        try:
            Collection = webrequests()
            url = 'http://192.168.111.113:9060/app/158'
            data = Collection.confige_items('CollectionInterface_data')
            header = Collection.confige_items('CollectionInterface_header')
            status_code, response_json = Collection.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = Collection.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = Collection.getdict(response_json,'data')
                Expected = {
                    "address": "yVnFGcC94uGMvMxmT9FamgN2aV15ZNf977",
                    "qr_value": "DASH:yVnFGcC94uGMvMxmT9FamgN2aV15ZNf977"
                }#期望返回值
                self.assertEqual(data1,Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_19_GetBalance159(self):
        '''获取用户比账户余额'''
        case_name = '获取用户比账户余额'
        try:
            GetBalance = webrequests()
            url = 'http://192.168.111.113:9060/app/159'
            data = GetBalance.confige_items('GetBalance_data')
            header = GetBalance.confige_items('GetBalance_header')
            status_code, response_json = GetBalance.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = GetBalance.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = GetBalance.getdict(response_json,'data')
                Expected = {
                    "balance": "0.00000000",
                    "code": "ETH",
                }#期望返回值
                self.assertEqual(data1,Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_20_GetCurrencyList200(self):
        '''获取币种展示列表'''
        case_name = '获取币种展示列表'
        try:
            GetCurrencyList = webrequests()
            url = 'http://192.168.111.113:9060/app/200'
            data = GetCurrencyList.confige_items('GetCurrencyList_data')
            header = GetCurrencyList.confige_items('GetCurrencyList_header')
            status_code, response_json = GetCurrencyList.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = GetCurrencyList.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg,'成功')
                log1.info('msg返回正确')
                data1 = GetCurrencyList.getdict(response_json,'list')
                self.assertEqual(len(data1),3)
                log1.info('list返回的币种符合预期')
                Expected = {
                    "code": "BTC",
                    "code_name": "Bitcoin",
                    "icon": "https://tjsstatic.oss-cn-shanghai-finance-1-pub.aliyuncs.com/20180806103826159.png",
                    "id": "b3751ab2-64a1-4c30-b102-659adf001739",
                    "select": 1
                }#期望返回值
                self.assertEqual(data1[0],Expected)
                log1.info('data数据返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_21_CheckRatioAddress201(self):
        '''获取币种展示列表'''
        case_name = '获取币种展示列表'
        try:
            CheckRatioAddress = webrequests()
            url = 'http://192.168.111.113:9060/app/201'
            datalist =['CheckRatioAddress_data','CheckRatioAddress1_data','CheckRatioAddress2_data']
            header = CheckRatioAddress.confige_items('CheckRatioAddress_header')
            a,b,c, = 0,0,0
            for i in datalist:
                data = CheckRatioAddress.confige_items(i)
                status_code, response_json = CheckRatioAddress.post(url, data, header)
                self.assertEqual(status_code, 200)
                messg = CheckRatioAddress.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1
                    data1 = CheckRatioAddress.getdict(response_json, 'data')
                    Expected = {
                        "is_inner": 0
                    }  # 期望返回值   请输入转账地址
                    self.assertEqual(data1, Expected)
                    log1.info('data数据返回正确')
                elif messg == '请输入转账地址':
                    b += 1
                elif messg == '无效的地址格式':
                    c += 1
                else:log1.info('请重新检查测试数据。。。。。。。。')
            self.assertEqual(a,1)
            log1.info('msg返回正确')
            self.assertEqual(b,1)
            log1.info('请输入转账地址测试通过')
            self.assertEqual(c,1)
            log1.info('无效的地址格式测试通过')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_22_MarketList250(self):

        '''获取用户行情列表'''
        case_name = '获取用户行情列表'
        try:
            MarketList = webrequests()
            url = 'http://192.168.111.113:9060/app/250'
            data = MarketList.confige_items('MarketList_data')
            header = MarketList.confige_items('MarketList_header')
            status_code, response_json = MarketList.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = MarketList.getdict(response_json, 'msg')
            print('aaa',messg)
            if messg is not None:
                self.assertEqual(messg, '成功')
                log1.info('msg返回正确')
                datalist = MarketList.getdict(response_json, 'list')
                print(datalist)
                self.assertEqual(len(datalist), 3)
                log1.info('list返回的币种个数符合预期')
                Expected = ["coin_code",
                            "exchange_code",
                            "percent_change",
                            "price",
                            "price_change",
                            "price_sign",
                            "ticker_code",
                            "ticker_id",
                            "url"]
                  # 期望返回值
                Actual = []#实际返回值
                for k,v in datalist[0].items():
                    if k is not None:
                        Actual.append(k)
                self.assertEqual(Actual, Expected)
                log1.info('data数据返回key正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_23_TransactionPairList251(self):

        '''获取交易对列表'''
        case_name = '获取交易对列表'
        try:
            PairList = webrequests()
            url = 'http://192.168.111.113:9060/app/251'
            data = PairList.confige_items('PairList_data')
            header = PairList.confige_items('PairList_header')
            status_code, response_json = PairList.post(url, data, header)
            self.assertEqual(status_code, 200)
            messg = PairList.getdict(response_json, 'msg')
            if messg is not None:
                self.assertEqual(messg, '成功')
                log1.info('msg返回正确')
                datalist = PairList.getdict(response_json, 'list')
                self.assertEqual(len(datalist), 3)
                log1.info('list返回的币种个数符合预期')
                Expected = ["coin_code",
                            "collect",
                            "exchange_code",
                            "ticker_code",
                            "ticker_id"]
                  # 期望返回值
                Actual = []#实际返回值
                for k,v in datalist[0].items():
                    if k is not None:
                        Actual.append(k)
                self.assertEqual(Actual, Expected)
                log1.info('data数据返回key正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_24_Quotation252(self):

        '''收藏或取消行情'''
        case_name = '收藏或取消行情'
        try:
            Quotation = webrequests()
            url = 'http://192.168.111.113:9060/app/252'
            datalist = ['Quotation_data', 'Quotation1_data']
            header = Quotation.confige_items('Quotation_header')
            a = 0
            for i in datalist:
                data = Quotation.confige_items(i)
                status_code, response_json = Quotation.post(url, data, header)
                self.assertEqual(status_code, 200)
                messg = Quotation.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1
                    data1 = Quotation.getdict(response_json, 'data')
                    Expected = {
                        "res": "success"
                    }  # 期望返回值   请输入转账地址
                    self.assertEqual(data1, Expected)
                    log1.info('data数据返回正确')
            self.assertEqual(a, 2)
            log1.info('msg返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_25_QuotationSort253(self):

        '''用户行情排序'''
        case_name = '用户行情排序'
        try:
            QuotationSort = webrequests()
            url = 'http://192.168.111.113:9060/app/253'
            data = QuotationSort.confige_items('QuotationSort_data')
            header = QuotationSort.confige_items('QuotationSort_header')
            status_code, response_json = QuotationSort.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = QuotationSort.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = QuotationSort.getdict(response_json, 'data')
                Expected = {
                    "res": "success"
                }  # 期望返回值   请输入转账地址
                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_26_GetKeys400(self):

        '''获取公私钥'''
        case_name = '获取公私钥'
        try:
            GetKeys = webrequests()
            url = 'http://192.168.111.113:9060/app/400'
            data = GetKeys.confige_items('GetKeys_data')
            header = GetKeys.confige_items('GetKeys_header')
            status_code, response_json = GetKeys.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = GetKeys.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = GetKeys.getdict(response_json, 'data')
                Expected = [
                    "encrypt",
                    "is_lock",
                    "is_pay",
                    "k",
                    "uid"]
                 # 期望返回值   请输入转账地址
                expectedlist = []
                for k,v in data1.items():
                    expectedlist.append(k)
                self.assertEqual(expectedlist,Expected)
                log1.info('data数据返回正确')
            else:log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_27_CurrencyList404(self):

        '''获取计价货币列表'''
        case_name = '获取计价货币列表'
        try:
            CurrencyList = webrequests()
            url = 'http://192.168.111.113:9060/app/404'
            data = CurrencyList.confige_items('CurrencyList_data')
            header = CurrencyList.confige_items('CurrencyList_header')
            status_code, response_json = CurrencyList.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = CurrencyList.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = CurrencyList.getdict(response_json, 'list')
                Expected = [
                    {
                        "name": "人民币",
                        "select": 1,
                        "sign": "¥",
                        "value": "CNY"
                    },
                    {
                        "name": "美元",
                        "select": 0,
                        "sign": "$",
                        "value": "USD"
                    }
                ]  # 期望返回值   请输入转账地址
                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_28_ChangeCurrencyList405(self):

        '''切换当前计价方式'''
        case_name = '切换当前计价方式'
        try:
            ChangeCurrencyList = webrequests()
            url = 'http://192.168.111.113:9060/app/405'
            datalist = ['ChangeCurrencyList_data', 'ChangeCurrencyList2_data']
            header = ChangeCurrencyList.confige_items('ChangeCurrencyList_header')
            a = 0
            for i in datalist:
                data = ChangeCurrencyList.confige_items(i)
                status_code, response_json = ChangeCurrencyList.post(url, data, header)
                self.assertEqual(status_code, 200)
                messg = ChangeCurrencyList.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1
                    data1 = ChangeCurrencyList.getdict(response_json, 'data')
                    Expected = {
                        "res": "success"
                    }  # 期望返回值   请输入转账地址
                    self.assertEqual(data1, Expected)
                    log1.info('data数据返回正确')
            self.assertEqual(a, 2)
            log1.info('msg返回正确')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_29_GetH5Address406(self):

        '''获取计价货币列表'''
        case_name = '获取计价货币列表'
        try:
            GetH5Address = webrequests()
            url = 'http://192.168.111.113:9060/app/406'
            data = GetH5Address.confige_items('GetH5Address_data')
            header = GetH5Address.confige_items('GetH5Address_header')
            status_code, response_json = GetH5Address.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = GetH5Address.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = GetH5Address.getdict(response_json, 'data')
                Expected = {
                    "url": "http://wap.cp.com/invitelist?app=1"
                }  # 期望返回值   请输入转账地址
                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_30_RegisteredColdWallet500(self):

        '''获取计价货币列表'''
        case_name = '获取计价货币列表'
        try:
            RegisteredColdWallet = webrequests()
            url = 'http://192.168.111.113:9060/app/500'
            data = RegisteredColdWallet.confige_items('RegisteredColdWallet_data')
            header = RegisteredColdWallet.confige_items('RegisteredColdWallet_header')
            status_code, response_json = RegisteredColdWallet.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = RegisteredColdWallet.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = RegisteredColdWallet.getdict(response_json, 'data')
                Expected = {
                    "res": "success"
                }  # 期望返回值   请输入转账地址
                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_31_ImportcoldWallet501(self):

        '''导入冷钱包'''
        case_name = '导入冷钱包'
        try:
            ImportcoldWallet = webrequests()
            url = 'http://192.168.111.113:9060/app/501'
            data = ImportcoldWallet.confige_items('ImportcoldWallet_data')
            header = ImportcoldWallet.confige_items('ImportcoldWallet_header')
            status_code, response_json = ImportcoldWallet.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = ImportcoldWallet.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = ImportcoldWallet.getdict(response_json, 'data')
                Expected = {
                    "res": "success"
                }  # 期望返回值   请输入转账地址
                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_32_RedEnvelopes550(self):

        '''用户发送红包'''
        case_name = '用户发送红包'
        try:
            RedEnvelopes = webrequests()
            url = 'http://192.168.111.113:9060/app/550'
            datalist = ['RedEnvelopes_data','RedEnvelopes2_data']
            header = RedEnvelopes.confige_items('RedEnvelopes_header')
            a = 0
            for i in datalist:
                data = RedEnvelopes.confige_items(i)
                status_code, response_json = RedEnvelopes.post(url, data, header)
                self.assertEqual(status_code, 200)
                log1.info('响应码放返回正常')
                messg = RedEnvelopes.getdict(response_json, 'msg')
                if messg == '成功':
                    a +=1
                    data1 = RedEnvelopes.getdict(response_json, 'data')
                    Expected = [
                        "content",
                        "icon",
                        "red_id",
                        "title",
                        "url"
                    ]  # 期望返回值   请输入转账地址
                    data2 = []
                    for k,v in data1.items():
                        if k is not None:
                            data2.append(k)
                    self.assertEqual(data2, Expected)
                    log1.info('data数据返回正确')
                else:
                    log1.info('测试异常请检查数据')
            self.assertEqual(a,2)
            log1.info('两次发红包都正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_33_RedRecords551(self):

        '''红包记录'''
        case_name = '红包记录'
        try:
            RedRecords = webrequests()
            url = 'http://192.168.111.113:9060/app/551'
            header = RedRecords.confige_items('RedRecords_header')
            data = RedRecords.confige_items('RedRecords_data')
            status_code, response_json = RedRecords.post(url, data, header)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = RedRecords.getdict(response_json, 'msg')
            if messg == '成功':
                data1 = RedRecords.getdict(response_json, 'list')
                Expected = [
                    "amount",
                    "coin_code",
                    "coin_icon",
                    "dateline",
                    "grab_number",
                    "id",
                    "number",
                    "share",
                    "url"
                ]  # 期望返回值   请输入转账地址
                data2 = []
                for k, v in data1[0].items():
                    if k is not None:
                        data2.append(k)
                self.assertEqual(data2, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_34_MessageNotification(self):

        '''消息通知'''
        case_name = '消息通知'
        try:
            MessageNotification = webrequests()
            url = 'http://cpapp.kcmc.cc/api/msg?param=CCBw38ZKl546oLPdyp2FompLx7PeaA9kS73V6j91mm3kFxvCxCCkZZsMcayDWRWz4KO6DIDEd3Nh%0Agle0XHDCFQldWIt%2FLKtM2%2ByE5PwGIoqYUDtLF5ni5YVF0tzSvbtY2dhZxCKZz3yydUKt%2FPWu0Vn9%0A8TPcDAma1AL4OllIZGpmQvrhJDxsT2N9dq87rL3QD35btNI4txagwzklWdsIYDUVSD9GdBY7uWz1%0A3DE8%2B%2Fa274tKd7aapXUiHlKVxAoi5yUQC%2FP8%2B%2BjfAAd60rCB6Kl1JCQa0bbp7BMsMWAWb4cVP%2FUx%0AbCKqwf74gQF8IGE1bRfHjV6Zt28VzfNmbZFoeg%3D%3D%0A'
            status_code, response_json = MessageNotification.get(url)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = MessageNotification.getdict(response_json, 'msg')
            print(messg)
            if messg == '成功':
                data1 = MessageNotification.getdict(response_json, 'list')
                Expected = [
                    "content",
                    "dateline",
                    "id",
                    "status",
                    "title",
                    "type",
                    "type_desc"
                ]  # 期望返回值   请输入转账地址
                data2 = []
                for k, v in data1[0].items():
                    if k is not None:
                        data2.append(k)
                self.assertEqual(data2, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_35_ReadMessageNotification(self):

        '''消息点击阅读'''
        case_name = '消息点击阅读'
        try:
            ReadMessageNotification = webrequests()
            url = 'http://cpapp.kcmc.cc/api/msg_read?local=1&message_id=a4d7b3a7-ec87-4ac2-9e8e-81b3bd2c10ad'
            status_code, response_json = ReadMessageNotification.get(url)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = ReadMessageNotification.getdict(response_json, 'msg')
            print(messg)
            if messg == '成功':
                data1 = ReadMessageNotification.getdict(response_json, 'data')
                Expected = {
                    "count": "尊敬的客户，您的账户17612159836有一笔收款到账，收款总额为0.10000000SIPC。感谢您对我们的支持，我们将为您提供最诚挚的服务。"
                }  # 期望返回值   请输入转账地址

                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_36_SafetyGrade(self):

        '''安全等级'''
        case_name = '安全等级'
        try:
            SafetyGrade = webrequests()
            url = 'http://cpapp.kcmc.cc/api/safety?local=0&user_id=932fee22-5275-4d4e-938c-d7aeac55a737&param=ZrWDWYMp6NcaYq4jIHVAWFuXpBSl3mKnL%2BfRoj4yRiNF8URTN%2F9AzMbfml6ETFtRSmW6OcbFrKY%2F%0ALSY3Z6XDrJoa6wNqgLCzgO%2Ft6p7GsZLw4ASELCarN8oOzahaJtfS7pyRcjLTiBKyBFIZYj3lmfaD%0A%2FLS%2BfPfZi2e5C6VXnuI%3D%0A'
            status_code, response_json = SafetyGrade.get(url)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = SafetyGrade.getdict(response_json, 'msg')
            print(messg)
            if messg == '成功':
                data1 = SafetyGrade.getdict(response_json, 'data')
                Expected = {
                    "is_app_lock": 0,
                    "is_pay_pass": 0,
                    "is_sms_valid": 0,
                    "v1_day_amount": 0,
                    "v2_day_amount": 0
                }  # 期望返回值   请输入转账地址

                self.assertEqual(data1, Expected)
                log1.info('data数据返回正确')
            else:
                log1.info('测试异常请检查数据')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_37_ServiceAgreement(self):

        '''获取服务协议'''
        case_name = '获取服务协议'
        try:
            ServiceAgreement = webrequests()
            url = 'http://cpapp.kcmc.cc/api/protocol/?code=service&param=HC2l8tO%2B%2BnR8Ak0m00Y6MJOXAwiXXMcTrkiZTY0j6VUFqwnCVJuno193sbGDiHp7nJJlRycbl7EP%0AZQOFjxXVMbvv%2BCK1zOooklmfF%2FV0LnKutPgKfzWxvtxv1g3kMFCsyvpAN176OCwSQY94UkEDW2fv%0AJyyc55PbSbGMtMFM8oEemHntzbPpOq4ECk7fnSjKZqfSYGvOhBl%2BJ3zaEZa4p9tTqZ9RgPWy43rZ%0AD00O9UnL0ZnQ60oThGTCRItIP%2Bq2Ctdc91XZJEG25JKbJQb6qYFB5O0NRlkDpaN%2BixXBOqnx4IaV%0AOj1NWJhksNKOfiuBXC59l%2FQihDE3L8cemaMkwA%3D%3D%0A'
            status_code, response_json = ServiceAgreement.get(url)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = ServiceAgreement.getdict(response_json, 'msg')
            self.assertEqual(messg,'成功')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_38_MarketDetails(self):

        '''获取行情详情'''
        case_name = '获取行情详情'
        try:
            MarketDetails = webrequests()
            url = 'http://cpapp.kcmc.cc/api/ticker/?ticker_id=d9b876d3-1e09-49c5-8cde-e211ba602586&param=R%2FZfiW%2B8hSBgM9C%2Be24CH8q76AwBiwrWHFDxk0VfoFmXZPTDDYPk7npk4%2FY9Q2LoCL%2FeP0ZYiGyr%0A39MABv9%2FkvEipjv%2Bpd6%2BHjc%2B8sfqqAJYq2NXo28P68MO2u0a4Bsr3fhoK5GVcWLwM9PR5K4wT6Te%0AB6Qb%2B8YQ68gnB11oi4Y8yB%2BtcamznUTZkqdusHvMrCL8ZlWR21aK%2F6bNd1pRPkRMODa%2B1F3qNnOw%0A9q5lew20FcJoqTcIM9lWqILW3AT0QwDfXiDJAhCweXWIKwB7dBjAxAmzMoo%2BuWfRmH5o5yGfPdiA%0APzlpJmTCgoesTTe6FBc7P4C3XGM3ojoylyW3HQ%3D%3D%0A'
            status_code, response_json = MarketDetails.get(url)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = MarketDetails.getdict(response_json, 'msg')
            if messg == '成功':
                Expected = ['cny_price','coin_code','coin_desc','coin_icon','coin_name','global_list','percent','usd_price']
                Actul = []
                data = MarketDetails.getdict(response_json, 'data')
                for k,v in data.items() :
                    if k is not None:
                        Actul.append(k)
                self.assertEqual(Actul,Expected)
                log1.info('返回值正确')
            else:log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_39_HelpContent(self):

        '''获取帮助内容'''
        case_name = '获取帮助内容'
        try:
            HelpContent = webrequests()
            url = 'http://cpapp.kcmc.cc/api/help_view'
            Parma = {'local':1,'cat_id':'3e63a1ca-7e92-479f-8d7e-937da6e6d2f1'}
            status_code, response_json = HelpContent.get(url,Parma)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = HelpContent.getdict(response_json, 'msg')
            if messg == '成功':
                Expected = ['content','id','image','title']
                Actul = []
                data = HelpContent.getdict(response_json, 'list')
                for k,v in data[0].items() :
                    if k is not None:
                        Actul.append(k)
                self.assertEqual(Actul,Expected)
                log1.info('返回值正确')
            else:log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_40_RedPackets(self):

        '''获取红包详情'''
        case_name = '获取红包详情'
        try:
            RedPackets = webrequests()
            url = 'http://wap.cp.com/api/red_detail/'
            Parma = {'red_id':'0c51f4ca-ec29-41a0-8ec6-9b5777594813'}
            status_code, response_json = RedPackets.get(url,Parma)
            self.assertEqual(status_code, 200)
            log1.info('响应码放返回正常')
            messg = RedPackets.getdict(response_json, 'msg')
            if messg == '成功':
                Expected = ['amount','coin_code','grab_amount','grab_number','id','list','number','remark','user']
                Actul = []
                data = RedPackets.getdict(response_json, 'data')
                for k,v in data.items() :
                    if k is not None:
                        Actul.append(k)
                self.assertEqual(Actul,Expected)
                log1.info('返回值正确')
            else:log1.info('请检查接口是否正常')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise
    def test_41_HandRed(self):
        '''领红包'''
        case_name = '领红包'
        try:
            #发红包
            RedEnvelopes = webrequests()
            url = 'http://192.168.111.113:9060/app/550'
            datalist = ['RedEnvelopes_data', 'RedEnvelopes2_data']
            header = RedEnvelopes.confige_items('RedEnvelopes_header')
            red_id = []  # 返回的红包id
            for i in datalist:
                data = RedEnvelopes.confige_items(i)
                status_code, response_json = RedEnvelopes.post(url, data, header)
                self.assertEqual(status_code, 200)
                log1.info('响应码放返回正常')
                messg = RedEnvelopes.getdict(response_json, 'msg')
                if messg == '成功':
                    data1 = RedEnvelopes.getdict(response_json, 'data')
                    for k, v in data1.items():
                        if k == 'red_id':
                            red_id.append(v)
                    log1.info('data数据返回正确')
                else:
                    log1.info('测试异常请检查数据')
            print(red_id)

            #领红包
            HandRed = webrequests()
            url = 'http://wap.cp.com/api/red_grab/'
            a = 0
            for i in red_id:
                Parma = {'app': '1',
                         'red_id': i,
                         'from': 'singlemessage',
                         'isappinstalled': 0,
                         'mobile': '17612159836',
                         'coin_code': 'DASH', }
                status_code, response_json = HandRed.get(url, Parma)
                self.assertEqual(status_code, 200)
                log1.info('响应码放返回正常')
                messg = HandRed.getdict(response_json, 'msg')
                if messg == '成功':
                    a += 1
                    Expected = ['amount', 'amount_rmb', 'grab_user']
                    Actul = []
                    data = HandRed.getdict(response_json, 'data')
                    for k, v in data.items():
                        if k is not None:
                            Actul.append(k)
                    self.assertEqual(Actul, Expected)
                    log1.info('返回值正确')
                else:
                    log1.info('请检查接口是否正常')
            self.assertEqual(a,2)
            log1.info('两种红包都以领取')
        except BaseException as e:
            log1.info('用例执行失败：%s' % case_name, exc_info=1)
            raise












