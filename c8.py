# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:17:53 2018
@author: Ming
"""
import os
import glob
import cv2
import numpy
import math

class MyProcess(object):
    """
    文件路径在__init__中进行初始化
    in_read中读入
    split中进行分离
    out_read中读出
    """
    def __init__(self, path1, path2, ftype):
        self.path1 = path1
        self.path2 = path2
        self.ftype = ftype
    
    def dimension_file(self):
        """
        得到Raw.ome.tif 的维度信息
        return:
           data1:[C, Z, T]
           data2:[Width, Height]
        """
        in_file_path = self.path1
        command = r'Ometiff.exe -i -s '+in_file_path
        cmd = os.popen(command,'r',1)
        # 使用os.popen可以得到cmd中的返回值,保存在out里
        out = cmd.read()
        # [C, Z, T]'s info
        index1 = out.split("[")[2].split("]")[0]
        # [Width, Height]'s info
        index2 = out.split("[")[4].split("]")[0]
        data1 = list(map(lambda x:int(x), index1.split(",")))
        data2 = list(map(lambda x:int(x), index2.split(",")))
        print("该文件[C, Z, T] = " + str(data1) + ", [Width, Height] = " + str(data2))
        return data1, data2

    def split(self, data1):
        """
        调用ometiff.exe
        param: data1--[C, Z, T]
        return: Null
        """
        in_file_path = self.path1
        out_file_path = self.path2
        ftype = self.ftype
        # 程序从30开始读取图片
        bias = 30
        # 目前扫描第0片, 如果扫描所有片，下面一行可以注释掉
        data1[1] = 1
        for j in range(data1[1]):
            for k in range(bias, data1[2]+bias):
                command = 'Ometiff.exe -s '+in_file_path+' -o '+out_file_path+'\%05d.' % (j*data1[2]+k-bias)+ftype + \
                          ' -d 0,'+str(j)+','+str(k)
                os.popen(command,'r')

    def read_file(self):
        """
        读入path1和path2 中，所有的ftype类型的文件路径索引，
        保存到img1和img2中
        :return:
        img1 - path1目录下所有.ftype的文件路径索引的list
        img2 - path2目录下所有.ftype的文件路径索引的list
        """
        path1 = self.path1
        path2 = self.path2
        ftype = self.ftype
        img1 = glob.glob(path1 + '/*.' + ftype)
        img2 = glob.glob(path2 + '/*.' + ftype)
        return img1, img2

    def psnr(self, img1, img2):
        """
        计算两幅图像的psnr
        :param img1: 图一路径
        :param img2: 图二路径
        :return: 两幅图像的psnr数值
        """
        original = cv2.imread(img1)
        contrast = cv2.imread(img2)
        mse = numpy.mean((original - contrast) ** 2)
        if mse == 0:
            return 100
        else:
            PIXEL_MAX = 255.0
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


