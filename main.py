# encoding = utf-8
from tool.dir_handle import dir_handle
from tool.run_html import run_html

if __name__ == "__main__":
    dh = dir_handle()
    files = dh.get_html_list(type='list')
    [run_html(file).run() for file in files]

