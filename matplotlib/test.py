from matplotlib.pyplot import get


def my_func():
    lis = []
    dic = dict()
    res = lis + ['get', 'func', 'vars']
    words = "Life is short, You need Python!"
    print(words)
 
 
def creat_nodes(dom,r_node,n_1,name):
    lineup = dom.createElement(name)
    name_text_value = dom.createTextNode(n_1)
    lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
    r_node.appendChild(lineup)
    return lineup

 
def get_func_varnames(func):
    func_vars = func.__code__.co_varnames
    print(func_vars[4])
 
 
# if __name__ == "__main__":
get_func_varnames(creat_nodes)

def c_nodes(dom,r_node,n_1,name):
    fnode_name = creat_nodes()
    
    lineup = dom.createElement(name)
    name_text_value = dom.createTextNode(n_1)
    lineup.appendChild(name_text_value)  # 把文本节点挂到name_node节点
    fnode_name.appendChild(lineup)