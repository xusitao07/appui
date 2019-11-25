from Common.Base_test import webrequests
from Logs.log import log1

section = 'login'
username = '测试'
password = '一下'

s = webrequests()

s.config_write(section)
log1.info("写入section:%s" % section)
s.config_write(section, 'username', username)
log1.info("写入%s下的用户名是：%s" % (section, username))
s.config_write(section, 'password', password)
log1.info("写入%s下的密码是：%s" % (section, password))

url = s.confige_get('test', 'url', url='test/test1')
get_username = s.confige_get(section, 'username')
log1.info("读取的用户名:%s" % get_username)
get_password = s.confige_get(section, 'password')
log1.info("读取的密码:%s" % get_password)

s.config_delete(section, 'usrename', )
log1.info("删除%s下的username" % section)
s.config_delete(section, 'password')
log1.info("删除%s下的password" % section)
s.config_delete(section)
log1.info("删除%s" % section)

