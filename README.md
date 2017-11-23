# About IOCsToPaloaltoNGFW

将IOCs转换为Paloalto的外部动态列表

生成的外部动态列表命名依据GrabIOCs的config文件中的Setname参数，用于标识区分不同token生成的外部动态列表，例：
```
config文件中Setname为xxx
则最后生成的外部动态列表文件名为
xxx_ip.txt
xxx_domain.txt
xxx_url.txt

```

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

* 脚本输出的来源信息文件会保存在EDL文件夹中，并开启web服务
* 将外部动态列表的URL路径输出在屏幕上

### Installing

git clone https://github.com/Loveforkeeps/IOCsToPaloaltoEDL.git

若用户之前就有GrabIOCs可直接将项目中的
```
iocs_to_paloalto.py
webstart.py
webstop.py
```
拷至IOCs获取文件夹（GrabIOCs）中即可

### Recommended Python Version:

The recommended version for Python is **2.7.x**

### Using IOCsToPaloaltoEDL

Short Form    | Long Form     | Description
------------- | ------------- |-------------
  -h | --help | 显示帮助信息
  -f FILE | --file=FILE | 输入IOCs文件的路径，不加此参数时默认为当天的IOCs
  -m 80.0 | --min=80.0 |  增加信誉值过滤
  -c 500 | --count=500  | 外部动态列表的行数上限，不加此参数时默认为5000条


**Example**

* 转换当天IOCs数据
    * `python iocs_to_paloalto.py` 
* 指定IOCs文件
    * `python iocs_to_paloalto.py -f archive/IOCS_2017-11-21.csv`
* 指定文件，信誉值下限，条数
    * `python iocs_to_paloalto.py -f archive/IOCS_2017-11-21.csv -m 85 -c 1000`
* 单独开启EDL的HTTP服务
    * `python webstart.py`
* 关闭EDL的HTTP服务
    * `python webstart.py`




