import unittest

from lxml import html

from tool.qa import qa


class QaCase(unittest.TestCase):
    count_tag = False
    def setUp(self):
        with open('./html/测试方法和流程拆分出的内容.html', 'r', encoding='utf-8') as f:
            html_data = f.read()
        etree = html.etree
        html_data = etree.HTML(html_data)
        self.tag = '{}知识点'.format(html_data.xpath('//title/text()')[0].replace(' - 幕布', ""))
        datas = html_data.xpath('//span[@color="#3da8f5"]')
        self.datas = [qa(data) for data in datas]

    def log_handle(self, info):
        if QaCase.count_tag == False:
            QaCase.count_tag = 0
        print('{}{}'.format(str(QaCase.count_tag).zfill(3), info))
        QaCase.count_tag += 1

    def test_get_obj(self):
        self.log_handle('qa_get_obj测试返回锚点对象是否成功')
        for i in self.datas:
            self.assertEqual(i.get_obj(), i.obj)

    def test_make_pre(self):
        self.log_handle('qa_make_pre测试获取锚点上级有效目录是否成功')
        self.assertEqual(self.datas[0].make_pre(), '', '测试第一个目录的上级目录是不是为空')
        self.assertEqual(self.datas[10].make_pre(), '[如何解决没有合适的正交表？--k值不合适]', '测试第10个目录的上级目录是不是"[如何解决没有合适的正交表？--k值不合适]"')

    def test_img_handle(self):
        self.log_handle('qa_img_handle测试获图片地址的https转换成http是否有效')
        self.assertEqual(self.datas[0].img_handle('https://baidu.com'), 'http://baidu.com')


    def test_have_children(self):
        self.log_handle('qa_have_children测试判断是否有子目录是否有效')

        self.assertTrue(self.datas[9].have_children())
        self.assertTrue(self.datas[0].have_children())


    def test_title(self):
        print('测试文档锚点的内容获取是否有效')
        self.assertEqual(self.datas[0].title(), '<p>因果图法说明</p>')
        self.assertEqual(self.datas[10].title(), '<p>m值不合适</p>')


    def test_detail(self):
        """
        获得内容，作为anki答案
        如果没有子目录，返回标题图片
        detail_text定义内容
        将内容拼接成html
        :return: 内容<html>
        """
        # print([data.detail for data in self.datas])
        self.assertEqual(self.datas[0].detail(), '<p>1、因：输入条件</p><p>2、果：输出结果</p><p>3、以画图的方式来表示输入条件和输出结果之间的关系</p>')
        self.assertEqual(self.datas[10].detail(), '<p>1、最大值</p><p>2、少数服从多数</p>')


if __name__ == '__main__':
    # QaCase.count_tag = False
    unittest.main(verbosity=2)
