import TestCase.test_weather
import HTMLTestReportCN
import getcwd
import os
import Common.my_email

import unittest
if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestCase.test_weather.weather('test_1_login100'))
    # suite.addTest(TestCase.test_weather.weather('test_16_TransferChecking155'))
    suite.addTest(TestCase.test_weather.weather('test_1_login'))
    path = getcwd.get_cwd()
    # testDir = path+'\\TestCase'
    # discover = unittest.defaultTestLoader.discover(testDir, pattern="test_weather*.py")#discover批量运行
    file_path = os.path.join(path,'report/钱包接口自动化测试报告.html')
    fp = open(file_path,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream = fp,
        title = '钱包接口自动化测试报告',
        description = '钱包前后台交互的接口测试用例',
        tester = 'sitao'

    )
    # runner.run(suite)
    runner.run(suite)
    fp.close()
    # Common.my_email.mail()

    # testDir = 'D:\\TjsApi\\TestCase\\'  # 定义测试用例目录
    # reportDir = "D:\\TjsApi\\Android_report\\"  # 定义报告存放路
    # runner = HTMLTestRunner(stream=fp, title=u"同金社Android流程测试报告", description=u"测试用例执行情况：")
    # runner.run(discover)  # 运行用例生成报告
