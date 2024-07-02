import logging

print(logging.NOTSET)
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)

# 也可以用對應數值來查詢是哪個等級的訊息，可使用
print(logging.getLevelName(0))  # 輸出為：NOTSET
print(logging.getLevelName(10))  # 輸出為：DEBUG
print(logging.getLevelName(20))  # 輸出為：INFO
print(logging.getLevelName(30))  # 輸出為：WARNING
print(logging.getLevelName(40))  # 輸出為：ERROR
print(logging.getLevelName(50))  # 輸出為：CRITICAL
