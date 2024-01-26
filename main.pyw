# -*- coding: gbk -*-
from ast import Import
from cgitb import text
import ctypes

import os
a = os.getcwd()

def minimize_to_taskbar():
       # 获取控制台窗口的句柄
    console_handle = ctypes.windll.kernel32.GetConsoleWindow()
    
     # 最小化窗口到任务栏
    ctypes.windll.user32.ShowWindow(console_handle, ctypes.c_int(2))

minimize_to_taskbar()

from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, position, font_path, font_size, color):

    # 打开图片
    image = Image.open(image_path)
    print(image_path)
    # 创建绘图对象
    draw = ImageDraw.Draw(image)
    print(text)
    # 设置字体
    font = ImageFont.truetype(font_path, font_size)
    
    # 添加文字
    draw.text(position, text, font=font, fill=color)
    
    # 保存修改后的图片
    image.save("modified_image.png")
    
    # 关闭图片
    image.close()

text = ""
import datetime
def daojishi():
    global text
    # 获取当前时间
    now2 = datetime.datetime.now()
    hour = now2.hour
    minute = now2.minute

    now = datetime.datetime.now()

    # 设置目标日期为 2024 年 6 月 26 日
    target_date = datetime.datetime(2024, 6, 26)
    
    # 计算时间差
    time_delta = target_date - now
    text = f"         {hour}:{minute}\n                {time_delta.days}天{time_delta.seconds // 3600}小时{(time_delta.seconds // 60) % 60}分钟"
    # 输出时间差
    return text


daojishi()
position = (0,0)  # 文字位置，以左上角为原点
font_path = "DuanNingYingBiKaiShuCuTi-2.ttf"  # 字体文件路径
font_size = 256
color = (255, 0, 0)  # 文字颜色，RGB形式


import os
import sys
import time
def shanchu():
    if os.path.exists("modified_image.jpg"):
        os.remove("modified_image.jpg")
        print("shanchu")

def set_wallpaper(image_path):
    # Windows系统设置壁纸
    if os.name == "nt":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


def main():

    folder_name = a + "\\pictures"
    current_dir = os.path.dirname(sys.executable)
    pictures_dir = os.path.join(current_dir, folder_name)
    images = [f for f in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, f))]
    if not images:
        print("没有找到任何图片文件")
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
