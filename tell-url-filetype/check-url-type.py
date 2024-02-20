#!C:/Python310/python.exe
# -*- coding: UTF-8 -*-


import requests
import os
import sys
import argparse
from magika import Magika


def print_help():
    print('Usage: ')
    print('  python main.py -u http://需要验证类型的资源的URL -m method -d data' )

def parse_args():
    parser = argparse.ArgumentParser(description='获知网络资源的类型')
    parser.add_argument('--url', '-u', dest='url', metavar='URL', help='指定URL') 
    parser.add_argument('--method', '-m', dest='method', metavar='METHOD', help='请求方法') 
    parser.add_argument('--data', '-d', dest='data', metavar='DATA', help='提交的数据') 
    return parser.parse_args()


def send_request(url,method,data):
    headers = { 
        'referer': f'{url}',
        'accept': '*/*',
        'connection': 'close'
    }
    try:
        if method == 'post':
            response = requests.post(url,data=data,headers=headers)
        else:
            response = requests.get(url,headers=headers)
        if response.status_code == 200:  
            # response.text 只适合纯文本内容
            # print('响应内容:', response.text)  
            response.close()
            return response.content
        else:
            return None
    except Exception as errh: 
        print(f'HTTP Error: {errh.args[0]}, URL: {url}') 
        return None


def detect_type(content):
    magika = Magika()
    result = magika.identify_bytes(content)
    return result

def main():
    args = parse_args()
    url = args.url
    method = 'get'  
    if hasattr(args, 'method') and args.method is not None:  
        method = args.method.lower()      
    data = args.data
    if not url:
        print_help()
    else: 
        content = send_request(url,method,data)
        if content:
            result = detect_type(content)
            print(f'{method.upper()}【{url}】的判定类型为：{result.output.ct_label}。')
        else:
            print(f'{method.upper()} 【{url}】没有获得合适的内容。')
    return 0

if __name__ == '__main__':
    sys.exit(main())