import os
from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='./static',
            template_folder='./templates')

# 配置图片目录
IMAGE_DIR = '/mnt/d/github/0n10n/py2be/dl-bing-wallpapers/static/images/JA-JP'


@app.route('/')
def index():
    # 获取图片目录下所有的图片文件名
    image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files = sorted(image_files, reverse=True)
    return render_template('index.html', image_files=image_files )


if __name__ == '__main__':
    app.run(debug=True)
