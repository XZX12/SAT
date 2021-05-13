import random
import pyflowsolver as pfs
import itertools
import time
import painting as pt
import cv2

class conundrum:
    def __init__(self,size = (5,5),num_of_color = 5):
        self.size = size
        self.num_of_color = num_of_color
        self.coordinate_list = []
        self.color_list = 'RGYBOCEFJHI'

    def creat_random_conundrum(self):
        random_list = list(itertools.product(range(0,self.size[0]), range(0,self.size[1])))
        self.coordinate_list = random.sample(random_list, self.num_of_color*2)

        temp_index = 0
        content = ''
        file = open('puzzles/Test.txt','a+')
        file.truncate(0)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if (i,j) not in self.coordinate_list:
                    content += '.'
                else:
                    if temp_index < self.num_of_color:
                        content += self.color_list[temp_index]
                    else:
                        content += self.color_list[temp_index-self.num_of_color]
                    temp_index += 1
            content += '\n'
        file.write(content)
        return content

def creat_valid_random_conundrum(size,num_of_color):
    contents_list = []
    conund = conundrum(size,num_of_color)
    is_valid = False
    while(not is_valid):
        contents = conund.creat_random_conundrum()
        if contents in contents_list:
            continue
        files = ['puzzles/Test.txt']
        is_valid = pfs.pyflow_solver_main(files)
    return contents

def creat_conundrum(conundrum_size,num_of_color,step,level,path,img_path):
    '''
    :param conundrum_size: 谜面大小
    :param num_of_color:颜色数
    :param step: 阶段
    :param level:关卡
    :param path: txt文档存储的位置

    '''
    contents = creat_valid_random_conundrum(conundrum_size,num_of_color)
    rec_list, img = pt.paint_conundrum(conundrum_size, (512, 512), contents, num_of_color)
    pt.get_answer(img, pfs.display_char_list, rec_list, conundrum_size)
    pt.creat_txt(conundrum_size,num_of_color,step,level,path)
    cv2.imwrite(img_path, img)

if __name__ == '__main__':
    conundrum_size = (5,5)
    num_of_color = 4
    step = level = 0
    path = r'firstStep\test1.txt'
    creat_conundrum(conundrum_size,num_of_color,step,level,path)
    print(0)

