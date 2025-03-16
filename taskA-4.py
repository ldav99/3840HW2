# Luke Davidson
# Homework 2
# CS-2840
# 3/4/2025

import numpy as np
import cv2
from matplotlib import pyplot as plt


def main():
    #Load Image
    image = "Images/image3.jpg"
    #Read an Image of your choice
    originalImage = cv2.imread(image)

    #Create filter of size 7.  * (1/3) for grayscale
    filter = np.ones((7, 7))

    #Convert image to grayscale so we only have to worry about one channel
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

    imageFiltering(filter, grayImage)


def imageFiltering(filter, image):
#Get original image and output image height and width
    imageHeight, imageWidth = image.shape
    outputHeight, outputWidth = imageHeight-len(filter)+1 , imageWidth-len(filter)+1 #394 294 or 26,26

#Create output array with the correct dimensions
    output = np.zeros((outputHeight, outputWidth))
    
#Itterate over the original image and take a group of 7x7 pixels to be used 
    for y in range(outputHeight):
        for x in range(outputWidth):
            tempImg = np.array(image)

#Slide the grid till the edge hits the edges of the image 
            if x <= (imageWidth - 7) or y <= (imageHeight - 7):
                pixelGroup = tempImg[y:y+7, x:x+7]

#Take the sum of the pixel group multiplied by the filter and append it to the output 
            output[y, x] = np.sum(np.dot(filter , pixelGroup))
            
#Use Pyplot to take the output array of values and show them as an image
    plt.imshow(output, interpolation='nearest')
    plt.show()

    return output

if __name__=="__main__":
    main()