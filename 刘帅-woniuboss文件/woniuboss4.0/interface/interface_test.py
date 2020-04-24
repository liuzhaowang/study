import requests

class InterFace:
    def __init__(self):
        self.session = requests.session()
    # def do_login(self):
        self.login_url = 'http://localhost:8080/WoniuBoss4.0/login/userLogin'
        self.login_data = {"userName":"WNCD000","userPass":"woniu123","checkcode":"0000","remember":"Y"}
        self.login_resp = self.session.post(self.login_url,self.login_data)
        # print(self.login_resp.text)

    def queryVersion(self):
        self.qversion_url = 'http://localhost:8080/WoniuBoss4.0/sysVersion/queryVersion'
        self.qversion_data = {"pageSize":"10","pageIndex":"1"}
        self.qversion_resp = self.session.post(self.qversion_url,self.qversion_data)
        print(self.qversion_resp.text)

    def queryUser(self):
        self.quser_url = 'http://localhost:8080/WoniuBoss4.0/user/queryUser'
        self.quser_data = {"pageSize":"10","pageIndex":"1","userName":"","empName":""}
        self.quser_resp = self.session.post(self.quser_url,self.quser_data)
        print(self.quser_resp.status_code)
        if self.quser_resp.status_code == 200:
            print('测试成功')
        else:
            print('测试失败')

    def modifysysInfo(self):
        self.modify_url = 'http://localhost:8080/WoniuBoss4.0/employee/saveModifyEmp'
        self.modify_data = {"emp.employee_id":"2","emp.region_id":"4","emp.department_id":"23",
                            "emp.position":"测试开发工程师","emp.employee_name":"王大治","emp.sex":"男",
                            "emp.entry_time":"2020-05-01","emp.work_id":"","emp.emp_status":"01",
                            "emp.leave_time":"","emp.tel":"15615238899","emp.email":"","emp.qq":"",
                            "emp.education":"","emp.university":"","emp.major":"","emp.address":"",
                            "emp.source":"","emp.cardnum":"","emp.identity":"","emp.birthday":"",
                            "emp.birthday_type":"01","emp.emergency_contact":"","emp.emergency_tel":"",
                            "emp.emegency_relation":""}
        self.modify_resp = self.session.post(self.modify_url,self.modify_data)
        print(self.modify_resp.text)

    def getSelectValue(self):
        gsv_url = 'http://localhost:8080/WoniuBoss4.0/select/getSelectValue'
        gsv_data = {"elementName":"orientation"}
        gsv_resp = self.session.post(gsv_url,gsv_data)
        result = gsv_resp.text
        if result == '["公共","开发","测试"]':
            print('测试成功')
        else:
            print('测试失败')

    def saveApply(self):
        sa_url = 'http://localhost:8080/WoniuBoss4.0/apply/saveApply'
        sa_data = {"phone":"","apply.work_id":"WNCD000","apply.start_time":"2020-04-18+22:04",
                   "apply.end_time":"2020-04-19+00:00","apply.accounting_way":"02","apply.hours":"2小时",
                   "apply.region_id":"4","apply.reason":"开心不行啊,缺钱不行啊"}
        sa_resp = self.session.post(sa_url,sa_data)
        print(sa_resp.text)

    def addAss(self):
        aa_url = 'http://localhost:8080/WoniuBoss4.0/assets/addAss'
        aa_data = {"ass.assets_name":"01","ass.assets_type":"15","ass.bar_code":"55886699899",
                   "ass.price":"250","purchase_employee":"王大治","ass.purchase_employee_id":"2",
                   "ass.purchase_time":"2020-04-18","ass.note":"意外","ass.assets_owner":"01"}
        aa_resp = self.session.post(aa_url,aa_data)
        print(aa_resp.text)

    def saveModifyAss(self):
        smf_url = 'http://localhost:8080/WoniuBoss4.0/assets/saveModifyAss'
        smf_data = {"ass.assets_id":"3","purchase_employee":"王大治","ass.purchase_employee_id":"2",
                    "ass.purchase_time":"2020-04-18","ass.state":"01","ass.note":"意外","ass.assets_owner":"02"}
        smf_resp = self.session.post(smf_url,smf_data)
        print(smf_resp.text)
if __name__ == '__main__':
    L= InterFace()
    # L.do_login()
    # L.queryVersion()
    # L.modifysysInfo()
    # L.getSelectValue()
    # L.saveApply()
    # L.addAss()
    L.saveModifyAss()