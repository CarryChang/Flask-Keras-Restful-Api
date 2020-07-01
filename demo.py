# -*- coding: utf-8 -*-
# @Time: 2020/7/1 0001 13:57
pic_path = 'pic/cat.jpg'
# 直接进行二进制读取
image = open(pic_path, "rb").read()
print(image)