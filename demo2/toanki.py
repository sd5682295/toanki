#  encoding = 'utf-8'
from lxml import html
from demo2.tool.qa import qa




if __name__ == '__main__':
    with open('./测试方法和流程拆分出的内容.html', 'r', encoding='utf-8') as f:
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
    with open('./anki_test.txt', 'w', encoding='utf-8') as f:
        f.write(str)