#!C:/Python310/python.exe
# -*- coding: UTF-8 -*-


import sys
import requests
import re
import os
import argparse

def print_help():
    print('Usage: ')
    print('  python main.py -f filename.md')

def parse_args():
    
    parser = argparse.ArgumentParser(description='指定待处理的md文件')
    parser.add_argument('--file', '-f', dest='filename', metavar='FILENAME', help='指定要处理的文件名') 
    return parser.parse_args()

def absolute2relative(content):
    pass

def get_images(content):
    pass

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
        print("有内容")
        absolute2relative(content)
        get_images(content)


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