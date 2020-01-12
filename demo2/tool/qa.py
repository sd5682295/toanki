# encoding = "utf-8"

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