import os
from fileinput import filename
import os
from re import T
from time import time

from matplotlib.pyplot import get

import sys


class Get_flie():
    def __init__(self,file_path):
        self.file_path = file_path

    #获取目录下文件
    @staticmethod
    def get_name(ab_path):
        ls = os.listdir(ab_path)
        return ls

    #时间戳转换
    @staticmethod
    def formatTime(atime):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(atime))

    #获取文件属性
    @staticmethod
    def get_charact(filename):
        statinfo = os.stat(filename)   
        size = statinfo.st_size
        l_atime = Get_flie.formatTime(statinfo.st_atime)
        l_mtime = Get_flie.formatTime(statinfo.st_mtime)
        l_ctime = Get_flie.formatTime(statinfo.st_ctime)
        print("大小：" + str(size) + " 创建时间："+ l_ctime + " 最后一次修改时间：" + l_atime + " 上次访问时间：" + l_mtime,)

    #获取绝对路径
    @staticmethod
    def get_path(path,filename):
        abso_path = path + "\\" + filename 
        return abso_path



    def get_message(paths,lss):
        for name in lss:
            print(name)       
            abso = get_path(paths,name)
            print(abso)
            get_charact(abso)
            if os.path.isdir(abso):
                print ("it's a directory")
                file_name = get_name(abso)
                print(file_name)
                # pth = get_path(,name)
                # print(pth)
                get_message(abso,file_name)
            elif os.path.isfile(name):
                print ("it's a normal file")
            else:
                print ("it's a special file(socket,FIFO,device file)")


arg1 = os.getcwd()
if __name__ == '__main__':
    # arg1= sys.argv[1]

    # # cur_path = "F:\\program\\Python_practice\\test"
    # cur_path = arg1
    #if _name_ == “main”：下，全局变量是一直保持的
    if len(sys.argv) >= 2:
        # global arg1
        arg1= sys.argv[1]
    
    print(arg1)

    # ls = file_operation.get_name(arg1)
  
    # file_operation.get_message(arg1)
    gm = Get_flie(arg1)
    gm.get_message()