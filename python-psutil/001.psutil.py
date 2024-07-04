import psutil

# CPU逻辑数量
print(psutil.cpu_count())
# CPU物理数量
print(psutil.cpu_count(logical=False))
# 统计用户/系统 空闲时间
print(psutil.cpu_times())
# CPU使用率，间隔1秒执行一次
print(psutil.cpu_percent(interval=1, percpu=True))
# 获取物理内存和交换内存
print(psutil.virtual_memory())
# 交换空间大小
print(psutil.swap_memory())

# 磁盘使用率
print(psutil.disk_usage("/"))
# 磁盘分区，磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())
# 磁盘IO
print(psutil.disk_io_counters())

# 网络读写字节和包数
print(psutil.net_io_counters())

print(psutil.net_if_stats())

# 获取网络接口信息
print(psutil.net_if_addrs())

# 获取所有的进程ID
print(psutil.pids())

# 获取进程信息
print(psutil.Process(796))

process = psutil.Process(71368)
# 获取进程名称
print(process.name())
print(process.cpu_percent())
print(process.memory_percent())
print(process.cpu_times())
# 获取进程路径
print(process.exe())
