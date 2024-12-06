import cv2

img = cv2.imread("assets/cat.jpg", cv2.IMREAD_COLOR)
print(img.shape) # print the image dimensions

print(img[0, 0]) # print the first pixel

#Note: jab grayscale image tab ek hi number return hoga btw 0 and 255 (0-black and 255-white)
#      jab colour return hoga tab 3 numbers ka arrray return (BGR)
#      imread returns a numpy array 

# img = img * 2

# Increase the values of every pixel
# for i in range(img.shape[0]):          #shape[0] is no of rows and 1  is number of columns
#     for j in range(img.shape[1]):
#         img[i, j] = max(254, img[i, j] * 2)

# Invert the default BGR pixel order to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(rgb_img[0, 0])

cv2.imshow("Cat", img)
cv2.waitKey(0) # pause the program until any key is pressed
cv2.destroyAllWindows()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/1_gray_cat.jpg", gray_img)
