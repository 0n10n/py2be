# 远程-本地图片转换工具

## 起源：
有些网上的md格式教程，想保存成本地pdf，存在手机里随时阅读随时查。其他都好办，就是这些md里放的图片地址，就没法一起转成pdf了。需要把图片也保存到本地，并且修改原文本内的图片链接，比如原本是：


这里有个图片：

![zsw's cat](https://raw.githubusercontent.com/0n10n/py2be/main/remote2local-img/pangjuzi.jpg)


需要做的事情：

1、把图片保存到本地路径：

```
{BASE_DIR}/raw.githubusercontent.com/0n10n/py2be/main/remote2local-img/pangjuzi.jpg
```

2、把原md里的链接，改为：
```
![]({BASE_DIR}/raw.githubusercontent.com/0n10n/py2be/main/remote2local-img/pangjuzi.jpg
```
当然，全文都需要作此处理。

## 用法

修改程序开头的基础目录设置，指定自己希望最终的md文件和图片保存的目标目录：

```
base_dir_win = "d:/temp/"
base_dir_linux = "/mnt/d/tmp/"
```



```
python main.py -f 需要修改的文件名.md
```

## 注意事项
1，仅仅针对markdown格式的图片嵌入格式，不支持html的；
2，仅仅支持图片的URL地址是包含"域名"+"路径"+"文件名"的，如`https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png` 。如果是动态链接生成的，如`http://your_host/get_pic?id=1234`，会有问题。