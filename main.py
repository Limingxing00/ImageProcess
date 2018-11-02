# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:14:09 2018
@author: Ming

function:
In the first module (divided with ---), is responsible for extracting the sequence of images from the 4-d data;
the second module (dividing with ---) is responsible for calculating the value of psnr before and after encoding
in the two directories.
"""

from c8 import *
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
# Need to modify the directory and image type by yourself
img = MyProcess(path1=r'D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\Raw.ome.tif',
                             path2=r'D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test',
                             ftype='jpg')
# [C, Z, T] = data1, [Width, Height] = data2
data1, data2 = img.dimension_file()
img.split(data1)
# ----------------------------------------------------------------------------------------------------------------------
# # Need to modify the directory and image type by yourself
# result = MyProcess(path1=r"D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test",
#                    path2=r"D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\video_split",
#                    ftype="jpg")
# img1, img2 = result.read_file()
# psnr_avr = []
# # Need to calculate the number of images of psnr
# num = 819
# for i in range(num):
#     psnr0 = result.psnr(img1[i], img2[i])
#     psnr_avr.append(psnr0)
# print(np.mean(psnr_avr))
# ----------------------------------------------------------------------------------------------------------------------
