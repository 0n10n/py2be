#对目录及子目录下的文件做时间顺序排列
import glob
import os
import time
import math  

dir_name = 'D:/github/0n10n/py2be/dl-bing-wallpapers/static/images/ZH-CN/'
item_every_page = 3

list_of_files = filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) )

list_of_files = sorted( list_of_files,
                        key = lambda x: os.path.getmtime(os.path.join(dir_name, x))
                        )
list_of_files.sort(reverse=True)  

    
page_total = math.ceil(len(list_of_files) / item_every_page)      
def get_page(page_num):
    print(f'Page Number: [ {page_num} ]')
    for file_name in list_of_files[(page_num-1)*item_every_page:page_num*item_every_page]:
        file_path = os.path.join(dir_name, file_name)
        timestamp_str = time.strftime(  '%m/%d/%Y :: %H:%M:%S',
                                    time.gmtime(os.path.getmtime(file_path))) 
        print(timestamp_str, ' -->', file_name) 
for i in range(1,3):
    get_page(i)