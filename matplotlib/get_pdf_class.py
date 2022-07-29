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


class Get_pdf():
    def __init__(self,all_path,content):
        self.all_path = all_path

    
    def get_pdf_name(self):
        name_f = self.all_path.split("\\")[-1].split(".")[0]
        print(name_f) 
        return(name_f)

    def create_xml(name_pre):
        doc = Document()
        title = doc.createElement("title")
        doc.appendChild(title)
        
        with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')

    def creat_nodes(dom,r_node,n_1,name):
        lineup = dom.createElement(name)
        name_text_value = dom.createTextNode(n_1)
        lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
        r_node.appendChild(lineup)

    def append_XML(name_pre,i,n_1,n_11,n):
        domTree = parse(name_pre + '.xml')
        # 文档根元素
        rootNode = domTree.documentElement

        # 新建一个customer节点
        customer_node = domTree.createElement("frame")
        customer_node.setAttribute("ID", str(i))

        Get_pdf.creat_nodes(domTree,customer_node,n_1,"line_up")
        Get_pdf.creat_nodes(domTree,customer_node,n_11,"line_next")
        Get_pdf.creat_nodes(domTree,customer_node,n,"line")


        rootNode.appendChild(customer_node)
        print("1234567890")
        with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
            # f.write(domTree.toprettyxml(indent="  "))

        


