# IOCs —— PaloaltoNGFW

## 介绍
将IOCs转换为Paloalto的外部动态列表

生成的外部动态列表命名依据

GrabIOCs的config文件中的Setname参数，用于标识区分不同token生成的外部动态列表


* iocs_to_paloalto.py
    * IOCs数据转换
* webstart.py
    * HTTP服务开启
* webstop.py
    * HTTP服务关闭




通过iocs_to_paloalto.py将IOCs数据按照分值排序将其转换为
```
Paloalto防火墙
    |-- Objects
        |-- External Dynamic Lists
            |-- Source:
                Dynamic IP Lists
                Dynamic Domian Lists
                Dynamic URL Lists   
```

将脚本文件拷至IOCs获取文件夹（GrabIOCs）中，运行脚本后面跟GrabIOCs文件夹中archive文件夹里想要转换的IOCs文件名


* 脚本输出的来源信息文件会保存在EDL文件夹中
* 并在EDL文件夹里开启web服务
* 单独开启EDL的HTTP服务
    * `python webstart.py`
* 关闭EDL的HTTP服务
    * `python webstart.py`



