import os
from os import listdir
from os import path
import codecs

def check(file_path):
    f = codecs.open(file_path, encoding='utf-8')
    line_list = []

    for line in f:
        line_list.append(line)
    has_error = 0
    if(len(line_list) < 30):
        for i in range(0,len(line_list)):
            if(len(line_list[i]) > 9):
                if(line_list[i][0:9] == "    (file"):
                    return "error"
    else:
        for i in range(-30,0):
            if(len(line_list[i]) > 9):
                if(line_list[i][0:9] == "    (file"):
                    return "error"
                

    if(not has_error):
        if(line_list[-2][-2] == "S"):
            return "pass"
        elif(line_list[-2][-2] == "L"):
            return "fail"
        else:
            return "strange"

        