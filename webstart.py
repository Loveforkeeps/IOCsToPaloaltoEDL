#!/usr/bin/python
# encoding: utf8

import sys
import os
import SimpleHTTPServer 
import subprocess
import requests
from io import open
import signal
from time import sleep
import socket
 


PORT = "8008"

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

def webstart(setname=None):
    # 获取脚本位置路径
    path = os.path.split(os.path.realpath(__file__))[0] + '/'
    domainpath = 'EDL'
    os.chdir(path+domainpath)

    print "\n------ ↓↓ Starting HTTP server... ↓↓ ------Σ┗(＠ロ＠;)┛"
    cmd = 'nohup python -m SimpleHTTPServer ' + PORT + ' >/dev/null &'
    pro = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)

    with open("../pid","w") as f:
        f.writelines(unicode(pro.pid+1))
    sleep(1)
    print("Serving Running on..")
    ip = get_host_ip()
    url = "http://"+ip+":"+PORT+"/"
    print(url)

    print("\n<(‵▽′)>------ ↓↓ 复制下列外部动态列表至防火墙设置中 ↓↓ ------")
    
    print(url+setname+"_ip.txt")
    print(url+setname+"_domain.txt")
    print(url+setname+"_url.txt")

    return url

def main():
    webstart()
    
if __name__ == '__main__':
    main()




# try: 
#   from http.server import HTTPServer, BaseHTTPRequestHandler # Python 3
# except ImportError: 
#   import SimpleHTTPServer
#   from BaseHTTPServer import HTTPServer # Python 2
#   from SimpleHTTPServer import SimpleHTTPRequestHandler as BaseHTTPRequestHandler

# server = HTTPServer(('0.0.0.0',8008), BaseHTTPRequestHandler)
# thread = threading.Thread(target = server.serve_forever)
# thread.deamon = True
# def up():
#   thread.start()
#   print('starting server on port {}'.format(server.server_port))
# def down():
#   server.shutdown()
#   print('stopping server on port {}'.format(server.server_port))

# os.killpg(pro.pid, signal.SIGTERM)
