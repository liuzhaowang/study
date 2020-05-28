import cv2
from PIL import ImageGrab
import os


# 代码思路
# 1. 首先定义一个类ImageMatchByCV
# 2. 定义图像识别的核心方法find_image,参数是target
#  2.1 定义模板图片所在位置的路径image_path
#  2.2 定义截取的大图的保存路径screen_path,将来文件名可以定义为screen_shot.png
#  2.3 利用ImageGrab方法截取当前屏幕的大图,同时对该对象调用其保存的方法
#  2.4 利用CV2模块的imread方法分别读取大图和模板小图,获得screen与template图像对象
#  2.5 利用算法,传入两个图像参数
# 3. 定义一个检查指定模板图片是否存在的方法 check_exists

class ImageMatchByCV:

    def find_image(self, target):
        image_path = os.path.join(os.getcwd(), 'source')
        # 定义截图保存位置
        screen_path = os.path.join(image_path, 'screen_shot.png')
        ImageGrab.grab().save(screen_path)
        # 分别获取大图和小图的图像
        screen = cv2.imread(screen_path)
        template = cv2.imread(os.path.join(image_path,target))
        # 进行模板匹配
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # 获取匹配的结果
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)
        if max < 0.95:
            return -1, -1
        # 获取中心点坐标
        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x, y

    def check_exists(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1
