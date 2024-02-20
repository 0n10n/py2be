# URL内容的文件类型推断

## 起源：

看到谷歌新出了个开源的文件类型判断工具Magika，这个就是纯练手，写个几行代码，验证一下网络资源的文件类型。实际上不用写代码，curl配合Magika直接就能用，如 `curl -sL https://baidu.com |magika -`。

## 用法

```
# 需要先安装magika
$ pip install magika
# 执行的命令行：
$ python main.py -u https://需要被判断的资源URL -m METHOD -d DATA
```

- -u ：指定要检查资源的URL地址，如果带query_string，需要两边加单引号，如`python main.py -u 'https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ja-JP'`
- -m：HTTP请求方法，可选项，默认为GET，如果为POST，则：`python main.py -u https://host.com -m post -data your_data`

## 注意事项

- 不支持跳转；
- 不支持命令行设定Content_Type（todo）。
