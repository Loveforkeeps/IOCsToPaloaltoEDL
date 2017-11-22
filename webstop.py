#!python
# encoding: utf8

import os
from io import open
import sys
import subprocess

# 获取脚本位置路径
path = os.path.split(os.path.realpath(__file__))[0] + '/'
os.chdir(path) 

# 判断文件位置是否存在，若不存在则创建
domainpath = 'pid'
def webstop():
    if not os.path.exists(domainpath):
        print "HttpSever Not Running!!"
        exit(0)

    with open("pid","rb") as f:
        PID = f.read()
        print "Stoping server..."
        cmd = "kill " + PID
        pro = subprocess.call(cmd, shell=True)
        if not pro:
            print("Stop Succeed!")
    os.remove("pid")

def forceStop():
    res = os.popen("bash script/webstop.sh 2>/dev/null")
    print("Stop Succeed!")
    os.remove("pid")

def main():
    forceStop()
    # if len(sys.argv) == 2:
    #     if sys.argv[1] == '-f':
    #         forceStop()
    #     else:
    #         print("参数错误!\n-f :强制停止")
    # else:
    #     webstop()
if __name__ == '__main__':
    main()



