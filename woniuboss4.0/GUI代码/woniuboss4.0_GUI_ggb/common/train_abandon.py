from common.login import Login

class TrainAbadon:
    def __init__(self,driver):
        self.driver=driver
        self.login=Login(self.driver).do_login_zixun_manager('..\\config\\base.conf')


