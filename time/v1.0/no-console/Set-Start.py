import os
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 避免意外的位置

# -------------相关设置-----------------
# 最好别乱动 :D
startup_folder = os.path.join(os.getenv('APPDATA'), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
shortcut_name = "Check-Processes.lnk"# 在启动文件夹中的快捷方式名，如需修改请先清除自启动
shortcut_path = os.path.join(startup_folder, shortcut_name)
source_file = ".\\main.pyw"# 主程序路径
# -------------------------------------

if os.path.exists(shortcut_path):
    # 存在
    print("目前已被设为自启动，是否取消设置？")
    while True :
        print("[Y]是 [N]否")
        temp = input("你的回答是：")
        if temp.lower() in ["y", "yes", "是"]:
            print("删除自启动项中...")
            os.remove(shortcut_path)
            print("删除自启动项完毕！")
            break
        elif temp.lower() in ["n", "no", "否", "不"]:
            print("取消操作...")
            break
            # 退出
        else:
            print("请按说明回答！")
else:
    # 不存在
    print("目前没有被设为自启动，是否设置自启动？")
    while True :
        print("[Y]是 [N]否")
        temp = input("你的回答是：")
        if temp.lower() in ["y", "yes", "是"]:
            print("创建自启动项中...")
            # 在启动文件夹中创建快捷方式
            shutil.copyfile(source_file, shortcut_path)
            print("创建自启动项完毕！")
            break
        elif temp.lower() in ["n", "no", "否", "不"]:
            print("取消操作...")
            break
            # 退出
        else:
            print("请按说明回答！")

input("按Enter键继续...")