# About
做此项目是为了将使用[幕布](https://mubu.com/)网做的结构化笔记自动转换成[anki](https://zhuanlan.zhihu.com/-anki)的问答卡片，后续将出于人性化操作进行优化。由于是个人使用工具，所以不做性能上的优化和强化，或是延后再实现性能优化。

使用幕布可以结构化处理笔记，可以快速将传统笔记优化成大纲格式，使用toanki可以自动将大纲格式的笔记转化成记忆卡片，并且可以自己选择记忆的内容，并可以通过增量笔记的方式增量记忆卡片方便管理，同时有的记忆卡片忘记它的背景知识也可以查询幕布笔记。

在这个工具组合中toanki作为粘合剂，致力于实现这2个工具间转换的最佳实现，并使这套工具链变为学习复习的最佳工具组合


# 打赏
为了支持作者继续优化和维护这个工具请大家多多给予打赏。

如果有其他作者在我的工具基础上开发新的分支，可以有2钟处理方式，1：贴本文中的收款二维码，2：收取打赏后分一半给作者，既通过本文中的收款二维码打赏。如用作商业用途，需联系作者，联系方式:181673940@qq.com


![图片](https://uploader.shimo.im/f/GUDdIShehwENTpzj.png!thumbnail)![图片](https://uploader.shimo.im/f/R9DdWxAOecMwf5y3.png!thumbnail)

# # 使用方法：

```
git clone https://github.com/sd5682295/toanki.git 
```
先将需要处理的幕布笔记以html格式导出，然后放到根目录下的html文件夹下

```
cd toanki
python main.py
```


# 技术栈
python 3.7



# Todo list
- [x] .ipynb格式的demo -- 完成
- [x] 转换成.py格式demo -- 完成
- [x] 分装输入输出端 -- 完成
- [x] 各功能进行封装 -- 完成
- [ ] 将转化完成的html文件移除 -- 正在做
- [ ] 通过不同颜色判断是否需要正反导入两次
- [ ] 完善测试
- [ ] 以后再说
# License
[MIT](https://opensource.org/licenses/MIT)

## Copyright (c) 2020 sd5682295
Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.




