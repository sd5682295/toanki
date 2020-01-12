import os


class dir_handle(object):
    exists = os.path.exists

    def __init__(self):
        self.path_dir = ['html', 'csv']
        created_dir = [dir_handle.create_dir(_) for _ in self.path_dir]
        self.html_root = './html/'
        self.html_list = dir_handle.__get_html_list(self.html_root)

    #         print('==========', [_ for _ in self.html_list])

    @classmethod
    def create_dir(cls, data):
        print('开始')
        if cls.exists(data):
            print('{}已经存在'.format(data))
            return '{}已经存在'.format(data)
        else:
            os.mkdir('./{}'.format(data))
            print('{}不存在'.format(data))
            return '{}不存在'.format(data)

    @classmethod
    def __get_html_list(cls, dir):
        tree = [(root, dirs, files) for root, dirs, files in os.walk(dir, topdown=False)]
        clear_datas = [(root.replace('\\', '/'), dirs, files) for root, dirs, files in tree if
                       len(files) != 0 and '\\.' not in root]
        for clear_data in clear_datas:
            for file in clear_data[2]:
                if file.endswith('.html'):
                    cls.my_root = clear_data[0]
                    if cls.my_root.startswith('./') is False:
                        cls.my_root = ('./' + cls.my_root).replace('./.', './')
                    if cls.my_root.endswith('/') is False:
                        cls.my_root += '/'
                    yield cls.my_root + file
                else:
                    continue

    def get_html_list(self, html=False, type='iterable_object'):
        if html is not False:
            self.html_list = dir_handle.__get_html_list(html)
        else:
            self.html_list = dir_handle.__get_html_list(self.html_root)
        if type is 'list':
            return [_ for _ in self.html_list]
        return self.html_list


if __name__ == "__main__":
    dd = dir_handle()
    print(dd.get_html_list(html='.', type='list'))
