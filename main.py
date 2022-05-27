# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# -*- coding:utf-8 -*-
# 作者：黄家琦
# 创建：2022-05-09
# 更新：2022-05-16
# 用意：用于数据集的预处理，将带口罩的图片与不带口罩的图片样本分别存放至指定文件夹并重命名


import os
import shutil

# 原数据集解压后的路径
path = 'C:/Users/HUANG JIAQI/Desktop/Masked-Face-Dataset/masked_whn/'
# 挑选出没有戴口罩图片存放的路径
newpath_for_WithoutMask = 'C:/Users/HUANG JIAQI/Desktop/Masked-Dataset/Without Mask'
# 挑选出戴口罩图片存放的路径
newpath_for_WithMask = 'C:/Users/HUANG JIAQI/Desktop/Masked-Dataset/With Mask'


def search(path, keyword):
    content = os.listdir(path)
    filenumber = 0
    # print(content)
    for each in content:
        each_path = path + os.sep + each
        # print(each)
        if keyword in each:
            # print(each_path)
            filenumber = filenumber + 1
            os.rename(each_path, path +'' +str(filenumber) + '.jpg')
        if os.path.isdir(each_path):
            search(each_path, keyword)


def search_for_digit(path, newpath_for_WithMask):
    # 获取目录下文件名清单
    list = os.listdir(path)
    filenumber = 0
    # print(list)
    # 移动图片到指定文件夹
    for i in range(0, len(list)):  # 遍历目录下的所有文件夹
        path = os.path.join('C:/Users/HUANG JIAQI/Desktop/Masked-Face-Dataset/masked_whn/', list[i])
        print(path)
        if os.path.isdir(path):  # 判断是否为文件夹
            for item in os.listdir(path):  # 遍历该文件夹中的所有文件
                dirname = os.path.join('C:/Users/HUANG JIAQI/Desktop/Masked-Face-Dataset/masked_whn/', list[i])  # 将根目录与文件夹名连接起来，获取文件目录
                full_path = os.path.join(dirname, item)  # 将文件目录与文件名连接起来，形成原来完整路径
                os.rename(full_path, dirname + os.sep + list[i] + item)
                shutil.move(dirname + os.sep + list[i] + item, newpath_for_WithMask)  # 移动文件到目标路径


def move(path, newpath):
    content = os.listdir(path)
    for each in content:
        each_path = path + os.sep + each
        if os.path.isfile(each_path):
            print(each_path)
            shutil.move(each_path, newpath)


def rename(newpath):
    content_for_newpath = os.listdir(newpath)
    renamenumber = 0
    for each in content_for_newpath:
        each_path_for_new = newpath + os.sep + each
        if os.path.isfile(each_path_for_new):
            renamenumber = renamenumber + 1
            os.rename(each_path_for_new, newpath + os.sep + str(renamenumber) + '.jpg')
            print("成功提取" + str(renamenumber) + "个图片样本到目标文件夹\n")


if __name__ == '__main__':
    # 先检索没有带口罩的unmasked文件
    search(path, 'unmasked')
    move(path, newpath_for_WithoutMask)
    rename(newpath_for_WithoutMask)

    # 再检索已经戴口罩的数字标号文件
    search_for_digit(path, newpath_for_WithMask)
    rename(newpath_for_WithMask)

