import sys
class Father(object):
    def __init__(self, name):
        self.name=name
        # print ( "name: %s" %( self.name) )
    def getName(self):
        return 'Father ' + self.name
 
class Son(Father):
    def getName(self):
        return 'Son '+self.name
 
if __name__=='__main__':
#     son=Son('runoob')
#     print ( son.getName() )
    arg1 = sys.argv[1]
    if arg1 == "1":
        opt = Son
    elif arg1 == "2":
        opt = Father
        
    s = opt("runoob")
    print(s.getName())