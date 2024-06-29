"""追加模式"""
f = open(file="/tmp/test.txt", mode='a')
# 内容会被追加到文件尾部
f.write("hello atom")
# 文件是追加模式，不能读。
# f.readline()
f.close()
