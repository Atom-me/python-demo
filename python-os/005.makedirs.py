import os

path1 = os.getcwd() + "/aaa/bbb/ccc"

# 递归创建文件夹，自动创建父目录， 如果文件夹已经存在，同样会报错
os.makedirs(path1)
