from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import sys
from xml.dom.minidom import Document
from xml import dom
import xml.dom.minidom as xdc
from xml.dom.minidom import Document
from xml.etree import ElementTree as ET
from xml.dom.minidom import parse

from pyparsing import line
import os
from append_to_xml import Write_xml

from gettext import find
import sys, getopt


class Get_pdf():
    def __init__(self,all_path,output_file,find_con,option):
        self.all_path = all_path
        self.output_file = output_file
        self.find_con = find_con
        self.option = option
        self.pdf = open(all_path, "rb")
    
    def get_pdf_name(self):
        name_f = self.all_path.split("\\")[-1].split(".")[0]
        print(name_f) 
        return(name_f)

    

    def read_pdf(self):
        # resource manager 创建pdf资源管理器，来管理共享资源
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        #创建一个pdf设备对象
        laparams = LAParams()
        # device
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device,self.pdf)
        device.close()
        content = retstr.getvalue()
        # print("content+ " + content)
        retstr.close()
        # 获取所有行
        lines = str(content).split("\n")
        # print("line967+ " + lines[969])
        name_p = self.get_pdf_name()
        
        # n = 0
        for i in range(len(lines)):
            # print("line + " + line)
        
            if self.find_con in lines[i]:
                print("n-1 :" + lines[i-1])
                print("n+1 :" + lines[i+1])
                print(lines[i])
                print("**************************************************************")
                wx = Write_xml(name_p,i,lines[i-1],lines[i+1],lines[i],self.output_file,self.option)         
                sl = self.all_path .split(".")[0]
                if os.path.exists(sl + ".xml"):
                    wx.append_XML()
                else:
                    wx.create_xml()
                
        self.pdf.close()


def get_arg(argv):
    inputfile = ''
    outputfile = ''
    find_con = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","find_c="])
    except getopt.GetoptError:
        # print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            # print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-f", "--find_c"):
            find_con = arg
    
    print ('输入的文件为：', inputfile)
    print ('输出的文件为：', outputfile)
    print ('查找的内容为：', find_con)
    if outputfile == '':
        print("find_con is null")
    return inputfile,outputfile,find_con

def get_option():
    print("please enter your choice:\n",\
        "1:the line\n",\
        "2:three line\n",\
        "3:line up and the line")
    num = input()
    return num    
            

if __name__ == '__main__':
    in_file,out_file,find_c = get_arg(sys.argv[1:])
    print("*****************") 
    print(in_file,out_file,find_c)
    print("*****************") 
    option = get_option()
    # if len(sys.argv) >= 2:
    #     # global arg1
    #     arg1 = sys.argv[1]
    #     arg2 = sys.argv[2]
    #     print(arg1,str(arg2))
    gp = Get_pdf(in_file,out_file,find_c,option)
    gp.read_pdf()



