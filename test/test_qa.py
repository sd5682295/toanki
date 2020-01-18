import unittest

from lxml import html

from tool.qa import qa


class QaCase(unittest.TestCase):
    def setUp(self):
        with open('./html/测试方法和流程拆分出的内容.html', 'r', encoding='utf-8') as f:
            html_data = f.read()
        etree = html.etree
        html_data = etree.HTML(html_data)
        self.tag = '{}知识点'.format(html_data.xpath('//title/text()')[0].replace(' - 幕布', ""))
        datas = html_data.xpath('//span[@color="#3da8f5"]')
        self.datas = [qa(data) for data in datas]

    def test_get_obj(self):
        # print(self.test_get_obj().doc())
        for i in self.datas:
            self.assertEqual(i.get_obj(), i.obj)


    def test_make_pre(self):
        self.assertEqual(self.datas[0].make_pre(), '', '测试第一个目录的上级目录是不是为空')
        self.assertEqual(self.datas[10].make_pre(), '[如何解决没有合适的正交表？--k值不合适]', '测试第10个目录的上级目录是不是"[如何解决没有合适的正交表？--k值不合适]"')

    def test_img_handle(self):
        """
        处理图片地址，将https改成http
        :param img: 图片地址
        :return: 将https改成http后的图片地址 <ip>
        """
        self.assertEqual(self.datas[0].img_handle('https://baidu.com'), 'http://baidu.com')

    #     img[0].replace('https','http')

    def test_have_children(self):
        """
        判断是否有子目录
        :return: 返回判断值 <bool>
        """
        self.assertTrue(self.datas[9].have_children())
        self.assertTrue(self.datas[0].have_children())

    # def have_title_img(self):
    #     """
    #     判断是否有标题图片
    #     :return: 返回判断值 <bool>
    #     """
    #     return len(self.get_title_img())
    #
    # def get_img(self, obj):
    #     """
    #     获取图片
    #     :param obj: xpath节点
    #     :return: 返回节点的图片地址<ip>
    #     """
    #     return self.img_handle(obj.xpath('../div/img/@src'))
    #
    # def get_title_img(self):
    #     """1
    #     获取qa的title图片
    #     :return: 获取图片地址<ip>
    #     """
    #     return self.get_img(self.obj)

    def test_title(self):
        """
        获取节点标题
        :return: 节点标题<html>
        """
        self.assertEqual(self.datas[0].title(), '<p>因果图法说明</p>')
        self.assertEqual(self.datas[10].title(), '<p>m值不合适</p>')
        # if self.have_children():
        #     if self.get_title_img():
        #         return '<p>{}</p><img src={} />'.format(self.obj.xpath('./text()')[0].replace(' ', ''),
        #                                                 self.get_title_img()[0])
        #     else:
        #         return '<p>{}</p>'.format(self.obj.xpath('./text()')[0].replace(' ', ''))
        # my_data = self.obj.xpath('./text()')
        # return '<p>{}</p>'.format(my_data[0].replace(' ', ''))

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
        # img = self.get_title_img()
        # if not self.have_children():
        #     return '<img src={} />'.format(img)
        # detail_text = self.obj.xpath('../ul/li/span/text()')
        # if img:
        #     return ('<p>{}</p><img src={} />'.format(detail_text, img))
        # else:
        #     text = '</p><p>'.join(detail_text)
        #     return ('<p>{}</p>'.format(text))


if __name__ == '__main__':
    unittest.main(verbosity=2)
