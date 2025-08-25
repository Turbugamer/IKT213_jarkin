import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

img = cv.imread('Assignment_2/lena.png')

def padding (image, border_width): 
    reflect = cv.copyMakeBorder(image,border_width,border_width,border_width,border_width,cv.BORDER_REFLECT)
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    cv.imwrite('Assignment_2/solutions/reflect.png',reflect)
    plt.show()

def crop(image, x_0, x_1, y_0, y_1):
    cropped_image = image[y_0:(img.shape[0]-y_1), x_0:(img.shape[1]-x_1)]
    cv.imwrite("Assignment_2/solutions/cropped.jpg", cropped_image)  

def resize(image, width, height):
    resized_image = cv.resize(image, (width, height))
    cv.imwrite("Assignment_2/solutions/resized.jpg", resized_image)
    
def copy(image, emptyPictureArray):
    height, width = image.shape[:2]
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    emptyPictureArray[:] = image[:]
    cv.imwrite("Assignment_2/solutions/copied.jpg", emptyPictureArray)
    
def grayscale(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imwrite("Assignment_2/solutions/grayscale.jpg", gray)
    
def hsv(image):
    hsvImage = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imwrite("Assignment_2/solutions/hsv.jpg", hsvImage)
    
def hue_shifted(image, emptyPictureArray, hue):
    emptyPictureArray = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    emptyPictureArray[:] = image[:] + hue
    
    emptyPictureArray = np.clip(image.astype(np.int16) + hue, 0, 255).astype(np.uint8)
    cv.imwrite("Assignment_2/solutions/hue_shifted.jpg", emptyPictureArray)
    
def smoothing(image):
    smoothed = cv.GaussianBlur(image,(15,15),cv.BORDER_DEFAULT)
    cv.imwrite("Assignment_2/solutions/smoothed.jpg", smoothed)

def rotate(image, rotation_angle):
    if rotation_angle == 90:
        rotated = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        rotated = cv.rotate(image, cv.ROTATE_180)
        
    cv.imwrite("Assignment_2/solutions/rotated.jpg", rotated)

# padding(img,100)
# crop(img, 80, 130, 80, 130)
# resize(img, 200, 200)
# copy(img, np.array([]))
# grayscale(img)
# hsv(img)
# hue_shifted(img, np.array([]), 50)
# smoothing(img)
# rotate(img, 180)



