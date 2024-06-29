f = open(file="/tmp/test.txt", mode='r')

# 读一行
print(f.readline())
data = f.read(5)
print(data)
f.close()
