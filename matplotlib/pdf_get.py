from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import sys
from xml.dom.minidom import Document
import os
import append_to_xml
# test.append_XML("看到家",25,"shangyihang","xiayihang","benhang")

def get_pdf_name(path):
    name_f = path.split("\\")[-1].split(".")[0]
    print(name_f) 
    return(name_f)
    

def create_xml(name_pre):
    doc = Document()
    title = doc.createElement("title")
    doc.appendChild(title)

    
    # frame = doc.createElement("frame")
    # title.appendChild(frame)
    # frame.setAttribute("ID", str(i))

    # line_up = doc.createElement("line_up")
    # frame.appendChild(line_up)
    # personname = doc.createTextNode(n_1)
    # line_up.appendChild(personname)

    # next_line = doc.createElement("next_line")
    # frame.appendChild(next_line)
    # personname = doc.createTextNode(n_11)
    # next_line.appendChild(personname)

    # line = doc.createElement("line")
    # frame.appendChild(line)
    # personname = doc.createTextNode(n)
    # line.appendChild(personname)

    # filename = name_pre + ".xml"
    # f = open(filename, "w+",encoding="utf-8")
    # f.write(doc.toprettyxml(indent="  "))
    # f.close()

    with open(name_pre + '.xml', 'w',encoding="utf-8") as f:
        # 缩进 - 换行 - 编码
        doc.writexml(f, addindent='  ', newl='\n',encoding='utf-8')


 
def read_pdf(pdf,name_p,find_con):
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
    text = open('words.txt', 'a+',encoding="utf-8")
    create_xml(name_p)
    # n = 0
    for i in range(len(lines)):
        # print("line + " + line)
       
        if find_con in lines[i]:
            print("n-1 :" + lines[i-1])
            print("n+1 :" + lines[i+1])
            print(lines[i])
            print("**************************************************************")
            # write_to_xml(name_p,i,lines[i-1],lines[i+1],lines[i])
            # if os.path.exists("F:\program\Python_practice\matplotlib\\看到家.xml"):
            append_to_xml.append_XML(name_p,i,lines[i-1],lines[i+1],lines[i])
                # test.append_XML("看到家",21,"shangyihang","xiayihang","benhang")
            # else:
            #     write_to_xml(name_p,i,lines[i-1],lines[i+1],lines[i])
            text.writelines(lines[i]+'\n')
   

    text.close()
 

 
def run(all_path,content):
    #以二进制读模式打开
    my_pdf = open(all_path, "rb")
    name_pre = get_pdf_name(all_path)
    read_pdf(my_pdf,name_pre,content)
    my_pdf.close()


    
 
if __name__ == '__main__':

    if len(sys.argv) >= 2:
        # global arg1
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1,str(arg2))
    # write_to_xml("看到家",21,"shangyihang","xiayihang","benhang")
    # test.append_XML("看到家",23,"shangyihang","xiayihang","benhang")
    run(arg1,arg2)
   

 
    