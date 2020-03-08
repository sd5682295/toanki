# encoding = utf-8
from demo_shimo.tool.qa import dir_handle
from demo_shimo.tool.run_html import run_md


if __name__ == "__main__":
    dh = dir_handle()
    print(dh.watch_data(dh.get_html_iter()))
    # [run_md(file).run() for file in files]

