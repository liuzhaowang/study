#!/usr/bin/env python
# @Time : 2020/4/1 17:59
# @Author : lifei
#@desc: 图像匹配 确认可行性
from PIL import Image, ImageGrab
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

import cv2 as cv

class ImageFind:
    def __init__(self):
        self.mouse = PyMouse()
        self.pykeybord = PyKeyboard()

    def find_image_2(self):
        """
        原生算法
        """
        # 打开小图
        small = Image.open('user.png')
        sdata = small.load()
        color_length = len(sdata[0, 0])

        # 对当前屏幕截图(大图)
        if color_length == 3:
            big = ImageGrab.grab()
        else:
            big = ImageGrab.grab().convert('RGBA')
        bdata = big.load()

        # 遍历小图和大图的位置
        for x in range(big.width - small.width):
            for y in range(big.height - small.height):
                if self.check_match(small, bdata, sdata, x, y):
                    # print('找到了,坐标在[%d,%d]'.format(x,y))
                    center_x = int(x + small.width / 2)
                    center_y = int(y + small.height / 2)
                    return (center_x, center_y)
        return (-1, -1)

    def check_match(self, small, bdata, sdata, x, y):
        for i in range(small.width):
            for j in range(small.height):
                if bdata[x + i, y + j] != sdata[i, j]:
                    return False
        return True

    def find_image(self):
        """
        调用cv2
        """
        ImageGrab.grab().save('./screen.png')
        source = cv.imread('./screen.png')
        template = cv.imread('user.png')
        # 调用cv自带的matchTemplate方法进行模板匹配
        result = cv.matchTemplate(source,template,cv.TM_CCOEFF_NORMED)
        location = cv.minMaxLoc(result)
        # 获取最大匹配的位置
        print(location[3])
        pos_start = location[3]
        x = int(pos_start[0]) + int(template.shape[1] /2)
        y = int(pos_start[1]) + int(template.shape[0] /2)
       # 根据匹配度返回坐标，如果匹配度小于95% 则返回无效坐标(-1,-1)
        similarity = location[1]
        if similarity >= 0.95:
            return (x, y)
        else:
            return (-1, -1)


if __name__ == '__main__':
    time.sleep(3)
    finder = ImageFind()
    x,y = finder.find_image()
    finder.mouse.click(x,y)
    finder.pykeybord.type_string('hello123')
    # 对所有操作进行封装
    #