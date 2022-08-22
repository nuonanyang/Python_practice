from io import StringIO
from io import open
from optparse import Option
from selectors import SelectorKey
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


class Write_xml():
    def __init__(self,name_pre,line_number,line_up,line_next,line):
        self.name_pre = name_pre
        self.line_number = line_number
        self.line_up = line_up
        self.line_next = line_next
        self.line = line
   
       

    def create_xml(self):
        doc = Document()
        title = doc.createElement("title")
        doc.appendChild(title)
        
        # with open(self.name_pre + '.xml', 'w',encoding="utf-8") as f:
        #     # 缩进 - 换行 - 编码
        #     doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
        with open(self.name_pre , 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')

    @staticmethod
    def creat_nodes(dom,r_node,n_1,name):
        lineup = dom.createElement(name)
        name_text_value = dom.createTextNode(n_1)
        lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
        r_node.appendChild(lineup)

    def append_XML(self):
        # domTree = parse(self.name_pre + '.xml')
        domTree = parse(self.name_pre)
        # 文档根元素
        rootNode = domTree.documentElement

        # 新建一个customer节点
        customer_node = domTree.createElement("frame")
        customer_node.setAttribute("ID", str(self.line_number))

        
        self.creat_nodes(domTree,customer_node,self.line,"line")


        rootNode.appendChild(customer_node)
        print("1234567890")
        # with open(self.name_pre + '.xml', 'w',encoding="utf-8") as f:
        with open(self.name_pre, 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
            # f.write(domTree.toprettyxml(indent="  "))



class Up_line(Write_xml):
    def append_XML(self):
        domTree = parse(self.name_pre )
        # 文档根元素
        rootNode = domTree.documentElement

        # 新建一个customer节点
        customer_node = domTree.createElement("frame")
        customer_node.setAttribute("ID", str(self.line_number))

        self.creat_nodes(domTree,customer_node,self.line_up,"line_up")
        
        self.creat_nodes(domTree,customer_node,self.line,"line")


        rootNode.appendChild(customer_node)
        print("1234567890")
        with open(self.name_pre, 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
            # f.write(domTree.toprettyxml(indent="  "))

class Up_next_line(Write_xml):
    def append_XML(self):
        domTree = parse(self.name_pre )
        # 文档根元素
        rootNode = domTree.documentElement

        # 新建一个customer节点
        customer_node = domTree.createElement("frame")
        customer_node.setAttribute("ID", str(self.line_number))

        self.creat_nodes(domTree,customer_node,self.line_up,"line_up") 
        self.creat_nodes(domTree,customer_node,self.line,"line")
        self.creat_nodes(domTree,customer_node,self.line_next,"line_next")

        rootNode.appendChild(customer_node)
        print("1234567890")
        with open(self.name_pre , 'w',encoding="utf-8") as f:
            # 缩进 - 换行 - 编码
            domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
            # f.write(domTree.toprettyxml(indent="  "))
    
