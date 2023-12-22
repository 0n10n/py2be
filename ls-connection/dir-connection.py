#学习Python后的练手脚本。
#列出对外tcp连接的目标IP+端口及对应的进程路径，熟悉一下数据结构的用法
#也算磕磕巴巴地实现了... 2023/12/22

import subprocess  
import re  
import psutil  
  
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

def get_tcp_connections():  
    # 使用netstat命令获取当前所有TCP连接信息  
    netstat_cmd = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE)  
    output = netstat_cmd.communicate()
    # 使用正则表达式提取TCP连接信息  
    for out in output:
        if out is None:
            pass
        else:
            tcp_connections = re.findall(r'^\s*TCP.*', out.decode('UTF-8', errors='ignore'), re.MULTILINE)
    return tcp_connections

establish_conn=[line for line in get_tcp_connections() if 'ESTABLISHED' in line  ]
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
            #print(f"{array[1]} | dst {array[2]} |程序路径: {process_path}")  
            if not ip in pids:  
                pids[ip]=set()
            pids[ip].add(process_path)
        else:  
            pass
            #print(f"找不到进程ID: {pid}")



for ip_key in sorted(dst.keys(), reverse=False):
    print(f"{ip_key}, { "/".join(dst[ip_key]) }, {"  ".join(pids[ip_key])} ")

