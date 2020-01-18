from lxml import html

from tool.qa import qa


class run_html(object):
    def __init__(self, ihtml):
        self.html = ihtml
        self.file_name = self.html.strip('./html/').replace('.html','')
    def run(self):
        with open(self.html, 'r', encoding='utf-8') as f:
            html_data = f.read()
        etree = html.etree
        html_data = etree.HTML(html_data)
        tag = '{}知识点'.format(html_data.xpath('//title/text()')[0].replace(' - 幕布', ""))
        datas = html_data.xpath('//span[@color="#3da8f5"]')
        out_datas = [(qa(data).title(), qa(data).detail(), qa(data).make_pre()) for data in datas]
        str = ''
        for i in out_datas:
            str += '<p>[{}]{}</p> {}\t[{}]{} {}\n'.format(tag, i[2], i[0], tag, i[2], i[1])
        print(str)
        with open('./anki_txt/{}.txt'.format(self.file_name), 'w', encoding='utf-8') as f:
            f.write(str)

if __name__ == "__main__":

    rh = run_html('../测试方法和流程拆分出的内容.html')
    rh.run()