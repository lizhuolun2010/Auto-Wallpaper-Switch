# -*- coding: gbk -*-
from ast import Import
from cgitb import text
import ctypes

import os
a = os.getcwd()

def minimize_to_taskbar():
       # ��ȡ����̨���ڵľ��
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()
    
     # ��С�����ڵ�������
    ctypes.windll.user32.ShowWindow(console_handle, ctypes.c_int(2))

minimize_to_taskbar()

from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, position, font_path, font_size, color):

    # ��ͼƬ
    image = Image.open(image_path)
    print(image_path)
    # ������ͼ����
    draw = ImageDraw.Draw(image)
    print(text)
    # ��������
    font = ImageFont.truetype(font_path, font_size)
    
    # �������
    draw.text(position, text, font=font, fill=color)
    
    # �����޸ĺ��ͼƬ
    image.save("modified_image.png")
    
    # �ر�ͼƬ
    image.close()

text = ""
import datetime
def daojishi():
    global text
    # ��ȡ��ǰʱ��
    now2 = datetime.datetime.now()
    hour = now2.hour
    minute = now2.minute

    now = datetime.datetime.now()

    # ����Ŀ������Ϊ 2024 �� 6 �� 26 ��
    target_date = datetime.datetime(2024, 6, 26)
    
    # ����ʱ���
    time_delta = target_date - now
    text = f"         {hour}:{minute}\n                {time_delta.days}��{time_delta.seconds // 3600}Сʱ{(time_delta.seconds // 60) % 60}����"
    # ���ʱ���
    return text


daojishi()
position = (0,0)  # ����λ�ã������Ͻ�Ϊԭ��
font_path = "DuanNingYingBiKaiShuCuTi-2.ttf"  # �����ļ�·��
font_size = 256
color = (255, 0, 0)  # ������ɫ��RGB��ʽ


import os
import sys
import time
def shanchu():
    if os.path.exists("modified_image.jpg"):
        os.remove("modified_image.jpg")
        print("shanchu")

def set_wallpaper(image_path):
    # Windowsϵͳ���ñ�ֽ
    if os.name == "nt":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def main():

    folder_name = a + "\\pictures"
    current_dir = os.path.dirname(sys.executable)
    pictures_dir = os.path.join(current_dir, folder_name)
    images = [f for f in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, f))]
    if not images:
        print("û���ҵ��κ�ͼƬ�ļ�")
        return
    times = 1
    x = 0
    while True:
        daojishi()
        image_file = images[x]
        print(image_file)
        image_path = os.path.join(pictures_dir, image_file)
        add_text_to_image(image_path, text, position, font_path, font_size, color)
        set_wallpaper(a + ".\\modified_image.png")
        
        x += 1
        time.sleep(30)
        if x == len(images):
            x = 0
        
if __name__ == "__main__":
    main()
