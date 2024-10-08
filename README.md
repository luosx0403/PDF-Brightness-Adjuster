# PDF文字颜色加深
尤其适用于一些扫描的电子版PDF，加深文字颜色更易于阅读。

# 安装依赖库
```bash
pip install numpy pillow pdf2image pymupdf
```
# 安装Poppler
pdf2image 库依赖于 poppler，它是一个开源的PDF渲染库，用于将PDF页面转换为图像。
- Linux（例如Ubuntu）:
- ```bash
  sudo apt-get install poppler-utils
```
- macOS:
  brew install poppler
```
- Windows:
- 把bin添加到系统PATH目录，
[https://blog.alivate.com.au/poppler-windows/](https://github.com/oschwartz10612/poppler-windows)
