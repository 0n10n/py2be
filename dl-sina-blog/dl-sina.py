import sys
import requests
import re
from markdownify import markdownify as md    

urls=[]

def extract_links_and_titles(text):  
    pattern = r'<a title=".*" target="_blank" href="([^"]*)">([^<]*)<\/a>'  
    matches = re.findall(pattern, text)  
  
    for match in matches:  
        href,title = match
        #print(f"Title: {title}")  
        #print(f"Link: {href}")  
        #print("-" * 50)  
        urls.append(href)
        

def get_content(url):
    print(url)
    response = requests.get(url)  
    match = re.search(r'正文开始 -->([\s\S]*?)<!-- 正文结束 ', response.content.decode('UTF-8', errors='ignore'))  
    if match:  
        content = match.group(1)  
        print( md(content) )
        #print(content)    
        print("-" * 50)  

default_url='https://blog.sina.com.cn/s/articlelist_1218966851_0_1.html'
url=default_url if len(sys.argv)<2 else sys.argv[1]

headers = {  
#    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/9538'  
}  

for i in range(8, 7, -1):  
    print(i)
    response = requests.get(f'https://blog.sina.com.cn/s/articlelist_1218966851_0_{i}.html', headers=headers)  
    extract_links_and_titles(response.content.decode('UTF-8', errors='ignore'))


for item in urls:  
    get_content(f"https:{item}")

print(len(urls))

