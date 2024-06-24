"""
os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出 OSError。
该方法与 unlink() 相同。在Unix, Windows中有效
直接删除文件，不经过回收站

语法
remove()方法语法格式如下：


os.remove(path)

参数
path -- 要移除的文件路径
"""
import os


os.remove("../python-requests/baidu.html")

