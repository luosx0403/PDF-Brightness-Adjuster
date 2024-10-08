import os
import numpy as np
from PIL import Image, ImageEnhance
from pdf2image import convert_from_path

# 输入和输出PDF文件名
input_pdf = "123.pdf"
output_pdf = "123_output.pdf"

# 亮度调整参数，可以根据需要修改
brightness_adjust = 50

# 将PDF的每一页转换为图像
pages = convert_from_path(input_pdf)

adjusted_images = []

for i, page in enumerate(pages):
    # 不再将图像转换为灰度模式，保留彩色信息
    # 调整图像的对比度以加深文字颜色
    enhancer = ImageEnhance.Contrast(page)
    imgRes = enhancer.enhance(1.0 + (brightness_adjust / 100.0))

    # 将调整后的图像添加到列表
    adjusted_images.append(imgRes)

# 保存调整后的图像为新的PDF文件，保持原有质量和分辨率
if adjusted_images:
    adjusted_images[0].save(
        output_pdf, save_all=True, append_images=adjusted_images[1:]
    )
