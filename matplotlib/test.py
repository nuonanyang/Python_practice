from platform import python_branch
import sys

def add(a, b):
    print(float(a)+float(b))

if __name__ == '__main__':
	arg1, arg2 = sys.argv[1], sys.argv[2]   # 接收位置参数
	add(arg1, arg2)

print("s")    
print(arg1)