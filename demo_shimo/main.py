from demo_shimo.tool.dir_handle import dir_handle
from demo_shimo.tool.run_html import run_md

if __name__ == "__main__":
    dh = dir_handle()
    files = dh.get_html_iter()
    [run_md(file).run() for file in files]