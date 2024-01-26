# -*- coding: gbk -*-
import os
import ctypes
import time
import winreg
import sys
def minimize_to_taskbar():
       # ��ȡ����̨���ڵľ��
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()
    
     # ��С�����ڵ�������
    ctypes.windll.user32.ShowWindow(console_handle, ctypes.c_int(2))


def set_wallpaper(image_path):
    # Windowsϵͳ���ñ�ֽ
    if os.name == "nt":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
def add_to_startup():

    script_path = os.path.abspath("C:\��ֽ\��ֽ.exe")
    script_name = os.path.basename("��ֽ.py")

    # ���ע������Ƿ��Ѵ��ڸ�������
    run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
    try:
        value, _ = winreg.QueryValueEx(run_key, script_name)
        if value == script_path:
            return
    except FileNotFoundError:
        pass
    finally:
        winreg.CloseKey(run_key)

    # �򿪡����С�����ע�����
    run_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)

    # �ڡ����С�����ע����������ýű���·����Ϊֵ
    winreg.SetValueEx(run_key, script_name, 0, winreg.REG_SZ, script_path)

    # �ر�ע�����
    winreg.CloseKey(run_key)
    print("��������ӵ�������")

def main():
    
    add_to_startup()
    folder_name = "pictures"
    current_dir = os.path.dirname(sys.executable)
    pictures_dir = os.path.join(current_dir, folder_name)
    images = [f for f in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, f))]
    if not images:
        print("û���ҵ��κ�ͼƬ�ļ�")
        return
    times = 1
    x = 0
    minimize_to_taskbar()
    while True:
        image_file = images[x]
        print(image_file)
        image_path = os.path.join(pictures_dir, image_file)
        try:
            if not "��" in image_path:
                set_wallpaper(image_path)
                print(f"��ֽ������{times}��")
                times += 1
                x += 1
                time.sleep(20)
            else:
                set_wallpaper(image_path)
                print(f"��ֽ������{times}��")
                times += 1
                x += 1
                time.sleep(0.6)
        except IOError:
            print("�޷���ͼƬ�ļ�")
        if x == len(images):
            x = 0
    
if __name__ == "__main__":
    main()

