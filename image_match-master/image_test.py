#!/usr/bin/env python
# @Time : 2020/4/1 18:30 
# @Author : lifei
#@desc: 借助已经完成的image_auto框架，测试数据

from image_auto import ImageAuto
import time
ia = ImageAuto(2)
ia.start_web(r'"C:\Program Files\Mozilla Firefox\firefox.exe"','http://127.0.0.1:8080/WoniuSales-20180508-V1.4-bin/')
time.sleep(3)
ia.input('user.png','admin')
time.sleep(2)
ia.input('password.png','admin123')
ia.input('verifycode.png','0000')
time.sleep(2)
ia.click('do_login.png')
time.sleep(5)
if ia.exists('home.png'):
    print('测试成功')
else:
    print('测试失败')