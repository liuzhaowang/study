from PIL import  ImageGrab,Image
import os


class ImageMatch:

    def __init__(self):
        self.screen =None
        self.template =None
        self.screen_data = None
        self.template_data = None


    def compare(self,p1,p2):
        return p1[0] == p2[0] and p1[1]==p2[1] and p1[2]==p2[2] and p1[3] == p2[3]

    def find_image(self, target):
        image_path = os.path.join(os.getcwd(), 'source')
        self.screen = ImageGrab.grab().convert('RGBA')
        self.template = Image.open(os.path.join(image_path, target)).convert('RGBA')
        # 获取大小图宽高
        screen_width, screen_height = self.screen.size
        template_width, template_height = self.template.size
        # 获取大小图数据
        self.screen_data = self.screen.load()
        self.template_data = self.template.load()
        for y in range(screen_height - template_height):
            for x in range(screen_width - template_width):
                if self.compare(self.screen_data[x, y],
                                self.template_data[0, 0]) and \
                        self.compare(self.screen_data[x + template_width - 1, y],
                                     self.template_data[template_width - 1, 0]) and \
                        self.compare(self.screen_data[x, y + template_height - 1],
                                     self.template_data[0, template_height - 1]) and \
                        self.compare(self.screen_data[x + template_width - 1, y + template_height - 1],
                                     self.template_data[template_width - 1, template_height - 1]) and \
                        self.compare(self.screen_data[x + int(template_width / 2), y + int(template_height / 2)],
                                     self.template_data[int(template_width / 2), int(template_height / 2)]):
                    is_matched = self.check_match(x, y)
                    if is_matched:
                        pos_x = x + int(template_width / 2)
                        pos_y = y + int(template_height / 2)
                        return pos_x, pos_y
        return -1, -1

    # 定义一个全像素的匹配方法
    # def check_match(self, x, y):
    #     #     # 获取小图的宽高
    #     #     template_width, template_height = self.template.size
    #     #     # 在小图上滑动比对
    #     #     for small_y in range(template_height):
    #     #         for small_x in range(template_width):
    #     #             if not self.compare(self.screen_data[x + small_x, y + small_y],
    #     #                                 self.template_data[small_x, small_y]):
    #     #                 return False
    #     #     return True

    # 增加占比容错的匹配方法
    def check_match(self,x,y):
        same = 0
        different = 0
        template_width, template_height = self.template.size
        for small_y in range(template_height):
            for small_x in range(template_width):
                if self.compare(self.screen_data[x + small_x, y + small_y],self.template_data[small_x, small_y]):
                    same += 1
                else:
                    different += 1
        per = same/(same+different)
        if per >= 0.9:
            print(per)
            return True
        else:
            return False


    def check_exists(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1


if __name__ == '__main__':
    im = ImageMatch()
    x,y = im.find_image('python.PNG')
    print(x,y)

