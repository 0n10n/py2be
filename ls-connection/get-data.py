# Windows： 
# TCP    127.0.0.1:2133         127.0.0.1:2134         ESTABLISHED     68412
# Linux:
# tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      644/sshd: /usr/sbin

import re
filename='ss.txt'
def contain_port(s):
    return bool(re.search(r':\d+', s))  

def net_status(s,pattern='ESTABLISHED'):
    return bool(re.search(pattern, s))  

def split(s):
    pattern = re.compile(r'\S+')
    return  re.findall(pattern, s) 

#结构：status{"192.168.100.1":{"port":{80,443};"pid":{1234,3456}}}
summary={}

with open(filename, 'rt') as file:
    for line in file:
        if contain_port(line) and net_status(line):
            results=split(line)
            print(results)
            remote_ip,remote_port = results[4].split(":")
            pid=results[6].split("/")[0]
            print(f'{remote_ip} {remote_port} {pid}')
            if remote_ip in summary:
                ports=summary[remote_ip]['ports']
                pids=summary[remote_ip]['pids']
            else:
                ports=set()
                pids=set() 
            ports.add(remote_port)
            pids.add(pid)
            summary[remote_ip]={"ports":ports,"pids":pids}

for ip,vaule in summary.items(): 
    print(f"{ip}: {vaule['ports']}  {vaule['pids']}")
