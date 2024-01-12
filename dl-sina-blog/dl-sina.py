import sys
import requests
import re
import os
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

def remove_multi_blankline(content):
    #替换连续的空行：
    pattern = re.compile(r'(^\s*?$\n)+', re.M)  
    replacement = r'\n'  
    new_html_content = re.sub(pattern, replacement, content) 
    return new_html_content

def resort_img(content):
    #pattern = r'<img.*?real_src="(.*?)".*?/>'  
    replace_pattern = r'(<a HREF=.*?)?<img.*?real_src\s+="http://.*?/.*?/([\s\S]*?)(&amp;690)?".*?/>(</A>)?'
    replacement = r'<img src="images/\2"/><p>\r\n'  
    new_html_content = re.sub(replace_pattern, replacement, content)  
    return new_html_content

def download_img(url,content):
    pattern = r'real_src\s+="([\s\S]*?)".*?'  
    matches = re.findall(pattern, content)     
    for match in matches:  
        img_url = match    
        print(img_url)
        match = re.search(r'http://(.*?)/.*?/([a-zA-Z0-9]+)', img_url)  
        if match:  
            img_filename = match.group(2)  
            headers = { 
            'authority':f'{match.group(1)}',               
            'referer': f'https:{url}',
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
            with open(f'images/{img_filename}', 'wb') as f:  
                f.write(response.content)        
        except Exception as errh: 
            print(f'HTTP Error: {errh.args[0]}, URL: {img_url}') 
    
    
def get_content(url):
    response = requests.get(url)  
    match = re.search(r'"titName SG_txta">([\s\S]*?)</h2>[\s\S]*?SG_txtc">\(([\s\S]*?)\)</span>[\s\S]*?正文开始 -->([\s\S]*?)<!-- 正文结束 ', response.content.decode('UTF-8', errors='ignore'))  
    if match:  
        blogtime = match.group(2)  
        title = match.group(1)  
        content = match.group(3) 
        print(f"<h1>{title}</h1>" ) 
        print(f"{blogtime}" )
        print("-" * 6)  
        return title,blogtime,content

def remove_file(file_path):
    if os.path.exists(file_path):  
        os.remove(file_path)  
        print(f"{file_path} 文件已被删除")  
    else:  
        print(f"{file_path} 文件不存在")            


def write_markdown(url,title,blogtime,content,filename):
    md_content= md(resort_img(content))
    with open(filename, 'a') as file: 
        file.write(f"\r\n<h2>{title}</h2>\r\n" )    
        file.write(f"链接：[{url}]({url})\r\n")     
        file.write(f"时间：{blogtime}\r\n")     
        #file.write()
        file.write(remove_multi_blankline(md_content))      
        file.write("-" * 6 )    

def get_maxpage(id):
    response = requests.get(f'https://blog.sina.com.cn/s/articlelist_{id}_0_1.html')  
    match = re.search(r'共(\d+)页', response.content.decode('UTF-8', errors='ignore'))  
    if match:  
        maxpage = match.group(1) 
        return maxpage
    
#blog_id='1218966851'
blog_id='1198952915'

id=blog_id if len(sys.argv)<2 else sys.argv[1]
print(id)

headers = {  
    'Referer': f'https://blog.sina.com.cn/s/articlelist_{id}_0.html'
}  

for filename in os.listdir():  
    if filename.startswith(f'{id}'):  
        os.remove(filename) 
        print(f'已删除 {filename}') 

maxpage=int(get_maxpage(id))
print(f'maxpage {maxpage}')
#exit(0)

# 先抓取全部的页面和链接，存到urls[]数组里
# 从哪页爬到哪页（start,end,正向/反向）
for i in range(1, maxpage+1, 1):  
    #print(i)
    response = requests.get(f'https://blog.sina.com.cn/s/articlelist_{id}_0_{i}.html', headers=headers)  
    extract_links_and_titles(response.content.decode('UTF-8', errors='ignore'))


count = 0  
page=1
#反序排列（先取出时间久远的blog）
for i in range(len(urls)-1, -1, -1):  
    title,blogtime,content = get_content(f"https:{urls[i]}")
    print(f"{i} https:{urls[i]}")
    filepath = f'{id}_{page}.md' 
    write_markdown(f'https:{urls[i]}',f'{page}/{count+1} {title}',blogtime,content,filepath)
    download_img(urls[i],content)
    count += 1  
    with open(f'{id}.md', 'a') as file: 
        file.write(f'{count} [{title}](https:{urls[i]})|({blogtime}) \r\n\r\n')
    if count % 30 == 0:  
        page += 1  
    if count == 40:  
        pass


