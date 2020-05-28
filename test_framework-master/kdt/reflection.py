# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/8 16:51 
# @Author : lifei
# @desc:
class MyTest:
    phone = '17710414567'
    def get_name(self):
        print('蜗牛学院')

    def get_addr(self):
        print('成都孵化园')

    def set_value(self,value):
        print('你设置了值%s'% value)

    def test(self):
        def run():
            print('这是闭包里边的内容')
        return run

    # print(test())
# if __name__ == '__main__':
#     my = MyTest()
    # print(dir(my))
    # getattr(my,'get_name')()
    # getattr(my,'set_value')('hello')
    # print(getattr(my,'phone'))
    # print(hasattr(my,'get_name'))
    # print(id(getattr(my,'get_name')))
    # setattr(my,'phone','17888888')

