# 要在 Python 中处理文件，你必须先打开文件。因此，open() 函数正如其名称所暗示的那样:它为你打开一个文件，以便你可以使用该文件。
# 要使用 open() 函数，首先要为其声明一个变量。 open() 函数最多需要 3 个参数——文件名、模式和编码。然后，你可以在 print 函数中指定要对文件执行的操作。
from os.path import expanduser, join

# 用os.path.expanduser 模块获取主目录
home_directory = expanduser("~")

hcloud_config_directory = join(home_directory, ".hcloud/config.json")

hcloud_config = open(hcloud_config_directory, 'r')

print(hcloud_config.read())

# open() 函数不会关闭文件，因此你还必须使用 close() 方法关闭文件。
hcloud_config.close()
