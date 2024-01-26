from PIL import Image, ImageDraw, ImageFont
import os
import sys
def add_text_to_image(image_path, text, position, font_path, font_size, color,i):

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
    image.save(f"{i}.png")
    
    # 关闭图片
    image.close()


text = "中考倒计时:"
position = (2900,0)  # 文字位置，以左上角为原点
font_path = "DuanNingYingBiKaiShuCuTi-2.ttf"  # 字体文件路径
font_size = 192
color = (101, 148, 68)  # 文字颜色，RGB形式
folder_name = "pictures"
current_dir = os.path.dirname(sys.executable)
pictures_dir = os.path.join(current_dir, folder_name)
images = [f for f in os.listdir(pictures_dir) if os.path.isfile(os.path.join(pictures_dir, f))]
if not images:
        print("没有找到任何图片文件")



for i in range(11):
    image_file = images[i]
    image_path = os.path.join(pictures_dir, image_file)
    add_text_to_image(image_path, text, position, font_path, font_size, color,i)
