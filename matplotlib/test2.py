from xml import dom
import xml.dom.minidom as xdc
from xml.dom.minidom import Document
from xml.etree import ElementTree as ET
from xml.dom.minidom import parse

from pyparsing import line


def creat_nodes(dom,r_node,n_1,name):
    lineup = dom.createElement(name)
    name_text_value = dom.createTextNode(n_1)
    lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
    r_node.appendChild(lineup)


# def c_nodes(dom,r_node,n_1,name):
#     lineup = dom.createElement(name)
#     name_text_value = dom.createTextNode(n_1)
#     lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
#     r_node.appendChild(lineup)

def append_XML(name_pre,i,n_1,n_11,n):
    domTree = parse(name_pre + '.xml')
	# 文档根元素
    rootNode = domTree.documentElement

	# 新建一个customer节点
    customer_node = domTree.createElement("frame")
    customer_node.setAttribute("ID", str(i))

    creat_nodes(domTree,customer_node,n_1,"line_up")
    creat_nodes(domTree,customer_node,n_11,"line_next")
    creat_nodes(domTree,customer_node,n,"line")

    # 创建name节点,并设置textValue
    # lineup = domTree.createElement("line_up")
    # name_text_value = domTree.createTextNode(n_1)
    # lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
    # customer_node.appendChild(lineup)

    # test_line = domTree.createElement("test_line")
    # test_text_value = domTree.createTextNode("test_line")
    # test_line.appendChild(test_text_value)  # 把文本节点挂到name_node节点
    # lineup.appendChild(test_line)

    # # 创建phone节点,并设置textValue
    # nextline = domTree.createElement("next_line")
    # phone_text_value = domTree.createTextNode(n_11)
    # nextline.appendChild(phone_text_value)  # 把文本节点挂到name_node节点
    # customer_node.appendChild(nextline)

    # # 创建comments节点
    # line = domTree.createElement("line")
    # cdata_text_value = domTree.createTextNode(n)
    # line.appendChild(cdata_text_value)
    # customer_node.appendChild(line)


    rootNode.appendChild(customer_node)
    print("1234567890")
    with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', newl='\n',encoding='utf-8')
        # f.write(domTree.toprettyxml(indent="  "))
    

if __name__ == '__main__':
    append_XML("看到家2",23,"shangyihang","xiayihang","benhang")



