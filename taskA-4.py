# Luke Davidson
# Homework 2
# CS-2840
# 3/4/2025

import numpy as np
import cv2


def main():
    #Load Image
    image = "Images/creeper.png"
    #Read an Image of your choice
    originalImage = cv2.imread(image)

    #Create filter of size 7.  * (1/3) for grayscale
    filter = np.ones((7, 7))

    #Convert image to grayscale so we only have to worry about one channel
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

    imageFiltering(filter, grayImage)


def imageFiltering(filter, image):
    imageHeight, imageWidth = image.shape
    outputHeight, outputWidth = imageHeight-len(filter)+1 , imageWidth-len(filter)+1 #394 294

    #Create output array with the correct dimensions
    output = np.zeros([imageHeight, imageWidth])
    tempImg = np.zeros([imageHeight, imageWidth])
    pixelGroup = np.zeros([7,7])
    

    for y in range(imageHeight):
        for x in range(imageWidth):
            tempImg[y, x] = image[y, x]
            np.append(pixelGroup , tempImg[y:y+7 , x:x+7])

            output.append(sum(np.dot(pixelGroup, filter)))

    print(tempImg)
    print('--------')
    print(pixelGroup)

    return output

if __name__=="__main__":
    main()