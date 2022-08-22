
from gettext import find
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    find_con = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","find_c="])
    except getopt.GetoptError:
        # print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    print(args)
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
    if find_con == '':
        print("find_con is null")

if __name__ == "__main__":
    main(sys.argv[1:]) 