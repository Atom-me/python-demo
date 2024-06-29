"""
 自动创建文件
"""
f = open(file="/tmp/test.txt", mode='w')

f.write("atom devopler 50\n")
f.write("amily producter 60\n")

f.close()
