import os

os.getcwd()
path1 = os.getcwd() + "/bbb_dir"

# 创建单层文件夹，如果文件夹已经存在，就会报错，因此创建文件夹之前，最好使用os.path.exists(path) 判断文件夹是否存在
os.mkdir(path1)
