# About

做此项目是为了将使用幕布网做的结构化笔记自动转换成anki的问答卡片


# 说明

现在有3个demo

demo_prototype是最早的，通过jupyter运行
1. 先从幕布导出html文件放在项目根目录下
2. 使用jupyter打开toanki.ipynb，第一行设置输入的html文件地址，最后一行设置输出的txt文件地址，从上往下运行，即可完成转换

demo 是将demo_prototype文件转换成.py文件,用法和demo_prototype一致

demo2  是最新> 使用方法：

先从幕布导出html文件放在html目录下，运行main.py,输入anki的txt文件出现在csv目录下




## 技术栈

python 3.7



# Todo list

- [x] .ipynb格式的demo -- 完成
- [x] 转换成.py格式demo -- 完成
- [x] 分装输入输出端 -- 完成 
- [x] 各功能进行封装 -- 完成
- [ ] 将转化完成的html文件移除 -- 正在做
- [ ] 完善测试
- [ ] 以后再说


# License 

[MIT](https://opensource.org/licenses/MIT)
Copyright (c) 2020 sd5682295

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




