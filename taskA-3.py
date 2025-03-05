import cv2
import numpy as np


#Show image
originalImage = cv2.imread("Images/image1.png")
cv2.imshow("Original Image", originalImage)
cv2.waitKey(3000)