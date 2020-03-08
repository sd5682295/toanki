# encoding = "utf-8"
from lxml import html


class xpath_tool_base(object):
    def html_handle(self, html_data):
        """
        处理html,将html变成可以xpath的格式
        :param html_data: 原始的html
        :return: 可以xpath的html
        """
        pass
    def img_handle(self, img):
        """
        图片处理
        :param img: 图片地址
        :return: http格式的图片地址
        """
        pass
    def trim_data(self, obj, filter_data):
        """
        数据修剪
        :param obj: 数据
        :param filter_data: 修剪对象，为空时修剪空格
        :return: 完成修剪的数据
        """
        pass
    def get_title(self, obj):
        """
        获取文件的标题
        :param obj: 可以xpath的当前坐标
        :return: 标题
        """
        pass
    def get_text(self, obj):
        """
        获取当前坐标的text
        :param obj: 当前坐标
        :return: text值
        """
        pass
    def get_img(self, obj):
        """
        获取当前坐标的图片
        :param obj: 坐标
        :return: 图片地址
        """
        pass
    def have_child(self, obj):
        """
        判断是否有子节点
        :param obj: 坐标
        :return: 是否有子节点
        """
        pass
    def have_img(self, obj):
        """
        判断是否有图片
        :param obj: 坐标
        :return: 返回是否有图片
        """
        pass
    def list_data_handle(self, data):
        """
        列表数据处理
        :param data: 列数据
        :return: 第一个值
        """
        pass
    def to_html(self):
        """
        将信息包装成html
        :param data: 文字和图片地址
        :return: 内容的html
        """
        pass
    def get_pre(self):
        pass
    def get_color(self):
        pass
    def have_color(self):
        pass
    def data_clear(self):
        pass


获取上级菜单
获取颜色
判断颜色
字符串清洗

class xpath_tool(xpath_tool_base):
    def html_handle(self, html_data):
        etree = html.etree
        return etree.HTML(html_data)

    def img_handle(self, img):
        if img:
            if img.startswith('https'):
                return [img[0].replace('https', 'http')]
            return img
        return []

    def trim_data(self, obj, filter_data):
        if filter_data:
            return obj.replace(filter_data, '')
        return obj.replace(' ', '')

    def get_title(self, obj, filter_data):
        return self.trim(obj.xpath('//title/text()'),' - 幕布' )

    def get_text(self, obj):
        return obj.xpath('./text()')

    def get_img(self, obj):
        return self.img_handle(obj.xpath('../div/img/@src'))

    def have_child(self, obj):
        return len(self.obj.xpath('../ul'))

    def have_img(self, obj):
        return len(self.get_img(obj))

    def list_data_handle(self, data):
        if (type(data) == list):
            data = data[0]
        data = self.trim_data(data)
        return data

    def to_html(self, text, img):
        text = self.list_data_handle(text)
        text = self.list_data_handle(img)
        return '<p>{}</p><img src={} />'.format(text, img)

    def get_pre(self, obj):
        this_node = obj
        while this_node.xpath('../../../span/@color') == ["#3da8f5"]:
            if self.pre == '':
                tg = ''
            else:
                tg = '/'
            self.pre = this_node.xpath('../../../span/text()')[0] + tg + self.pre
            this_node = this_node.xpath('../../../span')[0]
        if self.pre != '':
            return ('[{}]'.format(self.pre))
        return ''

    def get_color(self):
        pass

    def have_color(self):
        pass

    def data_clear(self):
        pass

class qa():
    def __init__(self, obj):
        self.obj = obj
        self.pre = ''
        if not self.have_children() and not self.have_title_img():
            return False

    def get_obj(self):
        return self.obj

    def get_pre(self, node):
        data = node.xpath('../../../span');
        if data:
            return data.xpath('./@color')
        return False

    def make_pre(self):
        this_node = self.obj
        while this_node.xpath('../../../span/@color') == ["#3da8f5"]:
            if self.pre == '':
                tg = ''
            else:
                tg = '/'
            self.pre = this_node.xpath('../../../span/text()')[0] + tg + self.pre
            this_node = this_node.xpath('../../../span')[0]
        if self.pre != '':
            return ('[{}]'.format(self.pre))
        return ''

    def img_handle(self, img):
        if img:
            return [img[0].replace('https', 'http')][0]
        return []

    #     img[0].replace('https','http')

    def have_children(self):
        return len(self.obj.xpath('../ul'))

    def have_title_img(self):
        return len(self.get_title_img())

    def get_img(self, obj):
        return self.img_handle(obj.xpath('../div/img/@src'))

    def get_title_img(self):
        return self.get_img(self.obj)

    def title(self):
        if self.have_children():
            if self.get_title_img():
                return '<p>{}</p><img src={} />'.format(self.obj.xpath('./text()')[0].replace(' ', ''),
                                                        self.get_title_img()[0])
            else:
                return '<p>{}</p>'.format(self.obj.xpath('./text()')[0].replace(' ', ''))
        my_data = self.obj.xpath('./text()')
        return '<p>{}</p>'.format(my_data[0].replace(' ', ''))

    def tag(self):
        return self.obj

    def detail(self):
        if not self.have_children():
            return '<img src={} />'.format(self.get_title_img())
        img = self.get_title_img()
        detail_text = self.obj.xpath('../ul/li/span/text()')
        if img:
            return ('<p>{}</p><img src={} />'.format(detail_text, img))
        else:
            text = '</p><p>'.join(detail_text)
            return ('<p>{}</p>'.format(text))