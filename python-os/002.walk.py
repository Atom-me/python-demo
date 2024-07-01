import os

# walk() 方法， 传入任意一个path路径，深层次遍历指定路径下的所有子文件夹，返回一个由路径、文件夹列表、文件列表组成的元组。
specified_folder = os.walk("/Users/atom/testDir/helm-test")
for path, dirs, files in specified_folder:
    print(path)
    print(dirs)
    print(files)
    print("\n")
