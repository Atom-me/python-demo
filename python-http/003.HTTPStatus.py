from http import HTTPStatus

"""
HTTPStatus,它是标准库的一部分，你可以在任何项目中使用它。
它有更多的数据：每个状态代码都有其原因短语和描述。
作为一个枚举，它是一个独立的类型，int ，这对于比较、调试和类型检查很有用。
"""

print(HTTPStatus(200))
print(HTTPStatus.OK)
