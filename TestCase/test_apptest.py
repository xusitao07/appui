# coding=utf-8
from appium.webdriver.common.touch_action import TouchAction
from Logs.log import log1
from Common.Base_test import webrequests
import time
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re,random
from threading import Timer
class apptest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # desired_caps = {'platformName': 'Android', # 平台名称
        #                 # 'platformVersion': '6.0.1',  # 系统版本号
        #                 #'deviceName': '83c4caa7',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
        #                 #'platformVersion': '4.4.2',  # 系统版本号
        #                 #'deviceName': '127.0.0.1:62001',  #nox_adb.exe connect 127.0.0.1:62001 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
        #                 # 'platformVersion': '4.4.4',  # 系统版本号
        #                 # 'deviceName': '0acb291f',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
        #                 'platformVersion': '5.1.1',
        #                 'deviceName': 'Y9K0215204005433',
        #                 'appPackage': 'com.shuniuyun.tjs',  # apk的包名
        #                 'appActivity': 'com.shuniuyun.tjs.ui.main.activity.StartActivity',  # activity 名称
        #                 'automationName' : 'Uiautomator2',
        #                 'unicodeKeyboard': 'True',#使用unicode编码方式发送字符串
        #                 'resetKeyboard': 'True'#将键盘隐藏起来 http://127.0.0.1:4723/wd/hub
        #                 }
        webr = webrequests()
        name = 'find.exe'
        count = 2
        tim = Timer(7.0,webr.kill_pids,(name,count))# 启动程序7s后 查找进程find.exe并删除两次
        tim.start()#启动
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1.1",#5.1.1
            "deviceName": "127.0.0.1:21503",#Y9K0215204005433
            "appPackage": "com.shuniuyun.tjs",
            "appActivity": "com.shuniuyun.tjs.ui.main.activity.StartActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "automationName": "Uiautomator2",
            "chromeOptions": {"androidProcess" :"com.shuniuyun.tjs"}
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps) # 连接Appium
        time.sleep(5)
        TouchAction(self.driver).press(x=625, y=787).move_to(x=80, y=787).release().perform()  # 滑动启始页面
        time.sleep(3)
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_start").click()
    def setUp(self):
        '''登录操作'''
        time.sleep(10)
        self.driver.implicitly_wait("120")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login").click()
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_login_phone").send_keys("18770059999")
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login_ok").click()
        self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_pwd").send_keys("aa111111")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        try:
            self.assertTrue(self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_message").is_displayed())
        except Exception as error:
            raise
    # def tearDown(self):
    #     '''退出登录操作'''
    #     self.driver.find_element_by_xpath("android.widget.TextView[@text='账户']").click()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_personal_center").click()
    #     TouchAction(self.driver).press(x=541, y=1413).move_to(x=536, y=696).release().perform()
    #     self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_sign_out").click()
    # @classmethod
    # def tearDownClass(self):
    #      time.sleep(5)
    #      self.driver.quit()

    # def test_1_longin(self):
    #     """使用验证码登录"""
    #     case_name = '使用验证码登录'
    #     try:
    #         self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
    #         # self.driver.find_element_by_id("com.shuniuyun.tjs:id/fixed_bottom_navigation_title").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_login_phone").send_keys("18770059999")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_login_ok").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_code").click()  # 发送验证码
    #         time.sleep(3)
    #         tool = webrequests()  # 非静态方法使用需要实例化
    #         code = tool.get_identifying_code("SELECT code FROM n_valid a ORDER BY a.add_time DESC LIMIT 1", "code",
    #                                          "num_sms")  # 获取登录验证码
    #         codelist = tool.get_codeList(code)
    #         # 输入验证码模拟键盘输入
    #         for i in codelist:
    #             print(i)
    #             if i == 0:
    #                 self.driver.press_keycode(7)
    #             else:
    #                 self.driver.press_keycode(i + 7)
    #             time.sleep(1)
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_next").click()
    #         try:
    #             self.assertTrue(self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_message").is_displayed())
    #         except Exception as error:
    #             print(u'断言未通过：%s' % error)
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_personal_center").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_sign_out").click()
    #     except BaseException as e:
    #         log1.info("测试用例执行出错: %s" % case_name,exc_info=1)
    #         raise
    def get_toast(self,text,timeout=30,poll_frequency=0.5):
        """
        driver - 传driver,
        text   - 页面上看到的文本内容
        timeout - 最大超时时间，默认30s
        poll_frequency  - 间隔查询时间，默认0.5s查询一次"""
        toast_loc = (By.XPATH, ".//*[contains(@text,'{}')]".format(text))#{}.format(text)等同于%s,%text
        elm = WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_loc))
        print(elm.text)
        return  elm.text
    def switch_webview (self):
        """
        功能：hybrid 混合型APP 在native和webview之间切换
             切换当前driver为所填的contexts  “webview_name”
        driver  驱动
        context_name  需要切换的webview或native名称
         """
        # con2 = self.driver.contexts
        # print("所有contexts{}".format(con2))
        try:
            self.driver.switch_to.context('WEBVIEW_com.shuniuyun.tjs')
            time.sleep(4)
            con = self.driver.current_context
            print("已切到：{}".format(con))
        except BaseException as e:
            log1.info("切换WEBVIEW失败")
            raise
    def switch_native (self):
        """
        功能：hybrid 混合型APP 在native和webview之间切换
             切换当前driver为所填的contexts  “webview_name”
        driver  驱动
        context_name  需要切换的webview或native名称
         """
        # con = self.driver.current_context
        # print("当前contexts：{}".format(con))
        try:
            self.driver.switch_to.context('NATIVE_APP')
            time.sleep(4)
            con2 = self.driver.current_context
            print("已切到：{}".format(con2))
        except BaseException as e:
            log1.info("切换native失败")
            raise
    def creadeNonCollectionpro(self):
        '''创建非募集产品'''
        tool = webrequests()
        ceradeurl = tool.confige_get('craderurl', 'url',url='')
        creadebody = tool.confige_items('creaderbody')
        resut = tool.CreatProduct(ceradeurl, creadebody)
        print(resut)
        time.sleep(6)
    def creadeCollectionpro(self):
        '''创建募集产品'''
        tool = webrequests()
        ceradeurl = str(tool.confige_get('craderurl', 'url'))
        creadebody = tool.confige_items('creaderbody2')
        tool.CreatProduct(ceradeurl, creadebody)
        time.sleep(6)
    def creadeCollectionpro_weibao(self):
        '''创建募集尾包产品'''
        tool = webrequests()
        ceradeurl = tool.confige_get('craderurl', 'url')
        creadebody = tool.confige_items('creaderbody3')
        tool.CreatProduct(ceradeurl, creadebody)
        time.sleep(6)
    def examine(self,sql):
        '''审核'''
        tool = webrequests()
        examineUrl = tool.confige_get('examinUrl', 'url',url='')
        prductID = str(tool.get_identifying_code(sql, "id", "num_pro"))
        tool.config_write('examinPostDate', 'product_id', prductID)  # 写入数据库中的product_id
        time.sleep(3)
        examineData = tool.confige_items('examinPostDate')
        print(examineData)
        tool.examine(examineUrl, examineData)
        time.sleep(5)
    def establish(self,sql):
        '''成标'''
        tool = webrequests()
        establishUrl = tool.confige_get('establishUrl', 'url',url='')
        prductID = str(tool.get_identifying_code(sql, "id", "num_pro"))
        tool.config_write('establishPostDate', 'id', prductID)  # 写入产品id参数
        time.sleep(3)
        establishData = tool.confige_items('establishPostDate')
        tool.examine(establishUrl, establishData)
        time.sleep(5)
    # def test_2_BuyProFeimuji(self):
    #     """"购买非募集产品"""
    #     #后台发布测试产品
    #     case_name = '购买非募集产品'
    #     try:
    #         tool = webrequests()
    #         #创建非募集产品
    #         self.creadeNonCollectionpro()
    #         log1.info('产品创建成功')
    #         time.sleep(7)
    #         # 审核
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.examine(sql)
    #         log1.info('产品审核成功')
    #         time.sleep(5)
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'理财')]").click()
    #         text = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").get_attribute("text")
    #         self.assertEqual(text, "app")
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").click()
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").get_attribute("text"),"我要投资")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").click()  # 点击投资按钮跳转购买页面
    #         # 校验起投金额是不是正确
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").get_attribute("text"),"100001元起投,1元递增")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("100000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         # 断言toast
    #         toast_loc = (By.XPATH, ".//*[contains(@text,'小于产品最低购买金额')]")
    #         elm = WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_loc))
    #         print('toast...:',elm.text)
    #         self.assertEqual(elm.text, '小于产品最低购买金额')  # 购买金额小于剩余额度
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").clear()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("5000000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         toast = self.get_toast('超过产品最大购买金额')
    #         self.assertEqual(toast,'超过产品最大购买金额')  # 购买金额大于剩余额度
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").clear()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("500000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         # 校验跳转是否成功
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),"投标")
    #         time.sleep(4)
    #         #切换webview contexts
    #         self.switch_webview()
    #         text = self.driver.find_element_by_xpath("/html/body/section[1]/div[6]/span[2]").text
    #         self.assertEqual(text,'500000.00元')
    #         self.driver.find_element_by_id("password").send_keys("aa111111")
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         self.driver.find_element_by_id("title_content").is_displayed()  # 校验购买成功
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         time.sleep(4)
    #         # 切回native contexts
    #         self.switch_native()
    #
    #         # 成标
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.establish(sql)
    #         log1.info('产品成标成功')
    #         time.sleep(4)
    #         # 删除产品
    #         tool.Del("'app'")
    #         log1.info('产品删除成功')
    #     except BaseException as e:
    #         log1.info("测试用例执行出错: %s" % case_name, exc_info=1)
    #         raise
    #
    #     #成标后续可以接入还款的测试脚本
    # def test_3_BuyPromuji(self):
    #     """"购买募集产品"""
    #     #后台发布测试产品
    #     case_name = '购买募集产品'
    #     try:
    #         tool = webrequests()
    #         #创建非募集产品
    #         self.creadeCollectionpro()
    #         log1.info('产品创建成功')
    #         ## 审核
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.examine(sql)
    #         log1.info('产品审核成功')
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'理财')]").click()
    #         text = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").get_attribute("text")
    #         self.assertEqual(text, "app")
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").click()
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").get_attribute("text"),"我要认购")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").click()  # 点击投资按钮跳转购买页面
    #         # 校验起投金额是不是正确
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").get_attribute("text"),"100001元起投,1元递增")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("100000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         # 断言toast
    #         toast_loc = (By.XPATH, ".//*[contains(@text,'小于产品最低购买金额')]")
    #         elm = WebDriverWait(self.driver, 10,0.01).until(EC.presence_of_element_located(toast_loc))
    #         print('toast...:',elm.text)
    #         self.assertEqual(elm.text, '小于产品最低购买金额')  # 购买金额小于剩余额度
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").clear()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("5000000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         toast = self.get_toast('超过产品最大购买金额')
    #         self.assertEqual(toast,'超过产品最大购买金额')  # 购买金额大于剩余额度
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").clear()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").send_keys("500000")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         # 校验跳转是否成功
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),"投标")
    #         time.sleep(4)
    #         #切换webview contexts
    #         self.switch_webview()
    #         time.sleep(4)
    #         text = self.driver.find_element_by_xpath("/html/body/section[1]/div[6]/span[2]").text
    #         self.assertEqual(text,'500000.00元')
    #         self.driver.find_element_by_id("password").send_keys("aa111111")
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         self.driver.find_element_by_id("title_content").is_displayed()  # 校验购买成功
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         time.sleep(4)
    #         # 切回native contexts
    #         self.switch_native()
    #         # 成标
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.establish(sql)
    #         log1.info('产品成标成功')
    #         time.sleep(4)
    #         # 删除产品
    #         tool.Del("'app'")
    #         log1.info('产品删除成功')
    #     except BaseException as e:
    #         log1.info("测试用例执行出错: %s" % case_name, exc_info=1)
    #         raise
    # def test_4_BuyPro_weibao(self):
    #     """"购买非募集产品"""
    #     #后台发布测试产品
    #     case_name = '购买非募集产品'
    #     try:
    #         tool = webrequests()
    #         #创建非募集产品
    #         self.creadeCollectionpro_weibao()
    #         log1.info('产品创建成功')
    #         time.sleep(7)
    #         # 审核
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.examine(sql)
    #         log1.info('产品审核成功')
    #         time.sleep(5)
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'理财')]").click()
    #         text = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").get_attribute("text")
    #         self.assertEqual(text, "app")
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'app')]").click()
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").get_attribute("text"),"我要认购")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_product_statue").click()  # 点击投资按钮跳转购买页面
    #         # 校验起投金额是不是正确
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/et_buy_money").get_attribute("text"),"50000.00")
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_buy").click()
    #         # 校验跳转是否成功
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),"投标")
    #         time.sleep(4)
    #         #切换webview contexts
    #         self.switch_webview()
    #         time.sleep(4)
    #         text = self.driver.find_element_by_xpath("/html/body/section[1]/div[6]/span[2]").text
    #         self.assertEqual(text,'50000.00元')
    #         self.driver.find_element_by_id("password").send_keys("aa111111")
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         self.driver.find_element_by_id("title_content").is_displayed()  # 校验购买成功
    #         self.driver.find_element_by_id("acceptBtn").click()
    #         time.sleep(4)
    #         # 切回native contexts
    #         self.switch_native()
    #
    #         # 成标
    #         sql = str("SELECT id FROM n_product WHERE NAME ='app'")
    #         self.establish(sql)
    #         log1.info('产品成标成功')
    #         time.sleep(4)
    #         # 删除产品
    #         tool.Del("'app'")
    #         log1.info('产品删除成功')
    #     except BaseException as e:
    #         log1.info("测试用例执行出错: %s" % case_name, exc_info=1)
    #         raise
    # def test_5_withdraw(self):
    #     '''提现(执行用例之前先确保提现手续费为2元)'''
    #     case_name = "提现"
    #     try:
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'账户')]").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_assets_eye").click()
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_withdraw").click()
    #         #查看跳转页面是否正确
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),"提现")
    #         #获取可提现余额
    #         text = str(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").get_attribute("text"))
    #         bla = re.search('(\d+\.\d+)',text)#匹配text中显示的账户余额
    #         blance = float(bla.group())
    #         print(blance)
    #
    #         #校验全部按钮使用是否正常
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_all").click()
    #         self.assertEqual(float(self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").get_attribute("text")),blance)
    #         self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").clear()
    #         time.sleep(3)
    #         #随机获取一个3位数的正常提现金额
    #         num = int(''.join(str(random.choice(range(10))) for i in range(3)))
    #         print('提现金额：',num)
    #         #校验提现
    #         testlist = [0,blance,blance+1,num]
    #         for i in testlist:
    #             if i == 0:
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(i)
    #                 log1.info("i == 0通过")
    #                 #校验按钮是否可点击，返回false状态正常
    #                 self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_withdraw").get_attribute("long-clickable"),"false")
    #             elif i > blance:
    #                 k = int(i)
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").clear()
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(k)
    #                 # 校验按钮是否可点击，返回false状态正常
    #                 self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_withdraw").get_attribute(
    #                     "long-clickable"), "false")
    #                 log1.info("i > blance通过")
    #             elif i == blance:
    #                 j = int(i)
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").clear()
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(j)
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_withdraw").click()
    #                 # 校验有手续费的情况下全额提示toast提示是否正常，返回false状态正常
    #                 toa = self.get_toast("可提现余额应减去手续费")
    #                 self.assertEqual(toa,"可提现余额应减去手续费")
    #                 log1.info("i == blance通过")
    #             elif i == num:
    #                 # 提现正常校验资金记录和用户余额显示是否正常
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").clear()
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(i)
    #                 self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_withdraw").click()
    #                 self.switch_webview()
    #                 #校验页面跳转正确
    #                 self.driver.find_element_by_xpath("/html/body/section[1]/div[1]/span[2]").is_displayed()
    #                 #校验手续费和扣除的金额是否正确
    #                 desc = float(self.driver.find_element_by_xpath("//*[@id='form']/div[4]/input").get_attribute("value"))
    #                 print("desc",desc)
    #                 self.driver.find_element_by_id("password").send_keys("aa111111")
    #                 self.driver.find_element_by_id("acceptBtn").click()
    #                 self.driver.find_element_by_id("acceptBtn").click()
    #                 self.switch_native()
    #                 self.driver.find_element_by_xpath("//android.widget.TextView[@text='首页']").click()
    #                 self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
    #                 #获取扣除提现金额后的账户余额
    #                 tex = float(self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").get_attribute("text"))
    #                 self.assertEqual(blance-tex,desc)#计算提现前账户余额（blance）减掉提现后账户余额（tex）是否等于提现实扣金额（desc）
    #                 #校验资金明细里面显示是否正确
    #                 log1.info("i == num通过")
    #             else:print('异常情况')
    #         self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资金明细')]").click()
    #         # 校验跳转页面
    #         self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),
    #                          '资金明细')
    #         # 获取资金记录并校验
    #         time.sleep(5)
    #         te = self.driver.find_element_by_accessibility_id("-{}.00元(手续费2.00元)".format(num+2)).get_attribute("content-desc")
    #         tes = float(re.search("(\d+\.\d+)",te).group())
    #         print("tes:",tes)
    #         self.assertEqual(tes,desc)#资金明细中校验记录金额（tes）是否和提现金额（desc）一致
    #         # self.assertEqual(desc,te)
    #         self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
    #         log1.info("提现资金记录校验通过")
    #     except BaseException as e:
    #         log1.info("测试用例执行出错：%s"%case_name,exc_info=1)
    #         raise

    def test_6_Recharge(self):
        '''充值'''
        case_name = "充值"
        try:
            monneylist = [0,0.01,100]#充值测试数据
            for i in monneylist:
                if i == 0:
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_assets_eye").click()  # 调试用跑用例时注释
                    # 校验跳转页面
                    self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").text, "充值")
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(i)
                    #输入为0时校验按钮是否置灰
                    self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_recharge").get_attribute("long-clickable"),"false")
                    self.driver.find_element_by_accessibility_id("转到上一层级").click()

                elif i == 0.01:
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_assets_eye").click()  # 调试用跑用例时注释
                    # 获取未充值前的账户余额用来做校验
                    AccountBalance = float(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").text)
                    # 校验跳转页面
                    self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").text, "充值")
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(i)
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_recharge").click()
                    # 校验跳转页面
                    self.assertEqual(self.driver.find_element_by_xpath("/html/body/section[1]/div[3]/span[2]").text,
                                     "快捷充值")
                    self.assertEqual(self.driver.find_element_by_xpath("//*[@id='form']/div[2]/span[2]").text,
                                     "{}元".format(i))
                    self.driver.find_element_by_id("vcode").send_keys("111111")
                    self.driver.find_element_by_id("butSend").click()
                    self.assertEqual(self.get_toast("短信验证码发送成功"), "短信验证码发送成功")
                    self.driver.find_element_by_id("acceptBtn").click()
                    time.sleep(3)
                    self.driver.find_element_by_id("acceptBtn").click()
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='首页']").click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
                    #获取充值后的账户余额
                    RechargeAccountBalance = float(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").text)
                    #校验账户余额金额增加是否正确
                    self.assertEqual(AccountBalance-RechargeAccountBalance,float(i))
                    #校验资金明细记录
                    self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资金明细')]").click()
                    # 校验跳转页面
                    self.assertEqual(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),
                        '资金明细')
                    # 获取资金记录并校验
                    time.sleep(5)
                    te = self.driver.find_element_by_xpath("//android.view.View[@content-desc='{}元'and@index='6']".format(i)).get_attribute("content-desc")
                    tes = float(re.search("(\d+\.\d+)", te).group())
                    print("tes:", tes)
                    self.assertEqual(tes, i)  # 资金明细中校验记录金额（tes）是否和提现金额（desc）一致
                    self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
                    log1.info("提现资金记录校验通过")
                elif i == 100:
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/iv_assets_eye").click()  # 调试用跑用例时注释
                    # 获取未充值前的账户余额用来做校验
                    AccountBalance = float(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").text)
                    # 校验跳转页面
                    self.assertEqual(self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").text, "充值")
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/clearEditText").send_keys(i)
                    self.driver.find_element_by_id("com.shuniuyun.tjs:id/btn_recharge").click()
                    # 校验跳转页面
                    self.assertEqual(self.driver.find_element_by_xpath("/html/body/section[1]/div[3]/span[2]").text,
                                     "快捷充值")
                    self.assertEqual(self.driver.find_element_by_xpath("//*[@id='form']/div[2]/span[2]").text,
                                     "{}元".format(i))
                    self.driver.find_element_by_id("vcode").send_keys("111111")
                    self.driver.find_element_by_id("butSend").click()
                    self.assertEqual(self.get_toast("短信验证码发送成功"), "短信验证码发送成功")
                    self.driver.find_element_by_id("acceptBtn").click()
                    time.sleep(3)
                    self.driver.find_element_by_id("acceptBtn").click()
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='首页']").click()
                    time.sleep(3)
                    self.driver.find_element_by_xpath("//android.widget.TextView[@text='账户']").click()
                    # 获取充值后的账户余额
                    RechargeAccountBalance = float(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/tv_available_balance").text)
                    # 校验账户余额金额增加是否正确
                    self.assertEqual(AccountBalance - RechargeAccountBalance, i)
                    # 校验资金明细记录
                    self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'资金明细')]").click()
                    # 校验跳转页面
                    self.assertEqual(
                        self.driver.find_element_by_id("com.shuniuyun.tjs:id/toolbar_title").get_attribute("text"),
                        '资金明细')
                    # 获取资金记录并校验
                    time.sleep(5)
                    te = self.driver.find_element_by_xpath(
                        "//android.view.View[@content-desc='{}.00元'and@index='6']".format(i)).get_attribute("content-desc")
                    tes = float(re.search("(\d+\.\d+)", te).group())
                    print("tes:", tes)
                    self.assertEqual(tes, i)  # 资金明细中校验记录金额（tes）是否和提现金额（desc）一致
                    self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
                    log1.info("提现资金记录校验通过")
                else:log1.info("测试数据异常")
            self.driver.find_element_by_id()
        except BaseException as e:
            log1.info("测试用例执行出错：%s"%case_name,exc_info=1)
            raise

    class lo():
        pass

    def test_7_Recharge(self):
        self.lo





