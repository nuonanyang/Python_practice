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

class Write_xml():
    def __init__(self,name_pre):
        self.name_pre = name_pre

    def create_xml(self):
        doc = Document()
        title = doc.createElement("title")
        doc.appendChild(title)
        
        with open(self.name_pre + '.xml', 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')

    def creat_nodes(dom,r_node,n_1,name):
        lineup = dom.createElement(name)
        name_text_value = dom.createTextNode(n_1)
        lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
        r_node.appendChild(lineup)

    def append_XML(self,i,n_1,n_11,n):
        domTree = parse(self.name_pre + '.xml')
        # 文档根元素
        rootNode = domTree.documentElement

        # 新建一个customer节点
        customer_node = domTree.createElement("frame")
        customer_node.setAttribute("ID", str(i))

        self.creat_nodes(domTree,customer_node,n_1,"line_up")
        self.creat_nodes(domTree,customer_node,n_11,"line_next")
        self.creat_nodes(domTree,customer_node,n,"line")


        rootNode.appendChild(customer_node)
        print("1234567890")
        with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
            # f.write(domTree.toprettyxml(indent="  "))






def run(gp,all_path,content):
    #以二进制读模式打开
    my_pdf = open(all_path, "rb")
    name_pre = gp.get_pdf_name(all_path)
    read_pdf(gp,my_pdf,name_pre,content)
    my_pdf.close()


    
 
if __name__ == '__main__':

    if len(sys.argv) >= 2:
        # global arg1
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1,str(arg2))
    gp = Get_pdf(arg1)
    run(gp,arg1,arg2)
   