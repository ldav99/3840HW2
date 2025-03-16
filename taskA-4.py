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

    #Create a blank filter of size 7 all 1's for now.
    filter = np.ones([7, 7])

    #Filter for df/dx
    dxFilter = np.zeros([3,3])
    dxFilter[0][0] = -1
    dxFilter[1][0] = -2
    dxFilter[2][0] = -1
    dxFilter[0][2] = 1
    dxFilter[1][2] = 2
    dxFilter[2][2] = 1
    #Filter for df/dy
    dyFilter = np.zeros([3,3])
    dyFilter[0][0] = -1
    dyFilter[0][1] = -2
    dyFilter[0][2] = -1
    dyFilter[2][0] = 1
    dyFilter[2][1] = 2
    dyFilter[2][2] = 1
    print(dyFilter)

    #Convert image to grayscale so we only have to worry about one channel
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

#Base filter
    imageFiltering(filter, grayImage)

#df/dx filter
    imageFiltering(dxFilter, grayImage)

#df/dy filter
    imageFiltering(dyFilter, grayImage)


def imageFiltering(filter, image):
#Get filter length
    filterLength = len(filter)
#Get original image and output image height and width
    imageHeight, imageWidth = image.shape
    outputHeight, outputWidth = imageHeight-filterLength+1 , imageWidth-filterLength+1 #394 294 or 26,26

#Create output array with the correct dimensions
    output = np.zeros([outputHeight, outputWidth])
    
#Itterate over the original image and take a group of 7x7 pixels to be used 
    for y in range(outputHeight):
        for x in range(outputWidth):
            tempImg = np.array(image)

#Slide the grid till the edge hits the edges of the image 
            if x <= (imageWidth - filterLength) or y <= (imageHeight - filterLength):
                pixelGroup = tempImg[y:y+filterLength, x:x+filterLength]

#Take the sum of the pixel group multiplied by the filter and append it to the output 
            output[y, x] = np.sum(np.dot(filter , pixelGroup))
            
#Use Pyplot to take the output array of values and show them as an image
#TODO Maybe add cmap='gray' to show greyscale. Check numbers in output first.
    plt.imshow(output, cmap='gray')
    plt.show()

    return output

if __name__=="__main__":
    main()