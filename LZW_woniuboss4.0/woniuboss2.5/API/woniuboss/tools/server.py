

from woniuboss.tools.util import Utility
import requests
class Service:

    # 判断页面上的某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            # 表示没找到
            return False
        return True

    # 向一个文本输入框执行三个固定操作：点击、清理、输入
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    # 随机选择下拉框中的一项
    @classmethod
    def select_random(cls, selecter):  # selecter是传递的下拉框元素
        from selenium.webdriver.support.select import Select
        seleter_length = len(Select(selecter).options)
        import random
        random_index = random.randint(0, seleter_length - 1)
        Select(selecter).select_by_index(random_index)

    # 去掉某个元素的只读属性（id）
    @classmethod
    def remove_readonly(cls, driver, ele_id):
        driver.execute_script('document.getElementById("%s").readOnly=false' % (ele_id))



    # 生成driver
    @classmethod
    def get_driver(cls, path):
        contents = Utility.get_json(path)
        from selenium import webdriver
        driver = getattr(webdriver, contents['BROWSER'])()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

    # 打开页面的方法
    @classmethod
    def open_page(cls, driver, path):
        contents = Utility.get_json(path)
        URL = 'http://%s:%s/%s' % (contents['HOSTNAME'], contents['PORT'],contents['AURL'])
        driver.get(URL)

    # 具体的业务功能需要绕过登录，使用cookie
    @classmethod
    def miss_login(cls, driver, base_config_path):
        cls.open_page(driver, base_config_path)
        # 通过字典方式传递cookie信息
        contents = Utility.get_json(base_config_path)
        driver.add_cookie({'name': 'username', 'value': contents['username']})
        driver.add_cookie({'name': 'password', 'value': contents['password']})
        cls.open_page(driver, base_config_path)

    # 截图.仅进行截图操作
    @classmethod
    def get_png(cls,driver,png_path):
        driver.get_screenshot_as_file(png_path)

    # 出现缺陷后的截图方法
    @classmethod
    def get_error_png(cls,driver):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        png_path = '..\\bugpng\\error_%s.png'%(ctime)
        cls.get_png(driver,png_path)

    @classmethod
    def get_session(cls,sum):
        base_info = Utility.get_json('..\\config\\base.conf')
        login_url = "%s://%s:%s/%s/" % (base_info['PROTOCOL'], base_info['HOSTNAME'], base_info['PORT'], base_info['AURL'],)
        print(login_url)
        base_data=Utility.get_json('..\\config\\Account.conf')
        login_data = {'userName': base_data[sum]['userName'], 'userPass': base_data[sum]['userPass'],'checkcode': base_data[sum]['checkcode']}
        print(login_data)
        session = requests.session()
        resp=session.post(login_url, login_data)
        print(resp.text)
        return session

if __name__ == '__main__':
    # a=Service.get_driver("..\\config\\base.conf")
    # Service.open_page(a,"..\\config\\base.conf")
    a=Service.get_session(2)
    print(a)