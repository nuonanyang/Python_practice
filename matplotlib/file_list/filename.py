from fileinput import filename
import os
from re import T
from time import time

from matplotlib.pyplot import get

import sys
import file_operation

#获取当前目录
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

    ls = file_operation.get_name(arg1)
  
    file_operation.get_message(arg1,ls)

    