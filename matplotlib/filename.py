from fileinput import filename
import os
from re import T
from time import time

from matplotlib.pyplot import get

import sys

#获取当前目录
cur_path = os.getcwd()
if __name__ == '__main__':
    arg1= sys.argv[1]

    # cur_path = "F:\\program\\Python_practice\\test"
    cur_path = arg1
    print(cur_path)

    #获取目录下文件
    def get_name(filepath):
        ls = os.listdir(filepath)
        return ls



    #时间戳转换
    def formatTime(atime):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(atime))

    #获取文件属性
    def get_charact(filename):
        statinfo = os.stat(filename)   
        size = statinfo.st_size
        l_atime = formatTime(statinfo.st_atime)
        l_mtime = formatTime(statinfo.st_mtime)
        l_ctime = formatTime(statinfo.st_ctime)
        print("大小：" + str(size) + " 创建时间："+ l_ctime + " 最后一次修改时间：" + l_atime + " 上次访问时间：" + l_mtime,)


    ls = get_name(cur_path)
    # print("最后一次访问时间:",formatTime(statinfo.st_atime))

    #获取绝对路径
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


    get_message(cur_path,ls)