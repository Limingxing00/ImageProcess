# ImageProcess

c8.py 

There are now two functions: 
1. Extracting the sequence of images from the 4D data; 
2. Calculating the psnr of all the types of pictures in both directories.

  2.1 if you want to use it on 8-bit img, please use psnr_8bit.
  2.2 if you want to use it on 16-bit img, please use psnr_16bit.

NOTE:
Please do not name the image as 1, 2, 3 to calculate psnr, 
because python reads follow 1, 10, 11, preferably in the format %0xd (x is an arbitrary number), 
such as 0001, 0002, 0003, if you have to name 1, 2, 3, it's also work,
but the current program doesn't add the module to adjust the order.Maybe I can add later.

Currently only my collaborators can use function one, and some things are not uploaded.


2018/11/6
update c12.py
c12.py
 the batch of 16-bit img clears their last 4-bit to zeros
