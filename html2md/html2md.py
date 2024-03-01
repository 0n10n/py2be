import sys
import requests
import re
import os
from markdownify import markdownify as md    

def remove_multi_blankline(content):
    #替换连续的空行：
    pattern = re.compile(r'(^\s*?$\n)+', re.M)  
    replacement = r'\n'  
    new_html_content = re.sub(pattern, replacement, content) 
    return new_html_content

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

filename = 'python-cheatsheet.html'
content = read_file(filename)
md_content = remove_multi_blankline(md(content, strip=['code'], newline_style='BACKSLASH'))
with open(f'{filename}.md', 'w') as file: 
    file.write(md_content)   
