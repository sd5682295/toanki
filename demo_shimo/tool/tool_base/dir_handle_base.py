import os
from collections import Iterator

class tool_base():
    exists = os.path.exists
    def get_file_list(self, file_type, file_path):
        pass
    def create_dir(self):
        pass
    def watch_data(self):
        pass

class dir_tool(tool_base):
    def tou_wei_handle(self, root, file):
        root = root.replace('\\', '/').replace('./.', './')
        if root.endswith('/') is False:
            root += '/'  # 处理部分root不以/结尾-----------直接+'/'

        return root + file  # 产生地址+名称的迭代器

    def get_file_list(self, file_path='./', file_type=None):
        if file_path != './' and dir_tool.exists(file_path) == False:
            return False
        tree = [(root, dirs, files) for root, dirs, files in
                os.walk(file_path, topdown=False)]  # 从path地址遍历出所有内容------遍历文件夹，将所有内容以<路径、地址、文件名>元组列的方式赋值给tree
        clear_datas = [(root, dirs, files) for root, dirs, files in tree if
                       len(files) != 0 and '\\.' not in root]  # 提取从根目录角度的文件树------路径处理'/',同时清理空目录以及内部文件
        for clear_data in clear_datas:  # 遍历出所有单个内容
            for file in clear_data[2]:
                if file_type == None:
                    yield self.tou_wei_handle(clear_data[0], file)
                elif file.endswith(file_type):  # 筛选出结尾是html的文件
                    yield self.tou_wei_handle(clear_data[0], file)
                else:
                    continue

    def create_dir(self, path, new_dir):
        if dir_tool.exists('{}{}'.format(path, new_dir)):
            print('{}{}'.format(path, new_dir))
            return '{}{}'.format(path, new_dir)
        else:
            os.mkdir('{}{}'.format(path, new_dir))
            print('{}{}'.format(path, new_dir))
            return '{}{}'.format(path, new_dir)

    def watch_data(self, data=None):
        if isinstance(data, Iterator):
            return [_ for _ in data]
        return data