# Luke Davidson
# Homework 2
# CS-2840
# 3/4/2025

import cv2
import numpy as np


#Show image
originalImage = cv2.imread("Images/image1.png")
cv2.imshow("Original Image", originalImage)
cv2.waitKey(3000)

#Sobel Edge Detection
#TODO Ask if we need to blur the image first before doing edge detection.
#cv2.sobel(src, ddepth, dx, dy)
# src - The source image
# ddepth - Precision of the output image
# dx - 
# dy -
sobelOutput = cv2.Sobel(src=originalImage, ddepth=cv2.CV_64F, dx= 1, dy=1)
#TODO Ask what our result should look like
cv2.imshow('Sobel Edge Detection', sobelOutput)
cv2.waitKey(3000)


#Canny Edge Detection
# cv2.Canny(image, threshold1, threshold2)
# image - the source image
# threshold1 - 
# threshold2 - 
cannyOutput = cv2.Canny(image=originalImage, threshold1=100, threshold2=200)
cv2.imshow('Canny Edge Detection', cannyOutput)
cv2.waitKey(3000)