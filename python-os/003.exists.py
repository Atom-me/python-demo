import os

path1 = "/Users/atom/testDir/helm-test"
# 判断指定路径下的目录或者文件是否存在，存在返回True，否则返回False
if os.path.exists(path1):
    print("directory exists")
else:
    print("directory does not exist")

path2 = "/Users/atom/testDir/helm-test/aaa.txt"
# 判断指定路径下的目录或者文件是否存在，存在返回True，否则返回False
if os.path.exists(path2):
    print("file exists")
else:
    print("file does not exist")
