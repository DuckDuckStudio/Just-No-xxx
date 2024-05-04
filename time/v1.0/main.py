import psutil
import os
import time
from tkinter import messagebox
from configparser import ConfigParser
import sys

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

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 避免意外的位置
config = ConfigParser(comment_prefixes=[])
config.read("config.ini", encoding='utf-8')
wait_time = config.getfloat('settings', 'wait_time')
threshold_time = config.getfloat('settings', 'threshold_time')

# -------------参数检查-----------------
# 别动我，否则没你好果子吃（指程序崩溃）
if wait_time < 0:
    messagebox.showerror("错误", "间隔时间不能小于0")
    sys.exit(1)
elif threshold_time < 0:
    messagebox.showerror("错误", "最多持续时间不能小于0")
    sys.exit(1)

try:
    wait_time = int(wait_time)
except:
    pass

try:
    threshold_time = int(threshold_time)
except:
    pass
# -------------------------------------

# 记录进程连续运行时间的字典
process_runtime = {}

# 读取需要检查的进程名称列表
def read_processes(file_path):
    with open(file_path, 'r') as file:
        processes = file.readlines()
    # 移除每行末尾的换行符
    processes = [process.strip() for process in processes]
    return processes

# 检查进程是否在运行
def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

def should_punish(process_name):# 该罚
    messagebox.showwarning("你在干什么？！", f"你竟然打开了{process_name}长达{threshold_time}秒？！\n你怎么敢的？")
    punish()

def main():
    processes_to_check = read_processes(nc_processes)
    print("读取配置文件完毕！")
    while True:
        for process_name in processes_to_check:
            if is_process_running(process_name):
                if process_name not in process_runtime:
                    process_runtime[process_name] = time.time()
                else:
                    runtime = time.time() - process_runtime[process_name]
                    if runtime >= threshold_time:
                        should_punish(process_name)
            else:  # 如果进程已经关闭，则重置运行时间
                if process_name in process_runtime:
                    del process_runtime[process_name]
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
