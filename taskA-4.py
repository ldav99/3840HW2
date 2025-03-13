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
    output = np.zeros([imageHeight, imageWidth], dtype=int)
    tempImg = np.zeros([imageHeight, imageWidth], dtype=int)
    pixelGroup = np.zeros([7,7], dtype=int)
    
#Itterate over the original image and take a group of 7x7 pixels to be used 
    for y in range(imageHeight):
        for x in range(imageWidth):
            tempImg[y, x] = image[y, x]

#Slide the grid till the edge hits the edges of the image 
            if x <= (imageWidth - 7) or y <= (imageHeight - 7):
                np.append(pixelGroup , tempImg[y:y+7 , x:x+7])#Assign this to the pizelGroup

#Take the sum of the pixel group multiplied by the filter and append it to the output 
            np.append(output, sum(np.dot(pixelGroup, filter)))

    print(tempImg)
    print('--------')
    print(pixelGroup)

    return output

if __name__=="__main__":
    main()