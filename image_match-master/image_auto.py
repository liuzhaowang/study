#!/usr/bin/env python
# @Time : 2020/4/1 18:21 
# @Author : lifei
#@desc: 封装image_find
import os

from PIL import Image, ImageGrab
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import cv2 as cv

class ImageAuto:
    def __init__(self,wait=1):
        self.mouse = PyMouse()
        self.pykeybord = PyKeyboard()
        self.wait = wait

    def find_image(self,filename):
        """
        调用cv2
        """
        ImageGrab.grab().save('./screen.png')
        source = cv.imread('./screen.png')
        template = cv.imread(filename)
        # 调用cv自带的matchTemplate方法进行模板匹配
        result = cv.matchTemplate(source,template,cv.TM_CCOEFF_NORMED)
        location = cv.minMaxLoc(result)
        # 获取最大匹配的位置
        # print(location[3])
        pos_start = location[3]
        x = int(pos_start[0]) + int(template.shape[1] /2)
        y = int(pos_start[1]) + int(template.shape[0] /2)
       # 根据匹配度返回坐标，如果匹配度小于95% 则返回无效坐标(-1,-1)
        similarity = location[1]
        if similarity >= 0.95:
            return (x, y)
        else:
            return (-1, -1)

    def click(self,filename):
        x,y = self.find_image(filename)
        self.mouse.click(x,y)
        # print('在位置(%d,%d)做单击'.format(x,y))
        time.sleep(self.wait)

    # 输入之前清空文本框内容
    def input(self,filename,content):
        x,y = self.find_image(filename)
        self.mouse.click(x,y)
        self.pykeybord.type_string(content)
        # print('在位置(%d,%d)做输入%s'.format(x, y,content))
        time.sleep(self.wait)

    # 断言
    def exists(self,filename):
        x,y = self.find_image(filename)
        if (x,y) == (-1,-1):
            return False
        else:
            return True

    # 启动应用程序
    def start_app(self,cmd):
        os.system('start /b '+cmd)

    # 启动浏览器
    def start_web(self,exe,url):
        os.system('start /b %s %s'%(exe,url))
