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
from subprocess import run


class MyProcess(object):
    """
    File path is initialized in __init__()
  Achieve the function one will use Dimension_file(), split()
  Achieve the function two will use read_file(), psnr()
    """
    def __init__(self, path1, path2, ftype):
        self.path1 = path1
        self.path2 = path2
        self.ftype = ftype
    
    def dimension_file(self):
        """
        Get the dimension information of Raw.ome.tif
        return:
           data1:[C, Z, T]
           data2:[Width, Height]
        """
        in_file_path = self.path1
        command = r'Ometiff.exe -i -s '+in_file_path
        cmd = os.popen(command,'r',1)
        # Use os.popen to get the return value in cmd, save it in out
        out = cmd.read()
        # [C, Z, T]'s info
        index1 = out.split("[")[2].split("]")[0]
        # [Width, Height]'s info
        index2 = out.split("[")[4].split("]")[0]
        data1 = list(map(lambda x:int(x), index1.split(",")))
        data2 = list(map(lambda x:int(x), index2.split(",")))
        print("This file:[C, Z, T] = " + str(data1) + ", [Width, Height] = " + str(data2))
        return data1, data2

    def split(self, data1):
        """
        Call ometiff.exe
        param: data1--[C, Z, T]
        return: Null
        """
        in_file_path = self.path1
        out_file_path = self.path2
        ftype = self.ftype
        # The program reads pictures from 30
        bias = 30
        # Currently scan the 0th slice, if you scan all the slices, the next line can be commented out
        data1[1] = 1
        for j in range(data1[1]):
            for k in range(bias, data1[2]+bias):
                command = 'Ometiff.exe -s '+in_file_path+' -o '+out_file_path+'\%05d.' % (j*data1[2]+k-bias)+ftype + \
                          ' -d 0,'+str(j)+','+str(k)
                run(command)

    def read_file(self):
        """
        The function reads into path1 and path2, and all file path indexes of type "ftype" are saved to img1 and img2.
    :return:
    img1 - a list of all ".ftype" file path indexes in the path1 directory
    img2 - list of all ".ftype" file path indexes in the path2 directory
        """
        path1 = self.path1
        path2 = self.path2
        ftype = self.ftype
        img1 = glob.glob(path1 + '/*.' + ftype)
        img2 = glob.glob(path2 + '/*.' + ftype)
        return img1, img2

    def psnr_8bit(self, img1, img2):
        """
        Calculate the psnr of the two images of 8-bit, like jpg
    param img1: Figure 1 path
    param img2: Figure 2 path
    return: psnr value of two images
        """
        original = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
        contrast = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
        float32_original = original.astype(np.float32)
        float32_contrast = contrast.astype(np.float32)
        diff = cv2.absdiff(float32_contrast, float32_original)
        mse = np.mean(diff ** 2)
        
        if mse == 0:
            return 100
        else:
            PIXEL_MAX = 255.0
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

    def psnr_16bit(self, img1, img2):
        """
        Calculate the psnr of the two images of 16-bit, like tiff
    param img1: Figure 1 path
    param img2: Figure 2 path
    return: psnr value of two images
        """
        original = cv2.imread(img1, -1)
        contrast = cv2.imread(img2, -1)
        float64_original = original.astype(np.float64)
        float64_contrast = contrast.astype(np.float64)
        diff = cv2.absdiff(float64_contrast, float64_original)
        mse = np.mean(diff ** 2)
        if mse == 0:
            return 100
        else:
            PIXEL_MAX = 65535.0
            return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))



