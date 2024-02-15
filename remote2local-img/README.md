# 远程-本地图片转换工具

## 起源：
有些网上的md格式教程，想保存成本地pdf，存在手机里随时阅读随时查。其他都好办，就是这些md里放的图片地址，就没法一起转成pdf了。需要把图片也保存到本地，并且修改原文本内的图片链接，比如原本是：

```
这里有个图片：

![](https://raw.githubusercontent.com/foobar/blog_image/main/image/image-123456.png)

```

需要做的事情：

1、把图片保存成本地路径：

```
raw_githubusercontent_com/foobar/blog_image/main/image/image-123456.png
```

2、把原md里的链接，改为：
```
![](raw_githubusercontent_com/W01fh4cker/blog_image/main/image/image-20240121181613825.png)
```
当然，全文都需要作此处理。

## 用法

```
python main.py -f 需要修改的文件名.md
```