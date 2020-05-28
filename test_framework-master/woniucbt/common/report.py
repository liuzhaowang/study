import pymysql
import os
import time


class Report:

    def __init__(self, version):
        self.version = version

    def write_report(self, module, type, case_id, case_title, result, error, screenshot):
        # 构造一个数据库连接对象
        con = pymysql.connect(user='root', password='123456', host='192.168.52.130', db='woniucbt', charset='utf8')
        # 获取游标对象
        cursor = con.cursor()
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        sql = f'insert into report(version,`module`,`type`,case_id,case_title,result,`time`,error,screenshot)' \
              f'values("{self.version}","{module}","{type}","{case_id}","{case_title}","{result}","{now}","{error}","{screenshot}");'
        cursor.execute(sql)
        con.commit()
        cursor.close()
        con.close()

    def generate_html_report(self):
        con = pymysql.connect(user='root', password='123456', host='192.168.52.130', db='woniucbt', charset='utf8')
        cursor = con.cursor()
        querysql = 'select * from report where version ="{}"'.format(self.version)
        cursor.execute(querysql)
        result = cursor.fetchall()
        if not len(result):
            print("当前没有测试结果")
            return
        # 读取测试报告的模板
        with open(os.path.join(os.getcwd(), 'template.html'), 'r', encoding='utf8') as f:
            content = f.read()
        # 替换版本
        content = content.replace('$test-version', self.version)
        failsql = 'select count(*) from report where version ="{}" and result="失败"'.format(self.version)
        cursor.execute(failsql)
        fail_count = str(cursor.fetchone()[0])
        content = content.replace('$fail-count', fail_count)
        passsql = 'select count(*) from report where version ="{}" and result="成功"'.format(self.version)
        cursor.execute(passsql)
        pass_count = str(cursor.fetchone()[0])
        content = content.replace('$pass-count', pass_count)
        errorsql = 'select count(*) from report where version ="{}" and result="错误"'.format(self.version)
        cursor.execute(errorsql)
        error_count = str(cursor.fetchone()[0])
        content = content.replace('$error-count', error_count)
        last_timesql = 'select time from report where version ="{}" order by time desc limit 1 '.format(self.version)
        cursor.execute(last_timesql)
        last_time = str(cursor.fetchone()[0])
        last_date = last_time.split(' ')[0]
        content = content.replace('$test-date', last_date)
        content = content.replace('$last-time', last_time)
        test_result = ''
        for record in result:
            # 根据成功失败变化颜色
            if record[6] == '成功':
                color = 'lightgreen'
            elif record[6] == '失败':
                color = 'red'
            else:
                color = 'yellow'
            if record[9] == '无':
                screenshot = '无'
            else:
                screenshot = f'<a href="{record[9]}">查看截图</a>'
            test_result += f'<tr height="40">'\
				            f'<td width="7%">{record[0]}</td>'\
				            f'<td width="9%">{record[2]}</td>'\
				            f'<td width="10%">{record[3]}</td>'\
				            f'<td width="7%"> {record[4]}</td>'\
				            f'<td width="20%"> {record[5]}</td>'\
				            f'<td width="7%" bgcolor="{color}">{record[6]}</td>'\
				            f'<td width="15%"> {record[7]}</td>'\
				            f'<td width="15%">{record[8]}</td>'\
				            f'<td width="10%">{screenshot}</td>'\
			                f'</tr>\r\n'
        content = content.replace('$test-result', test_result)
        now = int(time.time())
        with open(os.path.join(os.getcwd(), f'cbt_{now}.html'), 'w', encoding='utf8')as f:
            f.write(content)


if __name__ == '__main__':
    report = Report("1.0")
    # report.write_report("支付模块","UI测试","001","支付金额大于实际金额","失败","无","无")
    # report.write_report("支付模块", "UI测试", "002", "支付现金测试", "失败", "无", "无")
    # report.write_report("支付模块", "UI测试", "001", "支付微信测试", "失败", "无", "无")
    report.generate_html_report()
