# 就是不该开！
一个当检测到指定进程运行后执行惩罚的程序。

[![GitHub Release](https://img.shields.io/github/release/DuckDuckStudio/Just-No-xxx?style=flat)](https://github.com/DuckDuckStudio/Just-No-xxx/releases/latest) [![Github All Releases](https://img.shields.io/github/downloads/DuckDuckStudio/Just-No-xxx/total.svg?style=flat)]()  

## 如何使用
本程序分为基础版和计时版，两个版本区别如下：  
- 基础版：指定进程**一旦运行就执行惩罚**。
- 计时版：指定进程**连续运行指定时间后执行惩罚**。

### 如何下载
请前往[仓库发行版](https://github.com/DuckDuckStudio/Just-No-xxx/releases/latest)下载最新的程序。  
如果你需要下载不带控制台的程序 ~~(就是运行了你也看不见)~~ ，请下载名称带`no-console`的程序。  
如果你需要下载计时版，请下载名称带`time`的程序。  
如果你下载了名称带`py`的程序，则你必须先[配置Python](https://duckduckstudio.github.io/yazicbs.github.io/Tools/Fufu_Tools/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98Q&A/%E4%B8%BB%E7%A8%8B%E5%BA%8F/#open-lite-program)。  

### 如何设置自启动
请运行程序文件夹中的`Set-Start.py`来设置自启动。  
无论你是需要取消自启动还是设置自启动，都是用这个文件。  


## 自定义
本程序提供了一系列自定义方案，详细见下。  
### 如何自定义需要检测的进程
请修改程序文件夹中的`Processes.txt`文件，每行一个进程。  

### 如何自定义惩罚
你目前只可以在使用带`py`的程序时修改惩罚。  
打开程序文件夹中的`main.py`或`main.pyw`，你应该会看到以下内容：  
```python
# -------------相关设置-----------------
nc_processes = ".\\Processes.txt" # 需要检查的进程(Need Check Processes)
# 每次检查间隔时间请在config.ini中修改，时间过短可能会影响CPU
def punish():
    # 可以在这里编辑需要罚什么
    # 例如 os.system("shutdown -s -t 30") # 30秒后关机
    # 当然，你也可以将 30 秒改为 0 秒(立刻)，真就成防沉迷了属于是
    os.system("shutdown -s -t 30")
    pass # 就算没有惩罚也不要把我删掉呀，人家也有存在的意义嘛
# -------------------------------------
```
你可以通过编辑`punish`函数来自定义惩罚内容，默认为 30 秒后关机。  

### 如何自定义检测间隔
打开程序文件夹中的`config.ini`，你应该会看到以下内容：  
```ini
[settings]
wait_time = 1
# 如果是计时版还会有其他内容
```
你可以通过修改`wait_time`的值来自定义检测间隔，单位为“秒”，只接受非负数 (可以使用 0 或者浮点数) 。    

### 如何自定义进程最多持续时间
你目前只可以在使用 计时版 时修改最多持续时间。  
打开程序文件夹中的`config.ini`，你应该会看到以下内容：  
```ini
[settings]
wait_time = 1
threshold_time = 30
# 只适用于计时版
```
你可以通过修改`threshold_time`的值来自定义检测间隔，单位为“秒”，只接受非负数 (可以使用 0 或者浮点数，不过使用 0 就没意义了嘛) 。   