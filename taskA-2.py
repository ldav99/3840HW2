import cv2
import numpy as np

#Part 2
#Params:
# src - The input image
# dst - output image
# ddepth - desired depth of output image
# kernel - filter that will be applied to input image
# anchor - value for the filter that determines the relative poisition of a filtered point within the kernel
# delta - optional value added to filtered pixels before becoming the output image
# borderType - pixel extrapolation method

originalImage = cv2.imread("Images/image1.png")

#Move image left 1 pixel
leftFilter = np.zeros((3,3))
leftFilter[1][2] = 1
print(filter)


# #Use Filter2D to image 1 pixel left
leftImage = cv2.filter2D(src=originalImage, ddepth=-1, kernel=leftFilter, borderType=cv2.BORDER_CONSTANT)

#for loop to better show the difference between the two images
for i in range(10):
    cv2.imshow("Moved 1 Pixel Left", leftImage)
    cv2.waitKey(500)
    cv2.imshow("Moved 1 Pixel Left", originalImage)
    cv2.waitKey(500)


#Move image right 3 pixels
#Size of 7x7 to compensate for moving it three pixels, we want the 1 to be 3 spots away from the center of the filter.
rightFilter = np.zeros((7,7), np.float32)
rightFilter[3][0] = 1

rightImage = cv2.filter2D(src=originalImage, ddepth=-1, kernel=rightFilter, borderType=cv2.BORDER_CONSTANT)

#TODO ask if this is ok
#for loop to better show the difference between the two images
for i in range(10):
    cv2.imshow("Moved 3 Pixels Right", rightImage)
    cv2.waitKey(500)
    cv2.imshow("Moved 3 Pixels Right", originalImage)
    cv2.waitKey(500)

