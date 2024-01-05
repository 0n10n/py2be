#学习Python后的第一个练手小脚本。
#目标是列出Windows系统下，当前对外tcp连接的目标IP+端口及对应的进程路径，熟悉一下数据结构的用法
#也算磕磕巴巴地实现了... 2023/12/22
#只支持Windows系统！

import subprocess  
import re  
import psutil  
import os
import platform
import sys
  
def get_process_path_from_pid(pid):  
    try:  
        process = psutil.Process(pid)  
        return process.exe()  
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  
        return None  

def contains_local_address(s):  
    pattern = r'127\.0\.0\.1'  
    return bool(re.search(pattern, s))  
    #return False

op_str={}
op_str['Linux']="netstat -t -n -p"
op_str['Windows']="netstat -ano -p tcp"

def get_tcp_connections(os):  
    # 使用netstat命令获取当前所有TCP连接信息  
    netstat_cmd = subprocess.Popen(op_str[os].split(), stdout=subprocess.PIPE)  
    output = netstat_cmd.communicate()
    # 使用正则表达式提取TCP连接信息  
    for out in output:
        if out is None:
            pass
        else:
            tcp_connections = re.findall(r'^\s*TCP.*', out.decode('UTF-8', errors='ignore'), re.MULTILINE)
    return tcp_connections

system_platform = platform.system()
if  system_platform == "Linux":
    print("本程序暂时只支持Windows. ")
#    sys.exit(0)
    
establish_conn=[line for line in get_tcp_connections(system_platform) if 'ESTABLISHED' in line  ]
establish_list=[]
for line in establish_conn:
    array = line.split()  
    establish_list.append(array)

dst={}
pids={}
for array in establish_list:
    if not contains_local_address(array[1]) and not contains_local_address(array[2]):
        #print(f"source {array[1]} | dst {array[2]} | pid {array[4]}" )
        ip, port = array[2].split(":")
        if not ip in dst:  
            dst[ip]=set()
        dst[ip].add(str(port))
        pid=array[4]
        process_path = get_process_path_from_pid(int(pid))
        if process_path:  
            if not ip in pids:  
                pids[ip]=set()
            pids[ip].add(process_path)
        else:  
            pass
            #print(f"找不到进程ID: {pid}")

print(f"目标端ip\t 目标端口\t 相关进程 ")
for ip_key in sorted(dst.keys(), reverse=False):
    print(f"{ip_key},\t { '/'.join(dst[ip_key]) },\t\t {'  '.join(pids[ip_key])} ")

