# 用 Python 写一个爬图片的程序 
# https://tieba.baidu.com/f?kw=%E5%BC%A0%E9%A2%82%E6%96%87&ie=utf-8&pn=4250
# -*- coding: UTF-8 -*-
import requests
import re
import os
from urllib.parse import urlparse
from urllib.parse import quote
import time

base_dir = "./images"


def append_basedir(domain_and_path):
    return os.path.normpath(base_dir + domain_and_path)

def mkdir(local_dir):
    if not os.path.exists(local_dir):  
        os.makedirs(local_dir)  

# 从这个url里获取部分信息作为文件名：
# http://tiebapic.baidu.com/forum/w%3D580/sign=4bbe4651be1986184147ef8c7aec2e69/1ee55d2c11dfa9ec72b6952724d0f703918fc11a.jpg?
def get_filename_from_url(image_url):
    index = image_url.find(".jpg")
    return image_url[index-20:index+4]

def download_to_dir(img_url):
    mkdir(base_dir)   
    print(f'下载图片： {img_url} to {base_dir} ') 
    headers = { 
        'referer': f'{img_url}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'sec-ch-ua':'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site'            
    }
    try:
        response = requests.get(img_url,headers=headers,timeout=3)
        filename = get_filename_from_url(img_url)
        with open(f'{base_dir}/{filename}', 'wb') as f:  
            f.write(response.content)        
    except Exception as errh: 
        print(f'HTTP Error: {errh.args[0]}, URL: {img_url}')     
    
# 返回url页面的内容
def get_page(url):
    headers = { 
        'referer': f'{url}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'sec-ch-ua':'"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site'            
    }    
    response = requests.get(url,headers=headers,timeout=3)
    if response.status_code == 200:
        return response.content.decode('UTF-8', errors='ignore')
    else:
        return None

# 找出该url页面里的图片并下载
def fetch_img(url):
    html_content = get_page(url)
    if html_content:
        pattern = r'<img\s+[^>]*\bsrc\s*=\s*["\']?([^"\'>\s]+)["\']?[^>]*>'
        image_urls = re.findall(pattern, html_content)
        for img_url in image_urls:
            if ('tiebapic.baidu.com/forum' in img_url or 'imgsa.baidu.com' in img_url) and not '285356884' in img_url:
                print(f'{img_url} \n')
                #print(get_filename_from_url(img_url))        
                download_to_dir(img_url)

tieba_name = '张颂文'
encoded_name = quote(tieba_name, encoding='utf-8')
index_num = 4250
page_num=1
#fetch_url(url)

for _ in range(page_num):  # 重复五次
    if index_num<0:
        break
    url=f'https://tieba.baidu.com/f?kw={encoded_name}&ie=utf-8&pn={index_num}'
    html_content = get_page(url)
    #print(html_content)
    if html_content:
        pattern = r'href=\"(/p/\d+)\"'
        urls = re.findall(pattern, html_content)
        for url in urls:
            page_url = f'https://tieba.baidu.com{url}'
            fetch_img(page_url)
            time.sleep(30)
            
    index_num -= 50  # 对变量 i 减去 10
    
    
