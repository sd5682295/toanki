from demo_shimo.tool.run_html import run_md
from tool.dir_handle import dir_handle

from demo2.tool.tool_base.dir_handle_base import dir_tool


class dir_handle(dir_tool):
    def __init__(self):
        self.path_dir = ['md', 'anki_txt']
        self.html_root = '../md/'
        self.file_typle = 'md'

    def get_file_typle(self):
        return self.file_typle

    def get_html_iter(self):
        return self.__get_html_iter()

    def create_html_anki_txt(self):
        return self.__create_html_anki_txt()

    def __get_html_iter(self):
        return self.get_file_list(self.html_root, self.file_typle)

    def __create_html_anki_txt(self):
        for i in self.path_dir:
            self.create_dir('',i)

class qa():
   pass

if __name__ == "__main__":
    dh = dir_handle()
    files = dh.get_html_iter()
    [run_md(file).run() for file in files]