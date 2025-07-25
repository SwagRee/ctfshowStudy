from PIL import Image

# 定义颜色数据
p = [
    0xa3, 0x9f, 0x67, 0xf7, 0x0e, 0x93, 0x1b, 0x23,
    0xbe, 0x2c, 0x8a, 0xd0, 0x80, 0xf9, 0xe1, 0xae,
    0x22, 0xf6, 0xd9, 0x43, 0x5d, 0xfb, 0xae, 0xcc,
    0x5a, 0x01, 0xdc, 0x5a, 0x01, 0xdc, 0xa3, 0x9f,
    0x67, 0xa5, 0xbe, 0x5f, 0x76, 0x74, 0x5a, 0x4c,
    0xa1, 0x3f, 0x7a, 0xbf, 0x30, 0x6b, 0x88, 0x2d,
    0x60, 0x65, 0x7d, 0x52, 0x9d, 0xad, 0x88, 0xa1,
    0x66, 0x44, 0x50, 0x33
]

# 创建一个32x32的图像
img = Image.new('RGB', (32, 32))

# 获取图像的像素
pixels = img.load()

# 设置像素颜色
for y in range(0, len(p), 3):
    r = p[y]
    g = p[y + 1]
    b = p[y + 2]
    # 设置像素位置 (x, y)，其中 x 通过索引 / 3 来获取
    x = round(y / 3)
    pixels[x, 0] = (r, g, b)

# 保存图像
img.save('Flag.png')