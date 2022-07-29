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
from write_xml_class import Write_xml


class Get_pdf():
    def __init__(self,all_path,find_con):
        self.all_path = all_path
        self.find_con = find_con
        self.wx = Write_xml()
    
    def get_pdf_name(self):
        name_f = self.all_path.split("\\")[-1].split(".")[0]
        print(name_f) 
        return(name_f)

    

    def read_pdf(self,pdf,find_con):
        # resource manager 创建pdf资源管理器，来管理共享资源
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        #创建一个pdf设备对象
        laparams = LAParams()
        # device
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device, pdf)
        device.close()
        content = retstr.getvalue()
        # print("content+ " + content)
        retstr.close()
        # 获取所有行
        lines = str(content).split("\n")
        # print("line967+ " + lines[969])
        name_p = self.get_pdf_name()
        create_xml(name_p)
        # n = 0
        for i in range(len(lines)):
            # print("line + " + line)
        
            if find_con in lines[i]:
                print("n-1 :" + lines[i-1])
                print("n+1 :" + lines[i+1])
                print(lines[i])
                print("**************************************************************")
                append_XML(name_p,i,lines[i-1],lines[i+1],lines[i])
            


