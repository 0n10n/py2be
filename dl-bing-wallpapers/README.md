# 下载必应壁纸

## 起源：

必应一直是我最喜欢的壁纸站。但是，官方的Bing Wallpaper安卓版app里，设置的图片却用的是电脑版本的分辨率。所以练手来试一下，写个程序自动下载自己需要的分辨率图片。

## 用法

1，先编辑`dl-bing-wallpaper.py` 里这几行：

```
....
desire_locales=["zh-CN","ja-JP","en-US"]
desire_resolutions=['1080x1920']
download_folder='/mnt/d/temp/bing-wallpaper'
n_value=1
```

- desire_locales：指定下载哪个locale语言版本的壁纸，完整的locale列表在程序中有，可以选自己习惯用的，可以设置多个；
- desire_resolutions：指定适合自己的图片分辨率。主要就是手机和桌面版的区别了。可以设置多个，如 `desire_resolutions=['1920x1080', '1080x1920']`。
- download_folder：指定图片的下载目录。
- n_value：一次下载多少个图片，默认1，最大5。

2，依赖库：

```
pip install requests
```

3, 执行：

```
python3 dl-bing-wallpaper.py
```

4，自己用来存放手机版下载图片的地方：http://aws.debagua.com/bing/ 等以后再弄个合适的Web前端。

## 已知问题：

- 没有再细分子目录的保存，待完善。

- flask不懂，现在搞得很笨拙，慢慢来，希望可以分页，可以切换地区。

  
