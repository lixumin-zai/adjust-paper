# python3.7
# -*- coding: utf-8 -*-
# @Author : listen
# @Time   :
import base64
import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

a = open("1.txt").read()
b = base64.b64decode(a)

# image = cv2.imdecode(np.asarray(bytearray(b),dtype='uint8'), cv2.IMREAD_COLOR)

image = cv2.imread("1.png", -1)

# 将图像通道分离开。
b, g, r, i = cv2.split(image)
# 以RGB的形式重新组合。
rgb_image = cv2.merge([r, g, b, i])
# 也可以使用这个函数直接转换成RGB形式。
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)


cv_img = cv2.imdecode(np.fromfile("1.png", dtype=np.uint8), 1)
print(cv_img)
d = io.imread("1.png")
print(rgb_image == d)
print(d)
