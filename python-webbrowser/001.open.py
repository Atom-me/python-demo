# webbrowser 是Python语言里一个内置的模块，该模块提供了一些高级接口，使你可以调用计算机中的浏览器以打开基于WEB的文档，比如常见的html网页；

"""
该模块定义了以下函数：

webbrowser.open(url,new=0,autoraise=True)

使用系统中默认的浏览器打开URL，
如果new为0，则尽可能在同一浏览器窗口中打开url，
如果new为1，则尽可能打开新的浏览器窗口，
如果new为2，则尽可能打开新的浏览器标签；
如果autoraise为true，则会尽可能将窗口置前。

大多数情况下，只需要从webbrowser模块中调用此函数即可。
"""

import webbrowser

url = "https://www.baidu.com"
webbrowser.open(url)
