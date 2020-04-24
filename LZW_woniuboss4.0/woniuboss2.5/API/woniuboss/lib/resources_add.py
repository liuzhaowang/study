import time
from selenium.webdriver.common.by import By
from woniuboss.tools.server import Service


class Resources_Add:

    def __init__(self,driver):
        self.driver= driver

    # 点击新增
    def click_add_button(self):
        Service.click_element(self.driver,By.CSS_SELECTOR, "button.btn-padding:nth-child(1)")

    #输入电话
    def input_phone(self,tel):
        Service.send_input(self.driver,By.NAME,"cus.tel",tel)

    #输入姓名
    def input_name(self,name):
        Service.send_input(self.driver,By.NAME,"cus.name",name)

    #选择性别
    def select_sex(self):
        Service.select_random(self.driver,By.NAME,"cus.sex")

    #选择最新状态
    def last_status(self,status):
       Service.select_random(self.driver,By.CSS_SELECTOR,"select.form-control:nth-child(2)",selector=status)

    #输入邮箱
    def input_email(self,email):
        Service.send_input(self.driver,By.NAME,"cus.email",email)

    #输入QQ号
    def input_qq(self,qq):
        Service.send_input(self.driver,By.NAME,"cus.qq",qq)

    #输入学校
    def input_school(self,school):
        Service.send_input(self.driver,By.NAME,"cus.school",school)

    #选择学历
    def select_education(self):
        Service.select_random(self.driver,By.NAME,"cus.education")

    #输入专业
    def input_major(self,major):
        Service.send_input(self.driver,By.NAME,"cus.major",major)

    #输入求职意向
    def input_intent(self,intent):
        Service.send_input(self.driver,By.NAME,"cus.intent",intent)

    #选择工作年限
    def selcet_workage(self):
        Service.select_random(self.driver,By.NAME,"cus.workage")

    #输入期望薪水
    def input_salary(self,salary):
        Service.send_input(self.driver,By.NAME,"cus.salary",salary)

    #选择渠道来源
    def select_source(self):
        Service.select_random(self.driver,By.CSS_SELECTOR,"#addCus > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > select:nth-child(2)")

    #输入应聘职位
    def input_applposition(self,applposition):
        Service.send_input(self.driver,By.NAME,"cus.applposition",applposition)

    #输入年龄
    def input_age(self,age):
        Service.send_input(self.driver,By.NAME,"cus.age",age)

    #输入教育经历
    def input_eduexp(self,eduexp):
        Service.send_input(self.driver,By.NAME,"cus.eduexp",eduexp)

    #输入工作经历
    def input_experience(self,experience):
        Service.send_input(self.driver,By.NAME,"cus.experience",experience)

    #输入最后跟踪
    def input_last_tracking_remark(self,last_tracking_remark):
        Service.send_input(self.driver,By.NAME,"cus.last_tracking_remark",last_tracking_remark)

    #点击保存
    def click_save(self):
        Service.click_element(self.driver,By.ID,"addCusBtn")

    #新增成功信息确认
    def click_ok(self):
        Service.click_element(self.driver, By.XPATH, "/html/body/div[14]/div/div/div[3]/button")

    # 新增培训资源,将新增培训资源的整个流程动作放在一起
    def add_source(self,tel,name,status,email,qq,school,major,intent,salary,applposition,age,eduexp,experience,last_tracking_remark):
        self.click_add_button()
        self.input_phone(tel)
        self.input_name(name)
        self.select_sex()
        self.last_status(status)
        self.input_email(email)
        self.input_qq(qq)
        self.input_school(school)
        self.select_education()
        self.input_major(major)
        self.input_intent(intent)
        self.selcet_workage()
        self.input_salary(salary)
        self.select_source()
        self.input_applposition(applposition)
        self.input_age(age)
        self.input_eduexp(eduexp)
        self.input_experience(experience)
        self.input_last_tracking_remark(last_tracking_remark)
        self.click_save()   #点击保存
        time.sleep(0.5)
        self.click_ok()    #点击新增确认按钮

