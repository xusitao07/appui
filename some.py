#coding = utf-8
# def log(func):
#     def wrapper(*args,**kwargs):
#         print("call:%s"%func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def run():
#     print("result")
# import time,functools
# def meter(func):
#     @functools.wraps(func)
#     def log(*args,**kwargs):
#         # print(time.ctime())
#         print(func(*args,**kwargs))
#     return log
# @meter
# def fast(x,y):
#     time.sleep(1)
#     return int(x+y)
# @meter
# def slow(x,y,z):
#     time.sleep(2)
#     return int(x*y*z)
# f = fast(11,22)
# s = slow(11,22,33)
# if f!=33:
#     print("失败")
# elif s != 7986:
#     print("失败")

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def log(*args,**kw):
        # print('fn():%s'%time.ctime())
        c = fn(*args, **kw)
        if c == 33:
            print('测试成功:', c)
        elif c == 7986:
            print('测试成功',c)
        else:print("失败")
    return log
@metric
def fast(x,y):
    time.sleep(1)
    return (x+y)
@metric
def slow(x,y,z):
    time.sleep(1)
    return (x*y*z)
fast(11,22)
fast(12,22)
fast(13,22)
fast(14,22)
fast(15,22)
fast(16,22)
slow(11,22,33)
# if c != 33:
#     print('测试失败:',c)
# elif s!=7986:
#     print('测试失败')
