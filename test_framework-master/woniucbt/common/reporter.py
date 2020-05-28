# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 14:42 
# @Author : lifei
import pymysql
from PIL import ImageGrab
from pymysql.cursors import SSDictCursor
import time
class Reporter:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','123456','test',charset='utf8')
        self.cursor = self.conn.cursor(cursor=SSDictCursor)
    def write_report(self,version,module,testtype,casetitle,result,screenshot):
        testtime = time.strftime('%Y-%m-%d %H:%M:%S')
        sql = "insert into report(version, module,testtype, " \
              "casetitle, result,testtime, screenshot) " \
              "values('%s','%s', '%s','%s', '%s','%s', '%s')" % \
              (version, module, testtype, casetitle, result,testtime,screenshot)
        self.cursor.execute(sql)
        self.conn.commit()
    def generate_report(self, version):
        sql_all = "select * from report where version='%s'" % version
        self.cursor.execute(sql_all)
        result_list = self.cursor.fetchall()
        test_date = result_list[0]['testtime']  # 测试时间
        test_version = version

        last_time = result_list[len(result_list) - 1]['testtime']

        sql_count = "select result,count(*) count from report where version='%s' GROUP BY result" % version
        self.cursor.execute(sql_count)
        list = self.cursor.fetchall()
        pass_count = 0
        fail_count = 0
        for item in list:
            if item['result'] == '失败':
                fail_count = item['count']
            elif item['result'] == '成功':
                pass_count = item['count']

        content = ''
        for result in result_list:
            content += '\n<tr height="40">'
            content += '\n<td width="10%%">%d</td>' % result['id']
            content += '\n<td width="10%%">%s</td>' % result['module']
            content += '\r<td width="10%%">%s</td>' % result['testtype']
            content += '\n<td width="34%%">%s</td>' % result['casetitle']

            if result['result'] =='失败':
                content += '\n<td width="8%%" bgcolor="red">%s</td>' % result['result']
            elif result['result'] == '成功':
                content += '\n<td width="8%%" bgcolor= "darkseagreen">%s</td>' % result['result']
            else:
                content += '\n<td width="8%%" bgcolor="yellow">%s</td>' % result['result']

            content += '\n<td width="13%%">%s</td>' % result['testtime']
            if result['screenshot'] == '无':
                content += '\n<td width="15%%">%s</td>' % result['screenshot']
            else:
                content += '\n<td width="15%%"><a href="%s">查看截图</a></td>' % result['screenshot']
            content += '\n</tr>'

        # 打开模板文件，并替换模板变量
        with open('../result/template.html', encoding='utf-8') as file:
            template = file.read()

        template = template.replace('$test-date', str(test_date))
        template = template.replace('$test-version', test_version)
        template = template.replace('$pass-count', str(pass_count))
        template = template.replace('$fail-count', str(fail_count))
        template = template.replace('$last-time', str(last_time))
        template = template.replace('$test-result', content)

        filename = time.strftime("%Y%m%d_%H%M%S.html")
        with open('../result/' + filename, mode='w+',encoding='utf-8') as file:
            file.write(template)

    def capture_screen(self):
        time.sleep(1)
        filename = time.strftime('%Y%m%d_ %H%M%S.png')
        ImageGrab.grab().save('../result/'+filename)
        return filename

if __name__ == '__main__':
    Reporter(). generate_report('2.2.8')
    # Reporter().write_report('2.1.2', '登录', 'GUI测试','测试登录功能','成功','无')



