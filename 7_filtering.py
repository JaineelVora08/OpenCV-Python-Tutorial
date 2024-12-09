import cv2
import numpy as np

img = cv2.imread("assets/cat.jpg")
# filter2D
blur_filter = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
blur_filter = blur_filter / 9
#9 se exposure same rahega...=9 se no filter NAHI rahega bcs sum = 1 se exposure same but it was still ki average liya baaju ke pixels ka
# >9 se darker (bcs kam ho jaayegi value) and <9 se lighter (bcs badh jaayegi value)
#The matrix has equal weights for each of the 9 elements (1/9). This means the filter will calculate the average of a 3x3 neighborhood of pixels and assign that average value to the center pixel.
#The matrix is normalized by dividing by 9, so the sum of all elements in the matrix equals 1. This ensures that the pixel values in the output image are not excessively bright or dar

# While the overall brightness remains unchanged, the individual pixel values can change because you're averaging values from neighboring pixels. For example:
# In the case of a blur filter, the center pixel in a 3x3 neighborhood gets replaced by the average value of its neighboring pixels. The individual pixel values may change, but the total intensity (brightness) of the image is preserved.
# Sharp edges may get softened, and fine details might be lost, but the overall brightness stays the same because the sum of the filter weights is 1.
# If you apply a blur filter (like the one with the sum of 1), the pixel value at each location is a weighted average of the surrounding pixels. Since the sum of the weights (filter matrix elements) equals 1, the pixel value is just a redistribution, not an amplification or reduction of the original intensity.
# The filter essentially redistributes the pixel intensity without causing a net increase or decrease in brightness.

blur_img = cv2.filter2D(img, ddepth=-1, 
        kernel=blur_filter)

# NO FILTER // BRIGHTNESS
no_filter = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
no_filter = no_filter * 2
bright_img = cv2.filter2D(img, ddepth=-1, 
        kernel=no_filter)

# BLUR
blur_img = cv2.blur(img, ksize=(111, 111))

# GAUSSIAN BLUR
gaus_img = cv2.GaussianBlur(img, ksize=(11, 11),
            sigmaX=30, sigmaY=300)
# ksize - kernel size has to be odd
# large kernel - more blurring and small kernel - less blurring

# SHARPEN - sharpening me you want a greater difference between your central pixel and the surrounding pixels 
#central value must be greater than sum of the negative values
sharpen_filter = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
sharp_img = cv2.filter2D(img, ddepth=-1, 
        kernel=sharpen_filter)

# EDGE DETECTION // LAPLACIAN
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.GaussianBlur(img, ksize=(3, 3),
            sigmaX=1, sigmaY=1)
edges = cv2.Laplacian(gray_img, ddepth=-1)
# how this works is it looks for the changes in Direction and colors when there's a big gap in colors between one side of an edge and another side of an edge that'll trigger the laplacian filter

cv2.imshow("Cat!", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

