import cv2 as cv
import numpy as np

img = cv.imread('Assignment_1/lena-1.png')

def info_image(image):
    print("Image height:", image.shape[0])
    print("Image width:", image.shape[1])
    print("Number of channels:", image.shape[2])
    print("Image size:", image.size)
    print("Image data type:", image.dtype)

info_image(img)