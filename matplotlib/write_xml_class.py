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
from get_pdf_class import Get_pdf


def append_XML(gp,name_pre,i,n_1,n_11,n):
    domTree = parse(name_pre + '.xml')
    # 文档根元素
    rootNode = domTree.documentElement

    # 新建一个customer节点
    customer_node = domTree.createElement("frame")
    customer_node.setAttribute("ID", str(i))

    gp.creat_nodes(domTree,customer_node,n_1,"line_up")
    gp.creat_nodes(domTree,customer_node,n_11,"line_next")
    gp.creat_nodes(domTree,customer_node,n,"line")


    rootNode.appendChild(customer_node)
    print("1234567890")
    with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
        # f.write(domTree.toprettyxml(indent="  "))

def read_pdf(gp,pdf,name_p,find_con):
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
    
    gp.create_xml(name_p)
    # n = 0
    for i in range(len(lines)):
        # print("line + " + line)
    
        if find_con in lines[i]:
            print("n-1 :" + lines[i-1])
            print("n+1 :" + lines[i+1])
            print(lines[i])
            print("**************************************************************")
            append_XML(name_p,i,lines[i-1],lines[i+1],lines[i])

def run(gp,all_path,content):
    #以二进制读模式打开
    my_pdf = open(all_path, "rb")
    name_pre = gp.get_pdf_name(all_path)
    read_pdf(my_pdf,name_pre,content)
    my_pdf.close()


    
 
if __name__ == '__main__':

    if len(sys.argv) >= 2:
        # global arg1
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1,str(arg2))
    gp = Get_pdf(arg1)
    run(gp,arg1,arg2)
   