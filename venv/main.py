import time
import math
import os
import datetime
import random
import randomconundrum as rdd


def create_result_folder(result_path):
    cdir = os.getcwd() + "\\"
    txt_dir = cdir + result_path + "\\txt\\"
    img_dir = cdir + result_path + "\\img\\"
    # 存放路径确认;
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    return txt_dir, img_dir


# 存放谜面的文件夹
result_dir = "result"
txt_dir, img_dir = create_result_folder(result_dir)

num = 5  # 生成num个谜面
# 存放谜面参数
c_size = 5

# 生成指定个数的谜面
tstart = time.time()
for i in range(num):
    # 随机颜色数量
    c_color = random.randint(3, 4)

    # 定义文件名
    filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = filename + "_" + str(c_size) + "_" + str(c_color) + "_" + str(i)
    txtfile = txt_dir + filename + ".txt"
    imgfile = img_dir + filename + ".png"

    # 随机生成谜面
    rdd.creat_conundrum((c_size, c_size), c_color, 0, 0, txtfile, imgfile)
tend = time.time()

timespan = tend - tstart
hour = math.floor(timespan / 3600)
m = math.floor((timespan - hour * 3600) / 60)
sec = math.floor(timespan - hour * 3600 - m * 60)
print("耗时:%d时%d分%d秒" % (hour, m, sec))