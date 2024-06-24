# 要在 Python 中处理文件，你必须先打开文件。因此，open() 函数正如其名称所暗示的那样:它为你打开一个文件，以便你可以使用该文件。
# 要使用 open() 函数，首先要为其声明一个变量。 open() 函数最多需要 3 个参数——文件名、模式和编码。然后，你可以在 print 函数中指定要对文件执行的操作。
from os.path import expanduser, join

# 用os.path.expanduser 模块获取主目录
home_directory = expanduser("~")

hcloud_config_directory = join(home_directory, ".hcloud/config.json")

# with 语句会在你不告诉它的情况下为你关闭文件。这是因为 with 语句在后台调用了 2 个内置方法: __enter()__ 和 __exit()__。
# __exit()__ 方法在你指定的操作完成后关闭文件。
with open(hcloud_config_directory, 'r') as hcloud_config:
    print(hcloud_config.read())

# 建议你使用 with 和 open() 的组合，因为 with 语句会为你关闭文件，并且你可以编写更少的代码。
