class IO_base(object):
    def read_file(path, my_filter):
        pass

    def out_put(path, data):
        pass

class IO(IO_base):
    def read_file(path, my_filter=False):
        with open(path, 'r', encoding='utf-8') as f:
            f_lines = f.readlines()
        if my_filter == False:
            return [line for line in f_lines]
        else:
            return [line for line in f_lines if my_filter in line]

    def out_put(path, data):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)