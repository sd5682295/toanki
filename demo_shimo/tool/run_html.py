# from lxml import html

# from demo2.tool.qa import qa
from demo_shimo.tool.IO_Handle import IO
# from tool.dir_handle import dir_handle


class run_md(object):
    def __init__(self, ihtml):
        self.html = ihtml
        # dh = dir_handle()
        self.file_name = self.html.strip('./{}/'.format('md')).replace('.md','')
    def run(self):
        datas = IO.read_file(self.html, my_filter="=>")
        datas = [data.split("=>") for data in datas]
        data_str = ""
        for data in datas:
            my_data = '<p>[{}]{}</p>\t{}\n'.format(self.file_name,data[0],data[1])
            data_str += my_data
        IO.out_put('./anki_txt/{}.txt'.format(self.file_name), data_str)

if __name__ == "__main__":

    rh = run_md('../md/Django 如何处理一个请求.md')
    rh.run()