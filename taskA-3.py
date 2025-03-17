# Luke Davidson
# Homework 2
# CS-2840
# 3/4/2025

import cv2
import numpy as np


#Show image
originalImage = cv2.imread("Images/image3.jpg")
cv2.imshow("Original Image", originalImage)
cv2.waitKey(3000)

#Sobel Edge Detection
#cv2.sobel(src, ddepth, dx, dy)
# src - The source image
# ddepth - Precision of the output image
# dx - order of the derrivative for the image x, for ours we will use 1 
# dy - order of the derrivative for the image y, for ours we will use 1 
sobelOutput = cv2.Sobel(src=originalImage, ddepth=cv2.CV_64F, dx= 1, dy=1)
cv2.imshow('Sobel Edge Detection', sobelOutput)
cv2.waitKey(3000)


#Canny Edge Detection
# cv2.Canny(image, threshold1, threshold2)
# image - the source image
# threshold1 - lower limit that helps the function determine edges
# threshold2 - upper limit that helps the function determine edges
cannyOutput = cv2.Canny(image=originalImage, threshold1=100, threshold2=200)
cv2.imshow('Canny Edge Detection', cannyOutput)
cv2.waitKey(3000)