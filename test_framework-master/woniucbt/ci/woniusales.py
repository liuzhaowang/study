# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/7 11:25 
# @Author : lifei
# @desc:针对woniusales从源码到打包部署.测试.报告到邮件发送全流程持续集成
import re

from woniucbt.suit.woniusales import WOniuSalesSuit
import time, os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from woniucbt.common.utility import Utility

class WoniuSaleCI:

    def __init__(self):
        self.svn_folder = Utility.get_config_value('ci','svn')
        self.svn_url = Utility.get_config_value('ci','svn_url')
        self.tomact_folder = Utility.get_config_value('ci','tomcat')
        self.result_folder = os.path.abspath('../result')
        self.ci_folder = os.path.abspath('.')

    # 从源码库下载woniusales源代码
    def svn(self):
        try:
            os.listdir(self.svn_folder)
            os.system('svn update %s' % self.svn_folder)
        except:
            os.mkdir(self.svn_folder)
            os.system('svn checkout %s %s --username=fei --password=123456' % (self.svn_url, self.svn_folder))

    # 利用ant编译源代码war包,用于安装
    def ant(self):
        os.system('ant -f %s/build.xml' % self.svn_folder)
        print('Ant已经构建完成源代码构建')

    # 复制war包到tomcat的webapps部署目录下
    def deploy(self):
        # 先停止tomacta
        os.system(r'%s \bin\shutdown.bat' % self.tomact_folder)
        # 删除webapps目录下已有的war和目录
        os.system('rd /S /Q %s\webapps\woniusales' % self.tomact_folder)
        os.system('del /S /Q %s\webapps\woniusales.jar' % self.tomact_folder)
        # 复制war包到webapps目录下
        os.system('copy %s\woniusales.war %s\webapps' % (self.svn_folder, self.tomact_folder))
        os.system(r'%s \bin\startup.bat' % self.tomact_folder)
        print('安装部署新版本到Tomcat完成')
        time.sleep(20)

    # 开始测试
    def test(self):
        # 测试进行之前先删除result目录下的东西
        os.system(r'del /S /Q %s\* ' % self.result_folder)
        os.system(r'copy %s\temlate.html %s' % (self.ci_folder, self.result_folder))
        time.sleep(3)
        WOniuSalesSuit.start_test()

    # 轮询svn服务器,确认是否有新版本,则立即持续集成
    def check(self):
        while (True):
            out_put = os.popen('svn update %s' % self.svn_folder).read()
            list = str(out_put).strip().split('\n')
            if len(list) > 2:
                print('检测到新版本 开始持续集成')
                ci.svn()
                ci.ant()
                ci.deploy()
                ci.test()
            else:
                print('目前没有检测到新版本')

    # 按需启动持续集成
    def start(self):
        self.svn()
        self.ant()
        self.deploy()
        self.test()
        self.report()
        self.email()

    # 对测试报告进行打包 并发送邮件
    def report(self):
        # 先对result目录进行压缩
        os.system(r'"%s" a %s\report.rar %s' % (Utility.get_config_value('ci','rar'),self.ci_folder, self.result_folder))
        time.sleep(5)
        # 获取report目录下的html报告名
        list = os.listdir(self.result_folder)
        for item in list:
            if re.match('\\d+_\\d+\\.html', item):
                report_name = item
                break
        with open(self.result_folder + './' + report_name, encoding='utf-8') as file:
            body = file.read()
        self.email(body, '%s\\report.rar' % self.ci_folder)

    # 发送邮件
    def email(self, body, attach):
        sender = '****@163.com'  # 发送邮箱
        receivers = '****@qq.com'  # 接收邮箱
        # 三个参数:第一个为文本内容，第二个plain 设置文本格式，第三个utf-8_ 设置编码
        # message = MIMEText('<p style="color: red; font-size: 30px">这是一 封来自Python发送的测试邮件的
        # message[ 'Subject'] = Header( '- -封Python发送的邮件’， 'utf-8')
        msg = MIMEMultipart()
        msg['Subject'] = 'WoniuSales持续集成报告'
        msg['From'] = sender
        msg['To'] = receivers
        content = MIMEText(body, 'html', 'utf-8')
        msg.attach(content)
        attachment = MIMEApplication(open(attach, 'rb').read())
        attachment.add_header('Content-Disposition', 'attachment', filename='report.rar')
        msg.attach(attachment)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('smtp.163.com', '25')
            smtpObj.login(user=sender, password='*****')
            smtpObj.sendmail(sender, receivers, str(msg))
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error:无法发送邮件")


if __name__ == '__main__':
    ci = WoniuSaleCI()
    ci.report()
    # ci.email('<font color="red">测试报告</font>', ci.ci_folder+'/report.rar')
