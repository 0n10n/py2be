#!C:/Python310/python.exe
# -*- coding: UTF-8 -*-

import requests
import os
import sys
import argparse
import re
import json

#必应壁纸涉及的区域代码和信息
regions = {
    "ar-XA":["Arabic","Arabia"],
    "bg-BG":["Bulgarian","Bulgaria"],
    "cs-CZ":["Czech","Czech Republic"],
    "da-DK":["Danish","Denmark"],
    "de-AT":["German","Austria"],
    "de-CH":["German","Switzerland"],
    "de-DE":["German","Germany"],
    "el-GR":["Greek","Greece"],
    "en-AU":["English","Australia"],
    "en-CA":["English","Canada"],
    "en-GB":["English","United Kingdom"],
    "en-ID":["English","Indonesia"],
    "en-IE":["English","Ireland"],
    "en-IN":["English","India"],
    "en-MY":["English","Malaysia"],
    "en-NZ":["English","New Zealand"],
    "en-PH":["English","Philippines"],
    "en-SG":["English","Singapore"],
    "en-US":["English","United States"],
    "en-XA":["English","Arabia"],
    "en-ZA":["English","South Africa"],
    "es-AR":["Spanish","Argentina"],
    "es-CL":["Spanish","Chile"],
    "es-ES":["Spanish","Spain"],
    "es-MX":["Spanish","Mexico"],
    "es-US":["Spanish","United States"],
    "es-XL":["Spanish","Latin America"],
    "et-EE":["Estonian","Estonia"],
    "fi-FI":["Finnish","Finland"],
    "fr-BE":["French","Belgium"],
    "fr-CA":["French","Canada"],
    "fr-CH":["French","Switzerland"],
    "fr-FR":["French","France"],
    "he-IL":["Hebrew","Israel"],
    "hr-HR":["Croatian","Croatia"],
    "hu-HU":["Hungarian","Hungary"],
    "it-IT":["Italian","Italy"],
    "ja-JP":["Japanese","Japan"],
    "ko-KR":["Korean","Korea"],
    "lt-LT":["Lithuanian","Lithuania"],
    "lv-LV":["Latvian","Latvia"],
    "nb-NO":["Norwegian","Norway"],
    "nl-BE":["Dutch","Belgium"],
    "nl-NL":["Dutch","Netherlands"],
    "pl-PL":["Polish","Poland"],
    "pt-BR":["Portuguese","Brazil"],
    "pt-PT":["Portuguese","Portugal"],
    "ro-RO":["Romanian","Romania"],
    "ru-RU":["Russian","Russia"],
    "sk-SK":["Slovak","Slovak Republic"],
    "sl-SL":["Slovenian","Slovenia"],
    "sv-SE":["Swedish","Sweden"],
    "th-TH":["Thai","Thailand"],
    "tr-TR":["Turkish","Turkey"],
    "uk-UA":["Ukrainian","Ukraine"],
    "zh-CN":["Chinese","China"],
    "zh-HK":["Chinese","Hong Kong SAR"],
    "zh-TW":["Chinese","Taiwan"]    
}
#必应壁纸支持的分辨率
resolutions=['800x600', '1024x768', '1280x720', '1280x768', '1366x768', '1920x1080', '1920x1200', '720x1280', '768x1024', '768x1280', '768x1366', '1080x1920']

#如果需要遍历所有的地区，则把下一句改为 desire_locales=list(regions.keys())
desire_locales=["zh-CN","ja-JP","en-US"]
desire_resolutions=['1080x1920']
download_folder='/mnt/d/temp/bing-wallpaper'
n_value=5
bing_wallpaper_api_url_template='https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n={n}&mkt={locale}'
host='https://bing.com'

#获取某url的页面内容
def send_request(url):
    headers = { 
        'referer': f'{url}',
        'accept': '*/*',
        'connection': 'close'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:  
            #print('响应内容:', response.text)  
            response.close()
            return response.text
        else:
            return None
    except Exception as errh: 
        print(f'HTTP Error: {errh.args[0]}, URL: {url}') 
        return None

#扫描api页面内容，返回找到的所有图片链接    
def scan_content(content):
    wallpapers_obj = json.loads(content)
    return wallpapers_obj['images']

    
#获取某个locale的wallpapers列表
#通过类似查询 https://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ja-JP，获得壁纸壁纸列表
def get_wallpapers_single(apiurl):
    content = send_request(apiurl)
    locale_wallpapers = scan_content(content)
    return locale_wallpapers 

#获取需要的全部locale的wallpapers
def get_wallpapers_all(desire_locales):
    wallpapers = []
    for locale in desire_locales:
        apiurl = bing_wallpaper_api_url_template.format(n=n_value, locale=locale) 
        locale_wallpapers = get_wallpapers_single(apiurl)
        if locale_wallpapers:
            wallpapers.extend(locale_wallpapers)
        #多加个小任务，给每种语言创建一个子目录
        mkdir(f'{download_folder}/{locale.upper()}')
    return wallpapers

def get_base_filename(str):
    parts = str.split('=')  
    if len(parts) >= 2:  
        content_after_equal = parts[1]  
        return content_after_equal
    else:  
        return None

def mkdir(local_dir):
    print(f"需要创建的目录 {local_dir}\n\r")
    if not os.path.exists(local_dir):  
        # 如果目录不存在，则创建它  
        os.makedirs(local_dir)  
    else:  
        pass
    
#从类似这样的：OHR.PeakDistrictNP_ZH-CN1987784653_XXX 文件名中获得区域代码
def get_locale_from_filename(s):
    pattern = r'_([^0-9]+)'  
    match = re.search(pattern, s)  
    language_part = 'default'
    if match:  
        language_part = match.group(1)  
    return language_part
        
def download_wallpapers(wallpapers,desire_resolutions):
    for wallpaper in wallpapers:
        for desire_resolution in desire_resolutions:
            url = f'{wallpaper["urlbase"]}_{desire_resolution}.jpg'
            print(f'url: {url} {wallpaper["title"]}')
            locale = get_locale_from_filename(get_base_filename(wallpaper["urlbase"]))
            filename = f'{wallpaper["startdate"]}_{get_base_filename(wallpaper["urlbase"])}_{desire_resolution}.jpg'
            headers = { 
                'referer': f'https:{url}',
                'accept': '*/*',
                'connection': 'close'           
            }
            try:
                response = requests.get(f'{host}{url}',headers=headers,timeout=3)
                #在下载目录下，根据语种（locale）存放下载的图片
                with open(f'{download_folder}/{locale}/{filename}', 'wb') as f:  
                    f.write(response.content)        
            except Exception as errh: 
                print(f'HTTP Error: {errh.args[0]}, URL: {url}')             


def main():
    wallpapers = get_wallpapers_all(desire_locales)
    download_wallpapers(wallpapers,desire_resolutions)
if __name__ == '__main__':
    sys.exit(main())