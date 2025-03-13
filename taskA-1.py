# Luke Davidson
# Homework 2
# CS-2840
# 3/4/2025

#Part 1
#Install/Import CV2 package
import cv2
import numpy as np

# #Load an Image
image = "Images/image3.jpg"
# #Read an Image of your choice
originalImage = cv2.imread(image)

#Convert the image into gray level image
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

#Show the original image
cv2.imshow("Original Image", originalImage)
cv2.waitKey(3000)

#Show the gray image
cv2.imshow("Gray Image", grayImage)
cv2.waitKey(3000)

#Destroy all windows
cv2.destroyAllWindows()