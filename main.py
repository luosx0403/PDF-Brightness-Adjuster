import os
import numpy as np
from PIL import Image
from pdf2image import convert_from_path

# 输入和输出PDF文件名
input_pdf = "123.pdf"
output_pdf = "123_output.pdf"

# 亮度调整参数，可以根据需要修改
brightness_adjust = 100

# 将PDF的每一页转换为图像
pages = convert_from_path(input_pdf)

adjusted_images = []

for i, page in enumerate(pages):
    # 将图像转换为灰度模式
    gray_page = page.convert("L")
    # 转换为numpy数组，确保使用int16类型防止溢出
    npImage = np.array(gray_page, dtype=np.int16)
    
    # 获取图像的最小和最大亮度值，并进行类型转换
    min_val = int(np.min(npImage)) + brightness_adjust
    max_val = int(np.max(npImage))

    # 确保min_val在0到255之间
    min_val = max(0, min(255, min_val))
    max_val = max(0, min(255, max_val))

    # 如果min_val大于等于max_val，调整min_val
    if min_val >= max_val:
        min_val = int(np.min(npImage))
        # 再次确保min_val在0到255之间
        min_val = max(0, min(255, min_val))
        # 如果仍然min_val >= max_val，则不进行调整
        if min_val >= max_val:
            LUT = np.arange(256, dtype=np.uint8)
        else:
            # 创建LUT（查找表）用于映射像素值
            LUT = np.zeros(256, dtype=np.uint8)
            LUT[min_val:max_val+1] = np.linspace(
                start=0,
                stop=255,
                num=(max_val - min_val) + 1,
                endpoint=True,
                dtype=np.uint8
            )
    else:
        # 创建LUT（查找表）用于映射像素值
        LUT = np.zeros(256, dtype=np.uint8)
        LUT[min_val:max_val+1] = np.linspace(
            start=0,
            stop=255,
            num=(max_val - min_val) + 1,
            endpoint=True,
            dtype=np.uint8
        )
    
    # 应用LUT并转换为图像
    # 首先将npImage裁剪到0-255范围并转换为uint8
    npImage = np.clip(npImage, 0, 255).astype(np.uint8)
    imgRes = Image.fromarray(LUT[npImage])
    
    # 将调整后的图像转换为RGB模式（保存为PDF需要）
    imgRes = imgRes.convert("RGB")
    
    # 将调整后的图像添加到列表
    adjusted_images.append(imgRes)

# 保存调整后的图像为新的PDF文件
if adjusted_images:
    adjusted_images[0].save(
        output_pdf, save_all=True, append_images=adjusted_images[1:]
    )
