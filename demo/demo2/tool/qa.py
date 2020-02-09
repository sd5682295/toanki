# encoding = "utf-8"

class qa():
    def __init__(self, obj):
        """
        初始化qa,获取xpath节点，
        :param obj: xpath节点
        """
        self.obj = obj
        self.pre = ''
        if not self.have_children() and not self.have_title_img():
            return False

    def get_obj(self):
        """
        返回xpath节点
        :return: xpath节点 <obj>
        """
        return self.obj

    # def get_pre(self, node):
    #     """
    #     获取上级菜单的颜色
    #     :param node: 测试的节点
    #     :return: 测试节点的上级菜单颜色，如果没有上级菜单就返回False <str|bool>
    #     """
    #     data = node.xpath('../../../span');
    #     if data:
    #         return data.xpath('./@color')
    #     return False

    def make_pre(self):
        """
        循环获得上级菜单，如果上级菜单时蓝色的就在上级标识中加入上级菜单
        :return: 上级标识 <str>
        """
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
        """
        处理图片地址，将https改成http
        :param img: 图片地址
        :return: 将https改成http后的图片地址 <ip>
        """
        if img:
            return [img.replace('https', 'http')][0]
        return []

    #     img[0].replace('https','http')

    def have_children(self):
        """
        判断是否有子目录
        :return: 返回判断值 <bool>
        """
        return len(self.obj.xpath('../ul'))

    def have_title_img(self):
        """
        判断是否有标题图片
        :return: 返回判断值 <bool>
        """
        return len(self.get_title_img())

    def get_img(self, obj):
        """
        获取图片
        :param obj: xpath节点
        :return: 返回节点的图片地址<ip>
        """
        return self.img_handle(obj.xpath('../div/img/@src'))

    def get_title_img(self):
        """
        获取qa的title图片
        :return: 获取图片地址<ip>
        """
        return self.get_img(self.obj)

    def title(self):
        """
        获取节点标题
        :return: 节点标题<html>
        """
        if self.have_children():
            if self.get_title_img():
                return '<p>{}</p><img src={} />'.format(self.obj.xpath('./text()')[0].replace(' ', ''),
                                                        self.get_title_img()[0])
            else:
                return '<p>{}</p>'.format(self.obj.xpath('./text()')[0].replace(' ', ''))
        my_data = self.obj.xpath('./text()')
        return '<p>{}</p>'.format(my_data[0].replace(' ', ''))

    def detail(self):
        """
        获得内容，作为anki答案
        如果没有子目录，返回标题图片
        detail_text定义内容
        将内容拼接成html
        :return: 内容<html>
        """
        img = self.get_title_img()
        if not self.have_children():
            return '<img src={} />'.format(img)
        detail_text = self.obj.xpath('../ul/li/span/text()')
        if img:
            return ('<p>{}</p><img src={} />'.format(detail_text, img))
        else:
            text = '</p><p>'.join(detail_text)
            return ('<p>{}</p>'.format(text))