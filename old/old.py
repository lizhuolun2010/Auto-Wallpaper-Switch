# -*- coding: gbk -*-
import os
import ctypes
import time
import winreg
import sys
def minimize_to_taskbar():
       # 获取控制台窗口的句柄
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()
    
     # 最小化窗口到任务栏
    ctypes.windll.user32.ShowWindow(console_handle, ctypes.c_int(2))


def set_wallpaper(image_path):
    # Windows系统设置壁纸
    if os.name == "nt":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
def add_to_startup():

    script_path = os.path.abspath("C:\壁纸\壁纸.exe")
    script_name = os.path.basename("壁纸.py")

    # 检查注册表中是否已存在该启动项
    run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
    try:
        value, _ = winreg.QueryValueEx(run_key, script_name)
        if value == script_path:
            return
    except FileNotFoundError:
        pass
    finally:
        winreg.CloseKey(run_key)

    # 打开“运行”键的注册表项
    run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)

    # 在“运行”键的注册表项中设置脚本的路径作为值
    winreg.SetValueEx(run_key, script_name, 0, winreg.REG_SZ, script_path)

    # 关闭注册表项
    winreg.CloseKey(run_key)
    print("程序已添加到自启动")

def main():
    
    add_to_startup()
    folder_name = "pictures"
    current_dir = os.path.dirname(sys.executable)
    pictures_dir = os.path.join(current_dir, folder_name)
    images = [f for f in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, f))]
    if not images:
        print("没有找到任何图片文件")
        return
    times = 1
    x = 0
    minimize_to_taskbar()
    while True:
        image_file = images[x]
        print(image_file)
        image_path = os.path.join(pictures_dir, image_file)
        try:
            if not "周" in image_path:
                set_wallpaper(image_path)
                print(f"壁纸已设置{times}次")
                times += 1
                x += 1
                time.sleep(20)
            else:
                set_wallpaper(image_path)
                print(f"壁纸已设置{times}次")
                times += 1
                x += 1
                time.sleep(0.6)
        except IOError:
            print("无法打开图片文件")
        if x == len(images):
            x = 0
    
if __name__ == "__main__":
    main()

