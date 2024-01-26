from PIL import Image
import os

# 输入文件夹路径和输出文件夹路径
input_folder = "输入文件夹路径"
output_folder = "输出文件夹路径"

# 获取输入文件夹中的所有 JPG 文件
jpg_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")]

# 遍历每个 JPG 文件进行转换
for jpg_file in jpg_files:
    # 构造输入文件的完整路径和输出文件的完整路径
    input_path = os.path.join(input_folder, jpg_file)
    output_path = os.path.join(output_folder, jpg_file.replace(".jpg", ".png"))

    # 打开 JPG 文件并进行大小调整和格式转换
    img = Image.open(input_path)
    img = img.resize((3840, 2160))
    img.save(output_path, "PNG")

print("转换完成")