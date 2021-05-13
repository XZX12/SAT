import pyflowsolver as pfs
import randomconundrum as rdd
import painting as pt

def creat_txt(path,conundrum_size,num_of_color):
    file = open(path,'a+')
    file.write(str(conundrum_size[0],'0','0',str(num_of_color)))
