# encoding = utf-8
from demo2.tool.dir_handle import dir_handle
from demo2.tool.run_html import run_html

if __name__ == "__main__":
    dh = dir_handle()
    files = dh.get_html_list(type='list')
    [run_html(file).run() for file in files]

