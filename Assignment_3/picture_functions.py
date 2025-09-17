import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

img = cv.imread('Assignment_3/lambo.png')
img_original = cv.imread('Assignment_3/shapes-1.png')
img_template = cv.imread('Assignment_3/shapes_template.jpg')

def sobel_edge_detection(image):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (3,3), 0)
    sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=1)
    cv.imwrite("Assignment_3/solutions/sobel_edge_detection.jpg", sobelxy)
    
def canny_edge_detection(image, threshold_1, threshold_2):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (3,3), 0)
    imga_canny = cv.Canny(image=img_blur, threshold1=threshold_1, threshold2=threshold_2)
    cv.imwrite("Assignment_3/solutions/canny_edge_detection.jpg", imga_canny)
    
def template_matching(image, template):
    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    
    res_mt = cv.matchTemplate(img_gray, template_gray, cv.TM_CCOEFF_NORMED)
    threshold = 0.9
    
    loc_matched = np.where(res_mt >= threshold)
    
    for pt in zip(*loc_matched[::-1]):
        cv.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv.imwrite("Assignment_3/solutions/template_matching.jpg", image)
    
def resize(image, scale_factor: int, up_or_down: str):
    if up_or_down == "up":
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)
    elif up_or_down == "down":
        width = int(image.shape[1] / scale_factor)
        height = int(image.shape[0] / scale_factor)
    else:
        raise ValueError("up_or_down must be either 'up' or 'down'")
    
    dim = (width, height)
    resized = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    cv.imwrite("Assignment_3/solutions/resized_image.jpg", resized)
    
    return resized

sobel_edge_detection(img)
canny_edge_detection(img, 50, 50)
template_matching(img_original, img_template)
resize(img, 2, "down")
