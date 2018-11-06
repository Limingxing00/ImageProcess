# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:17:53 2018
@author: Ming
"""
import time
import math
import glob
import cv2
from multiprocessing.dummy import Pool as ThreadPool


def read_file(path, ftype):
    """
    Read all files of type "ftype" under path
    :param path: file path
    :param ftype: file type
    :return:the list of file paths
    """
    img1 = glob.glob(path1 + '/*.' + ftype)
    return img1


def img16_to_img12(img):
    """
    The 16-bit pixel value is converted to binary,
    and the last four bits are changed to 0.
    :param img: 16-bit picture
    :return: img:  16-bit picture after reduction of last 4 bits
    """
    Width, Hight = img.shape
    for i in range(Width):
        for j in range(Hight):
            bin_var = bin(img[i, j])
            # Condition: only the binary length is greater than 4, and the last four digits are not "0000"
            if bin_var[-4:] != "0000" and len(bin_var) > 6:
                # Int's maximum is 2^32-1, uint16 will not overflow
                img[i, j] = int(bin_var[:-4]+str("0000"), 2)
    return img 

# =============================================================================
# def batch_change(path1, path2, ftype, num):
#     for i in range(num):
#         original = cv2.imread(path1[i], -1)
#         # img转换：16位转换成12位
#         img = img16_to_img12(original)
#         cv2.imwrite(path2+'\'+%05d.'%i+ftype, img)
#         print(i)
#     print("\n Format conversion completed")
#     
# =============================================================================


def batch_change(img, path2=r"D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test13", ftype="tiff"):
    """
    In order to adapt to the multi-threaded construction of the bulk storage function
    :param img: the list of catalogs of file paths
    :param path2: catalog of outputs
    :param ftype: file type
    :return:none
    """
    num_str = img.split("\\")[-1].split(".")[0]
    original = cv2.imread(img, -1)
    # img-conversion
    img16 = img16_to_img12(original)
    cv2.imwrite(path2+"\\"+num_str+"."+ftype, img16)
    print(num_str) 


if __name__ == '__main__':
    path1=r"D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test"
    ftype="tiff"
    start = time.time()
    imgs = read_file(path1, ftype)
    # batch_change(img, path2, ftype, num)
    pool = ThreadPool(64)
    pool.map(batch_change, imgs)
    pool.close()
    pool.join()
    end = time.time()
    print(end-start)  
    
    
    
    
