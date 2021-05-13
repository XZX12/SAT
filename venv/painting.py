import numpy as np
import cv2
import random
import randomconundrum as rdd
color_letter = 'RGYBOC'
color_list = [(48 ,48, 255),(0, 100 ,0),(0, 255, 255),(205 ,0 ,0),(0, 165, 255),(220, 248 ,255)]
right = 0
left = 1
up = 2
down = 3
path_list = []
color_completed = []
reg = []
class rec:
    def __init__(self,p1,p2,color = (255,255,255)):
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.dir = -1
        self.dir_color = color
        # 0: '─',
        # 1: '│',
        # 2: '┘',
        # 3: '└',
        # 4: '┐',
        # 5: '┌'
    def plt(self,img,color):
        cv2.rectangle(img, self.p1, self.p2, thickness=2, color=color)
    def dir_plt(self,img):
        center = self.get_center()
        if self.dir == -1:
            pass
        elif self.dir == 0:
            cv2.line(img,(self.p1[0],center[1]),(self.p2[0],center[1]),self.dir_color,5)
        elif self.dir == 1:
            cv2.line(img, (center[0], self.p1[1]), (center[0], self.p2[1]), self.dir_color, 5)
        elif self.dir == 2:
            cv2.line(img, (self.p1[0],center[1]), center, self.dir_color, 5)
            cv2.line(img, center, (center[0], self.p1[1]), self.dir_color, 5)
        elif self.dir == 3:
            cv2.line(img, (center[0],self.p1[1]), center, self.dir_color, 5)
            cv2.line(img, center, (self.p2[0],center[1]), self.dir_color, 5)
        elif self.dir == 4:
            cv2.line(img, (self.p1[0],center[1]), center, self.dir_color, 5)
            cv2.line(img, center, (center[0],self.p2[1]), self.dir_color, 5)
        elif self.dir == 5:
            cv2.line(img, center,(center[0],self.p2[1]), self.dir_color, 5)
            cv2.line(img, center, (self.p2[0],center[1]), self.dir_color, 5)
    def coloring(self,img):
        cv2.rectangle(img,self.p1,self.p2,color=self.color, thickness=-1)
    def get_center(self):
        return (int((self.p1[0]+self.p2[0])/2),int((self.p1[1]+self.p2[1])/2))

def show(img,name='img',time = 0):
    cv2.imshow(name,img)
    cv2.waitKey(time)

def creat_blank_img(img_size):
    img = 255 - np.zeros((img_size[0],img_size[1],3),dtype=np.uint8)
    return img

def draw_line_of_rec(img,p1,p2,num1,num2):
    rec_list = []
    dis1 = int((p2[0]-p1[0])/num1)
    i = 1
    while(i<num1):
        p3 = (p1[0]+i*dis1,p1[1])
        p4 = (p1[0]+i*dis1,p2[1])
        cv2.line(img,p3,p4,color=(0,0,0),thickness=2)
        i = i+1

    dis2 = int((p2[1] - p1[1]) / num2)
    i = 1
    while (i < num2):
        p3 = (p1[0], p1[1] + i * dis2)
        p4 = (p2[0], p1[1] + i * dis2)
        cv2.line(img, p3, p4, color=(0, 0, 0), thickness=2)
        i = i+1

    for j in range(num2-1):
        for i in range(num1-1):
            p3 = (p1[0]+i*dis1,p1[1]+j*dis2)
            p4 = (p1[0]+(i+1)*dis1,p1[1]+(j+1)*dis2)
            rec_list.append(rec(p3,p4))
        p3 = (p1[0]+(i+1)*dis1,p1[1]+j*dis2)
        p4 = (p2[0],p1[1]+(j+1)*dis2)
        rec_list.append(rec(p3,p4))

    for i in range(num1 - 1):
        p3 = (p1[0]+i * dis1,p1[1]+ (j+1) * dis2)
        p4 = (p1[0]+(i + 1) * dis1, p2[1])
        rec_list.append(rec(p3, p4))
    p3 = (p1[0]+(i+1) * dis1, p1[1]+(j+1) * dis2)
    p4 = (p2[0], p2[1])
    rec_list.append(rec(p3, p4))
    return rec_list

def paint_conundrum(conundrum_size,img_size,contents,num_of_color):
    img = creat_blank_img(img_size)
    p1 = (int(0.05*img_size[0]),int(0.05*img_size[1]))
    p2 = (int(0.95*img_size[0]),int(0.95*img_size[1]))
    cv2.rectangle( img,p1,p2,thickness=2,color=(0,0,0) )
    contents = contents.replace('\n','')
    rec_list = draw_line_of_rec(img,p1,p2,conundrum_size[0],conundrum_size[1])
    color_letter_list = color_letter[0:num_of_color]
    color_list_part = color_list[0:num_of_color]
    for i in range(conundrum_size[0]*conundrum_size[1]):
        if contents[i] == '.':
            rec_list[i].coloring(img)
        if contents[i] in color_letter_list:
            index = color_letter_list.index(contents[i])
            color = color_list_part[index]
            rec_list[i].color = color
            rec_list[i].coloring(img)

    for rec in rec_list:
        rec.plt(img,(0,0,0))
    return rec_list,img

def get_dir(rec_list,pos,last_dir):
    up_valid = [1, 4, 5]
    down_valid = [1, 2, 3]
    left_valid = [0, 3, 5]
    right_valid = [0, 2, 4]
    global reg
    try:
        if last_dir == up:
            raise Exception
        if(rec_list[pos[0]+1][pos[1]].dir in down_valid):
            reg = reg  +[pos[0]+1,pos[1]]
            return down,rec_list[pos[0]+1][pos[1]]
    except (IndexError,Exception):
        pass

    try:
        if last_dir == down:
            raise Exception
        if(rec_list[pos[0]-1][pos[1]].dir in up_valid):
            if pos[0]-1<0:
                raise IndexError
            reg = reg  +[pos[0]-1,pos[1]]
            return up,rec_list[pos[0]-1][pos[1]]
    except (IndexError,Exception):
        pass

    try:
        if last_dir == right:
            raise Exception
        if(rec_list[pos[0]][pos[1]-1].dir in left_valid):
            if pos[1]-1<0:
                raise IndexError
            reg = reg  +[pos[0],pos[1]-1]
            return left,rec_list[pos[0]][pos[1]-1]
    except (IndexError,Exception):
        pass

    try:
        if last_dir == left:
            raise  Exception
        if(rec_list[pos[0]][pos[1]+1].dir in right_valid):
            reg = reg + [pos[0],pos[1]+1]

            return right,rec_list[pos[0]][pos[1]+1]

    except (IndexError,Exception):
        pass

    try:
        if rec_list[pos[0]+1][pos[1]].dir == -1 and rec_list[pos[0]+1][pos[1]].color \
                == rec_list[pos[0]][pos[1]].color:
            reg = reg + [pos[0]+1,pos[1]]
            return -1,rec_list[pos[0]+1][pos[1]]
    except IndexError:
        pass

    try:
        if rec_list[pos[0]][pos[1]+1].dir == -1 and rec_list[pos[0]][pos[1]+1].color == rec_list[pos[0]][pos[1]].color:
            reg = reg  +[pos[0], pos[1]+1]
            return -1,rec_list[pos[0]][pos[1]+1]
    except IndexError:
        pass
    try:
        if rec_list[pos[0]-1][pos[1]].dir == -1 and rec_list[pos[0]-1][pos[1]].color == rec_list[pos[0]][pos[1]].color:
            reg = reg  +[pos[0]-1, pos[1]]
            return -1,rec_list[pos[0]-1][pos[1]]
    except IndexError:
        pass

    try:
        if rec_list[pos[0]][pos[1]-1].dir == -1 and rec_list[pos[0]][pos[1]-1].color == rec_list[pos[0]][pos[1]].color:
            reg = reg  +[pos[0], pos[1] - 1]
            return -1,rec_list[pos[0]][pos[1]-1]
    except IndexError:
        pass
def get_answer(img,display_char_list,rec_list,conundrum_size):
    global reg
    global color_completed
    color_completed = []
    dict = {
     '─':0,
     '│':1,
     '┘':2,
     '└':3,
     '┐':4,
     '┌':5
    }

    special_rec = []
    for i in range(len(display_char_list)):
        try:
            display_char_list[i] = dict[display_char_list[i]]
        except KeyError:
            display_char_list[i] = -1
    for j in range(conundrum_size[0]*conundrum_size[1]):
        rec_list[j].dir = display_char_list[j]
        special_rec.append(rec_list[j])
    rec_list = np.array(rec_list).reshape((conundrum_size[0],conundrum_size[1]))


    for i in range(rec_list.shape[0]):
        for j in range(rec_list.shape[1]):
            if rec_list[i][j].dir == -1:
                rec = rec_list[i][j]
                if color_completed.count(rec.color) == 0:
                    reg = []
                    reg = reg + [i, j]
                if color_completed.count(rec.color) == 1:
                    continue
                color = rec.color
                try:
                    dir,rec = get_dir(rec_list,(i,j),-1)
                except TypeError:
                    pass
                rec.dir_color = color
                rec.color = color
                rec.dir_plt(img)
                while(rec.dir!=-1):
                    color = rec.color
                    try:
                        dir,rec = get_dir(rec_list,tuple(np.argwhere(rec_list == rec).reshape(2,)),dir)
                    except TypeError:
                        pass
                    rec.dir_color = color
                    rec.color = color
                    rec.dir_plt(img)
                color_completed.append(rec.color)
                path_list.append(reg)

def creat_text_list():
    reg = []
    global path_list

    text_list = []
    for i in range(len(path_list)):
        for j in range(int(len(path_list[i])/2)):
            reg.append(tuple( path_list[i][2*j:2*j+2]))
        text_list.append(reg)
        reg = []
    return text_list

def creat_num_list(text_list,conundrum_size):
    reg = []
    num_list = []
    for i in range(len(text_list)):
        for tup in text_list[i]:
            reg.append(tup[0]*conundrum_size[0] + tup[1])
        num_list.append(reg)
        reg = []
    return num_list

def creat_txt(conundrum_size,num_of_color,step,level,path):
    text_list = creat_text_list()
    num_list = creat_num_list(text_list,conundrum_size)
    content = str([conundrum_size[0],level,step,num_of_color]).strip('[]')+';'
    for i in range(len(num_list)):
        content += str(num_list[i]).strip('[]')
        content.strip('[]')
        content+=';'
    content = content+ '\n'
    file = open(path,'a+')
    file.write(content)