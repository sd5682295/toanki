from lxml import html

from tool.qa import qa


class run_html(object):
    def __init__(self, ihtml, color_tag='"#3da8f5"', out_path='./anki_txt/'):
        self.out_path = out_path
        self.html = ihtml
        self.color_tag = color_tag
        self.file_name = self.html.strip('./html/').replace('.html','')


    def get_html_data(self):
        with open(self.html, 'r', encoding='utf-8') as f:
            html_data = f.read()
        etree = html.etree
        return etree.HTML(html_data)

    def get_tag(cls, html_data):
        return  '{}知识点'.format(html_data.xpath('//title/text()')[0].replace(' - 幕布', ""))

    def get_datas(self, html_data):
        datas = html_data.xpath('//span[@color={}]'.format(self.color_tag))
        return [(qa(data).title(), qa(data).detail(), qa(data).make_pre()) for data in datas]

    def out_put(self, str):
        with open('{}{}.txt'.format(self.out_path, self.file_name), 'w', encoding='utf-8') as f:
            f.write(str)

    def get_out_str(self, out_datas, tag):
        str = ''
        for i in out_datas:
            str += '<p>[{}]{}</p> {}\t[{}]{} {}\n'.format(tag, i[2], i[0], tag, i[2], i[1])
        print(str)
        return str

    def run(self):
        html_data = self.get_html_data()
        out_datas = self.get_datas(html_data)
        tag = self.get_tag(html_data)
        out_str = self.get_out_str(out_datas, tag)
        self.out_put(out_str)

if __name__ == "__main__":

    rh = run_html(ihtml='../html/测试方法和流程拆分出的内容.html', out_path='../anki_txt/')
    rh.run()