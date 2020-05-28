from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os
import time


# 代码思路
# 1. 首先定义一个测试类ImageTest
# 2. 定义一个初始化方法
#  2.1 定义一个mouse变量, 并对pymouse类进行实例化
#  2.2 定义一个keyboard变量,并对PyKeyboard类进行实例化
#  2.3 定义一个match变量,并对imageMatch模块进行实例化
# 3. 定义一个应用启动方法start_app, 定义一个参数 cmd(cmd命令)
#  3.1 利用os模块中的system方法,去执行命令"start /b + cmd"
#  3.2 加一个sleep,目的是等应用启动起来
# 4. 定义一个单击的方法click,有一个参数target,就是模板文件
#  4.1 先去利用match对象的find_image 方法去查找指定的模板,并将查找的结果赋值给x,y
#  4.2 检查x,y坐标,看看是否找到,如果没有找到,打印没找到的消息,然后单击方法返回
#  4.3 如果找到,那么就要对这个位置进行单击操作
#  4.4 利用mouse对象的click方法传入坐标即可
#  4.5 加一个sleep,目的是让操作不要太快
#  4.6 打印在 x,y位置做了一个单机操作
# 5. 定义一个双击的方法double_click,有一个参数target(模板图片)
#  5.1 利用match对象的find_image方法查找指定的模板,并将结果赋值给x,y
#  5.2 检查x,y坐标,如果没找到就输出相应的信息并返回
#  5.3 如果找到就利用mouse对象的click方法传入坐标以及操作次数的参数
#  5.4 加一个sleep防止操作过快
#  5.5 输出双击操作信息
# 6. 定义一个输入字符的方法input,有两个参数,一个是target,另一个是content(必须为字符串,数值需要类型转化)
#  6.1 调用前面实现的double_click方法
#  6.2 利用keyboard对象的方法type_string来输入content参数即可实现输入的动作
#  6.3 加一个sleep防止操作过快
#  6.4 打印输入操作信息
# 7. 定义一个下拉选择的方法select,有两个参数,一个是target,另一个是count的次数(下方向键的次数)
#  7.1 调用之前实现的click方法
#  7.2 利用for循环来实现在下拉菜单中选择运算方法的动作,range(就是count)
#  7.3 在循环体内部利用keyboard对象press_key方法来执行按键动作,具体按键又传入得参数决定,这里我们传入self.keyboard.dowm_key
#  7.4 按键完成别忘了做一个sleep,防止操作太快
#  7.5 在循环结束后,再次利用keyboard对象的press_key方法来执行按回车键确认的动作self.keyboard.enter_key
#  7.6 加一个sleep,防止操作过快
#  7.7 输出选择菜单的相应信息
# 8. 定义一个测试方法strat_test
#  8.1 调用start_app 方法启动被测应用
#  8.2 调用input方法输入
#  8.3 调用select方法选择运算类型
#  8.4 调用click方法单击计算按钮
#  8.5 利用match对象的check_exists方法检查运算结果
#  8.6 依据检查结果输出测试成功还是失败
from imageMatch import ImageMatch
from openCVdemo import ImageMatchByCV


class ImageTest:

    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        self.match = ImageMatchByCV()

    # 定义一个启动应用的方法
    def start_app(self,cmd):
        # os.system('start /b {}'.format(cmd))
        os.system(cmd)
        print("应用成功启动")
        time.sleep(5)

    # 定义一个关掉应用的方法
    def stop_app(self,cmd):
        os.system('taskkill /f /im {}'.format(cmd))
        print('应用成功关闭')

    # 定义一个鼠标单击的方法
    def click(self,target):
        x,y = self.match.find_image(target)
        if x == -1 and y == -1 :
            print("没找到{}".format(target))
            return
        self.mouse.click(x,y)
        print("在[{},{}]位置单击{}".format(x,y,target))
        time.sleep(0.5)

    # 定义一个鼠标双击的操作
    def double_click(self,target):
        x, y = self.match.find_image(target)
        if x == -1 and y == -1:
            print("没找到{}".format(target))
            return
        self.mouse.click(x,y,n=2)
        print("在[{},{}]位置双击{}".format(x, y, target))
        time.sleep(0.5)

    # 定义键盘输入的动作
    def input(self,target,content):
        self.double_click(target)
        # content 类型必须是字符串类型
        self.keyboard.type_string(content)
        print("在{}上输入{}".format(target,content))
        time.sleep(0.5)

    # 定义一个下拉选单选择的方法
    def select(self,target,count):
        self.click(target)
        # 这里应该对count做一个检查
        for i in range(count):
            self.keyboard.press_key(self.keyboard.down_key)
            time.sleep(0.5)
        self.keyboard.press_key(self.keyboard.enter_key)
        print("在{}上选择第{}项".format(target,count+1))
        time.sleep(0.5)

    # 定义一个测试方法
    def start_test(self):
        self.start_app('"C:\Program Files\Mozilla Firefox\firefox.exe" "https://snailpet.com/index"')
        time.sleep(5)
        self.input('username.PNG','17710414056')
        self.input('password.png', 'woniu123')
        # self.keyboard.press_key(self.keyboard.enter_key)
        self.click('submit.png')
        time.sleep(2)
        if self.match.check_exists('home.png'):
            print('测试成功')
        else:
            print('测试失败')

if __name__ == '__main__':
    ImageTest().start_test()
