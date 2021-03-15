
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def gaussianFilter(sigma, size, image):
    """
    sigma: float
        variance of gaussian filter.
    size: int
        size of gaussian filter. Assume size is odd.
    image: 2d array
        2d array of an image. Each value, image[i][j] is the pixel intensity at pixel (i, j).
    
    
    gaussianFilter applies a gaussian filter with sigma and shape (size, size) to image.
    Same padding is used; the resulting image will have the same shape as input image.
    """
    
    k = int((size - 1) / 2)
    
    # Create a gaussian filter
    
    vt = np.linspace(-k, k, size)
    x, y = np.meshgrid(vt, vt)
    gFilter = (1/ (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2)/(2 * sigma**2))
    gFilter /= np.sum(gFilter)
    
    # Pad image with zeroes
    
    paddedImage = np.pad(image, (k, k))
    
    # Create new image
    
    filteredImage = np.zeros((image.shape[0], image.shape[1]))
    
    # Iterate through every pixel in the image. For each pixel, apply the gaussian filter and
    # update image with the new pixel intensity.
    
    for i in range(k, paddedImage.shape[0] - k):
        for j in range(k, paddedImage.shape[1] - k):
            surroundingPixels = []
            for m in range(-k, k + 1):
                pixelRow = []
                for n in range(-k, k+1):   
                     pixelRow.append(paddedImage[i + m][j + n])
                surroundingPixels.append(pixelRow)
                
            filteredPixel = np.sum(np.multiply(surroundingPixels, gFilter))
            
            filteredImage[i - k][j - k] = filteredPixel
    
    return filteredImage


def gradientMagnitude(image):
    """
    image : 2d array
        2d array of an image. Each value, image[i][j] is the pixel intensity at pixel (i, j).
    
    gradientMagnitude returns the gradient magnitude of the image, using the sobel operator.
    """
    
    # Pad image with zeroes 
    
    paddedImage = np.pad(image, (1, 1))
    
    # Create new image
    
    filteredImage = np.zeros((image.shape[0], image.shape[1]))
    
    # Sobel filters
    
    sobelX = [[-1,  0,  1],
              [-2,  0,  2],
              [-1,  0,  1]]
    
    sobelY = [[-1, -2, -1],
              [0 ,  0,  0],
              [1 ,  2,  1]]
    
    # Iterate through every pixel in the image. For each pixel, apply the sobel filter and
    # update image with the new pixel intensity.
    
    for i in range(1, paddedImage.shape[0] - 1):
        for k in range(1, paddedImage.shape[1] - 1):
            surroundingPixels = [[paddedImage[i - 1][k - 1], paddedImage[i - 1][k], paddedImage[i - 1][k + 1]],
                                 [paddedImage[i    ][k - 1], paddedImage[i    ][k], paddedImage[i    ][k + 1]],
                                 [paddedImage[i + 1][k - 1], paddedImage[i + 1][k], paddedImage[i + 1][k + 1]]]
            
            gx = np.sum(np.multiply(surroundingPixels, sobelX))
            gy = np.sum(np.multiply(surroundingPixels, sobelY))
            
            gradient = np.sqrt(gx ** 2 + gy ** 2)      
            
            filteredImage[i-1][k-1] = gradient
    
    return filteredImage



def threshold(image):
    """
    image : 2d array
        2d array of an image. Each value, image[i][j] is the pixel intensity at pixel (i, j).
    """

    # Create new image
    
    filteredImage = np.zeros((image.shape[0], image.shape[1]))
    
    # Create initial threshold
    imageHeight, imageWidth = image.shape
    thresholds = []
    thresholds.append(np.sum(image)/ (imageHeight * imageWidth))
    
    # Set epsilon to an aribritary high number, so algorithm can run.
    epsilon = 100000

    
    while epsilon > 0.1:
        lower = 0
        lowerCount = 0
        upper = 0
        upperCount = 0
        
        # Check every pixel, and categorize into upper or lower class
        
        for i in range(0, len(image)):
            for k in range(0, len(image[i])):
                if image[i][k] > thresholds[-1]:
                    upper += image[i][k]
                    upperCount += 1
                else:
                    lower += image[i][k]
                    lowerCount += 1
                    
        newThreshold = (lower/lowerCount + upper/upperCount) / 2
        epsilon = np.abs(newThreshold - thresholds[-1])
        thresholds.append(newThreshold)
    
    # Create the output image; every pixel greater than threshold is white, 
    # every pixel less or equal to threshold is black.
    
    for i in range(0, len(image)):
            for k in range(0, len(image[i])):
                if image[i][k] >= thresholds[-1]:
                    filteredImage[i][k] = 255
                else:
                    filteredImage[i][k] = 0
        
    return filteredImage


def ccLabelling(image):
    """
    image : 2d array
        2d array of an image. Each value, image[i][j] is the pixel intensity at pixel (i, j).
        
    ccLabelling returns an image with the pixel intensities being the labels.
    """
    queue = []
    currentLabel = 1
    imageHeight, imageWidth = image.shape
    imageLabels = np.zeros((imageHeight, imageWidth))
    
    for i in range(0, imageHeight):
            for k in range(0, imageWidth):
                if image[i][k] == 255 and imageLabels[i][k] == 0:
                    imageLabels[i][k] = currentLabel
                    queue.append((i, k))
                    while queue:
                        i, k = queue.pop(0)
                        for p in range(-1, 2):
                            for q in range(-1, 2):
                                if imageHeight > i + p >= 0 and imageWidth > k + q >= 0:
                                    if image[i + p][k + q] == 255 and imageLabels[i + p][k + q] == 0:
                                        imageLabels[i + p][k + q] = currentLabel
                                        queue.append((i + p, k + q))
                    currentLabel += 1
    
    return imageLabels            
