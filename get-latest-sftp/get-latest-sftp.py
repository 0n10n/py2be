
# -*- coding: UTF-8 -*-

import sys
import os
import argparse
import paramiko
import tarfile
import subprocess

prefix='/product'
base_dir = '/tmp'
unzip_dir = 'install'
command = ['./install.sh']
def print_help():
    print('Usage: ')
    print(f'  python {os.path.basename(__file__)} -u sftp_username -p sftp_passwd -l sftp_host -i item_name')

def parse_args():
    parser = argparse.ArgumentParser(description='指定待处理的md文件')
    parser.add_argument('--username', '-u', dest='username', metavar='USERNAME', help='sftp服务器用户名') 
    parser.add_argument('--password', '-p', dest='password', metavar='PASSWORD', help='sftp服务器密码') 
    parser.add_argument('--host', '-l', dest='host', metavar='HOST', help='sftp服务器主机/ip') 
    parser.add_argument('--item', '-i', dest='item', metavar='ITEM', help='需要遍历的子目录') 
    return parser.parse_args()

def get_latest_sftp_filename(sftphost,sftpuser,sftppwd,item,prefix):
    port = 22
    # 创建 SSH 客户端
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    client.connect(sftphost, port, sftpuser, sftppwd)

    # 创建 SFTP 客户端
    sftp = client.open_sftp()
    sftp.chdir(f'{prefix}/{item}')

    # 获取目录下所有文件的信息
    file_infos = [(f.filename, f.st_mtime) for f in sftp.listdir_attr()]

    # 根据文件最后修改时间排序
    file_infos.sort(key=lambda x: x[1], reverse=True)

    # 获取最后更新的一个文件名
    latest_file_name = file_infos[0][0]

    # 打印最后更新的文件名
    print("最后更新的文件是:", latest_file_name)
    if os.path.exists(f'{base_dir}/{latest_file_name}'):
        print("文件已存在，无需重新下载:", f'{base_dir}/{latest_file_name}')
    else:
        download_sftp_file(sftp, item,prefix, latest_file_name)

    # 关闭 SFTP 客户端和 SSH 连接
    sftp.close()
    client.close()
    
    return latest_file_name
    #pass

# 下载sftp服务器上的文件
def download_sftp_file(sftp, item,prefix,filename):
    remote_path = f'{prefix}/{item}/{filename}'
    local_path = f'{base_dir}/{filename}'
    sftp.get(remote_path, local_path)
    print("最新文件下载到：", local_path)

# 解压下载的文件
def unzip_dl_file(filename,base_dir):
    extract_dir = f'{base_dir}/{unzip_dir}'
    os.makedirs(extract_dir, exist_ok=True)

    with tarfile.open(filename, 'r:gz') as tar:
        tar.extractall(extract_dir)

    print("文件已解压到目录:", extract_dir)

def run_command(target_dir,command):
    print(f"将在 {target_dir} 目录执行命令 {command}")
    try:
        # 切换到目标目录并执行命令
        subprocess.run(command, cwd=target_dir, check=True)
        print("命令执行成功!")
    except subprocess.CalledProcessError as e:
        print("命令执行失败:", e)
    
def main():
    args = parse_args()
    sftpuser = args.username
    sftppwd = args.password
    sftphost = args.host
    item =  args.item
    
    if not (sftpuser and sftphost and item and sftppwd):
        print_help()
    else: 
        latest_filename = get_latest_sftp_filename(sftphost,sftpuser,sftppwd,item,prefix)
        unzip_dl_file(f'{base_dir}/{latest_filename}',base_dir)
        zipfile_basename = latest_filename[:-7]
        #command = ['./install.sh', '-u', 'foobar']
        run_command(f'{base_dir}/{unzip_dir}/{zipfile_basename}', command)
        
    return 0

if __name__ == '__main__':
    sys.exit(main())
