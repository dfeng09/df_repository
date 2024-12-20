import os

print('df\'s name is : dingfeng')

def get_file_name(path):
    return os.path.basename(path)

path = r'D:\cs\c++ practice\test.txt'
# with open(path, 'w') as f:
#     f.write("Hello, this is a test.")
with open(path, 'r') as f:
    contents = f.read()
    print(contents)
if __name__ == '__main__':
    path = r'D:\cs\c++ practice'
    print(get_file_name(path))
    
