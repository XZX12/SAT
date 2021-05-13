import random
import randomconundrum as rdd
import numpy as np

# right = 0
# left = 1
# up = 2
# down = 3
covered_list = []#已经被有线段经过的位置

def creat_non_covered_list(array_size):
    non_covered_list = []
    global covered_list
    for i in range(array_size[0]):
        for j in range(array_size[1]):
            if not((i,j) in covered_list):
                non_covered_list.append((i,j))
    return non_covered_list
def valid_pos_connected(array_size,pos):#周围未被cover的点集
    non_covered_list = creat_non_covered_list(array_size)
    connected_point_list = connected_point(pos)
    result = [pos for pos in non_covered_list if pos in connected_point_list]
    return result
def calc_qi(array_size,pos):
    return len(valid_pos_connected(array_size,pos))
def connected_point(pos):
    return [
        (pos[0],pos[1]+1),
        (pos[0], pos[1] - 1),
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1])
    ]
def is_covered(array_size):
    '''
    用于判断数组是否已经被填满。有0表示没有被填满
    :param array: 数组
    :return: 是否
    '''
    result = creat_non_covered_list(array_size)
    if len(result) == 0:
        return True
    else:
        return False
# def is_pos_valid(array_size,pos):
#     global covered_list
#     is_valid1 = not (pos[0] >= array_size[0] or pos[0] < 0 or pos[1] >= array_size[1] or pos[1] < 0)
#     is_valid2 = not (pos in covered_list)
#
#     is_valid = is_valid1 and is_valid2
#     return is_valid
def find_next_point(array_size,pos):
    global covered_list
    valid_next_point_list = valid_pos_connected(array_size,pos)
    for temp_pos in valid_next_point_list:
        qi = calc_qi(array_size,temp_pos)
        if  qi== 0 or qi == 1:
            covered_list.append(temp_pos)
            return temp_pos
    try:
        temp_pos = random.sample(valid_next_point_list,1)[0]
    except ValueError:
        pass
    covered_list.append(temp_pos)
    return temp_pos
def creat_line(array_size):
    global covered_list
    line_list = []
    is_end = False
    is_valid = False
    while(not is_valid):
        pos = random.sample(creat_non_covered_list(array_size),1)[0]
        covered_list.append(pos)
        for temp_pos in valid_pos_connected(array_size,pos):
            if calc_qi(array_size,temp_pos)==0:
                is_valid = False
        is_valid = True
        covered_list.remove(pos)
    covered_list.append(pos)
    line_list.append(pos)
    while(not is_end):
        pos = find_next_point(array_size,pos)
        line_list.append(pos)
        is_end = True
        if len(line_list)<=2:
            is_end = False
        if calc_qi(array_size,pos) == 0:
            is_end = True
    return line_list
def is_finish(array_size):
    global covered_list
    non_list = creat_non_covered_list(array_size)
    single_pos = []
    for pos in non_list:
        if calc_qi(array_size,pos) == 0:
            single_pos.append(pos)
    if len(single_pos) == 0:
        return False
    else:
        return True

def creat_conundrum(array_size):
    line_list = [[]]
    while(not is_covered(array_size)):
        line_list += [creat_line(array_size)]
        if is_finish(array_size):
            non_list = creat_non_covered_list(array_size)
            for pos in non_list:
                connected_point_list = connected_point(pos)
                for i in range(1,len(line_list)):
                    if line_list[i][0] in connected_point_list:
                        line_list[i].insert(0,pos)
                        covered_list.append(pos)
                        break
                    if line_list[i][-1] in connected_point_list:
                        line_list[i].append(pos)
                        covered_list.append(pos)
                        break
    line_list.remove([])

    return line_list

stop = 0
while(not stop):
    stop = 1
    try:
        line_list = creat_conundrum((10,10))
    except Exception:
        continue
    for i in range(len(line_list)):
        if len(line_list[i])<=2:
            stop = 0
            break



print(0)