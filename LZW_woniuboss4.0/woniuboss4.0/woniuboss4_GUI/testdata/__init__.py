# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         __init__.py
# Description:  
# Author:       Administrator
# Date:         2020/2/11
#-------------------------------------------------------------------------------

# 第一步:读取文件 获取文件中的所有内容
with open("D:\study_all\笔记\Python2019.13.13\Python\Resource\WoniuSales.txt","r") as file:
    lines = file.readlines()
print(type(lines)) # <class 'list'>
print(lines)
print(len(lines))  # 17 表示文件中有17行数据

# 第二步:把文件中的内容读取到字典中
# 字典的格式{用例名称:[用例步骤]}
index = []
dct = {}
import re
for i, line in enumerate(lines):
    print(i,line)
    # i 是 line 在lines这个列表中的下标
    if re.match("^test_login", line):
        index.append(i)
    if len(index) == 2:
        # 开始切片
        dct[lines[index[0]]] = lines[index[0] + 1:index[1]]
        # 保证index的长度用于为2 要删除第一个用例的下标.
        index.pop(0)
# 补切最后一个用例
dct[lines[index[0]]] = lines[index[0] + 1:]
print(dct)
# 第三步:处理字典的键和键所对应的值
# 用于处理字典结束后所保留下来的数据
tcl = []

# 对字典做遍历
# for item in dct.items(): # print(type(item)) 元组(key,value)
for key, value in dct.items():
    # 保存一个用例
    li = []
    step = []
    title = key.split(":")[0]
    li.append(title)
    for i, s in enumerate(value):
        # 去除左右两边的空格 换行等符号 中间的去不掉
        s = s.strip()
        # 判断一行是否以s1 s2 或者s3 ... s6 开头.把这一行保存下来
        # 在正则中\d表示为0-9 d 是digit的缩写
        # 这里有个小bug.s11 能匹配上吗?
        if re.match("^s\\d", s):
            # 首先切掉sx x的取值0-9
            # 1告诉它只切第一个
            s = s.split(":", 1)[1].split(",")
            step.append(s)

    li.append(step)
    # 一个用例已经完成了 把用例放入列表
    tcl.append(li)

print("---------------")
for i in tcl:
    print(i)
