#!C:/Python310/python.exe
# -*- coding: UTF-8 -*-


import sys
import requests
import re
import os
import argparse
import platform  
from urllib.parse import urlparse  

base_dir_win = "d:/temp/bypass/"
base_dir_linux = "/mnt/d/tmp/bypass"

def is_windows():  
    return platform.system() == "Windows" 

def get_basedir():
    if is_windows():  
        base_dir = base_dir_win
    else:  
        base_dir = base_dir_linux
    if not base_dir[-1] == '/':
        base_dir = base_dir + '/'
    return base_dir

def print_help():
    print('Usage: ')
    print('  python main.py -f filename.md')

def parse_args():
    
    parser = argparse.ArgumentParser(description='指定待处理的md文件')
    parser.add_argument('--file', '-f', dest='filename', metavar='FILENAME', help='指定要处理的文件名') 
    return parser.parse_args()

#把原文本图片的绝对URL格式，改为本地目录格式，并保存到base_dir下。
def remote2local(content,filepath):
    base_dir= get_basedir()
    mkdir(base_dir)    
    path,filename = os.path.split(filepath)
    replace_pattern = r'!(\[.*\])\(https?://(.*?)\)'
    #replacement = f'!\\g<1>({base_dir}\\g<2>)'  
    replacement = f'!\\g<1>(./\\g<2>)'  
    new_content = re.sub(replace_pattern, replacement, content)  
    print(f'文件 {filename} 将保存到 {base_dir} 目录下。 ')
    with open(base_dir+filename, 'w') as file: 
        file.write(new_content)    


def get_images(content):
    images_url = set()
    #匹配出所有的这类链接：![可能有文字描述](https://图片url地址)
    pattern = r'!\[.*\]\((https?://.*?)\)'  
    matches = re.findall(pattern, content)  
    for match in matches:   
        print(f"匹配到的内容 {match}")    
        images_url.add(match)
    return images_url 

def append_basedir(domain_and_path):
    return os.path.normpath(get_basedir() + domain_and_path)

def mkdir(local_dir):
    #directory_path = get_local_path(domain_and_path)
    print(f"需要创建的目录 {local_dir}\n\r")
    if not os.path.exists(local_dir):  
        # 如果目录不存在，则创建它  
        os.makedirs(local_dir)  
    else:  
        pass
        #print(f"目录 {directory_path} 已存在。")

def download_to_dir(img_url):
    domain,path,filename = parse_url(img_url) 
    
    domain_and_path =  domain + path
    # 获得打算存放图片的本地目录，为 base_dir+domain+path
    directory_path = append_basedir(domain_and_path)
    mkdir(directory_path)   
    print(f'下载图片： {img_url} to {directory_path} ') 
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
        with open(f'{directory_path}/{filename}', 'wb') as f:  
            f.write(response.content)        
    except Exception as errh: 
        print(f'HTTP Error: {errh.args[0]}, URL: {img_url}')     
    
def parse_url(url):
    parsed_url = urlparse(url)  
    urlpath = parsed_url.path
    path,filename = os.path.split(urlpath)
    return parsed_url.netloc,path,filename


def download_images(images_url):
    for img_url in images_url:  
        download_to_dir(img_url)

def read_file(filename):
    try:  
        with open(filename, 'r', encoding='utf-8') as file: 
            print(f"filename: {filename} ")            
            content = file.read()
            return content
    except FileNotFoundError:  
        print(f"文件不存在 : {filename}")  
    except IOError:  
        print(f"文件读写错误: {filename} ")  
    except Exception as e:
        print(f"未知错误： {e}")  
    return None

def handle_md_file(filename):
    content = read_file(filename)
    if content:
        #把url绝对路径，改为本地路径，并把整理后的内容，写到base_dir目录下
        remote2local(content,filename)
        #扫描文件里的图片链接地址，并进行一系列下载处理
        download_images(get_images(content))
    else:
        print(f"文件{filename}没有内容")


def main():
    args = parse_args()
    filename = args.filename
    if not filename:
        print_help()
    else: 
        handle_md_file(filename)
    return 0

if __name__ == '__main__':
    sys.exit(main())