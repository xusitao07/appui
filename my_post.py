# coding=utf-8
from Common.Base_test import webrequests
import requests
class mytest():
    def __init__(self, url2, file):
        self.url2 = url2
        self.file = file

    def session_post(self):
        self.url = "http://admin.aiyomi.com/login.html"
        self.pos = {"phone": "15268299107", "password": "aa111111"}
        self.sess = requests.session()
        sess1 = self.sess.post(self.url, self.pos)
        # response_json = sess1.json()
        print(sess1)
        # print(sess1.json())
        sess2 = self.sess.post(self.url2, self.file)
        print("创建成功",sess2)
        # print(sess2.json())

if __name__ == '__main__':
    # url2 = "http://admin.aiyomi.com/server/wiki/edit_cook.html"
    # file = {
    #     "id": "0",
    #     "title": "王企鹅群翁群无124",
    #     "type": "vedio",
    #     "cook_type": "boil",
    #     "month_type": "",
    #     "function_type": "calcium",
    #     "display_order": "0",
    #     "read": "0",
    #     "image": "https://aiyomi.oss-cn-hangzhou.aliyuncs.com/aiyomi/20190820175157145.jpg",
    #     "remark": "文青翁群翁群翁群翁群翁",
    #     "media_url": "https://s1.aiyomi.cn/video/20190820175304178.m3u8",
    #     "content": "6K+36Zeu5LyB6bmF57+B576k57+B576k5LqM576k5LqMcQ=="
    # }
    url2 = "http://admin.aiyomi.com/server/section/edit_section.html"
    url1 = "http://admin.aiyomi.com/server/section/get_section_by_course_age.html"
    subtitle = ["起床音乐", "亲子对话", "经典名曲", "亲子游戏", "晚安故事"]
    too = webrequests()#3333
    for j in range (193,200):#设定新建课程天数区间
        too.config_write('course_age', "age_match", str(j))
        too.config_write('CoreCourse', "age_match", str(j))
        course_age = too.confige_items('course_age')
        edit_section = mytest(url1, course_age)
        edit_section.session_post()
        for i in subtitle:
            if i == "起床音乐":
                too.config_write('CoreCourse', "subtitle", i)
                too.config_write('CoreCourse', "parent_id", "0")
                # display_order入参 对应列表的下标subtitle.index(i)
                too.config_write('CoreCourse', "display_order", str(subtitle.index(i)))
                file_coure2 = too.confige_items('CoreCourse')
                edit_section = mytest(url2, file_coure2)
                edit_section.session_post()
                #查找并添加父id parent_id
                sql = str("SELECT parent_id FROM you_course.f_section ORDER BY parent_id DESC LIMIT 1")
                parent_id = str(too.get_identifying_code(sql, "parent_id", "you_course"))
                too.config_write('CoreCourse', "parent_id", parent_id)
            else:
                too.config_write('CoreCourse', "display_order", str(subtitle.index(i)))
                too.config_write('CoreCourse', "subtitle", i)
                file_coure = too.confige_items('CoreCourse')
                # print(file_coure)
                edit_section = mytest(url2, file_coure)
                edit_section.session_post()


