import requests,unittest

class Login:

    def __init__(self):
        self.session = requests.session()
    def do_login_(self):
        login_url = 'http://localhost:8080/WoniuBoss/login/userLogin'
        login_data = {"userName":"WNCD056","userPass":"woniu123","checkcode":"0000","remember":"Y"}
        login_resp = requests.post(login_url,login_data)
        print(login_resp.text)

    def add_notice(self):
        add_notice_url = 'http://localhost:8080/WoniuBoss/notice/doAdd'
        add_notice_data = {"title":"我的公告","content":"<p>疫情当下,带好口罩<br></p>"}
        add_notice_resp = requests.post(add_notice_url,add_notice_data)
        print(add_notice_resp)

    def queryNetCus(self):
        queryNetCus_url = 'http://localhost:8080/WoniuBoss/market/queryNetCus'
        queryNetCus_data = {"pageSize":"10","pageIndex":"1"}
        queryNetCus_resp = requests.post(queryNetCus_url,queryNetCus_data)
        print(queryNetCus_resp.text)


# class Login_test(unittest.TestCase):
#     def setUpClass(self):
#         self.login = Login()
#
#     def test_do_login01(self):
#         test_info1 = ('admin',)

if __name__ == '__main__':

    # Login().do_login_()
    Login().queryNetCus()