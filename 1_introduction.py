import cv2

#this image might go way off screen. The reason for this is because the dimensions
#of this image were far greater than the dimensions of the monitor that I'm currently working on. - so we use rescaling and resizing images
#if you have large images, it's possibly going to go off screen.

img = cv2.imread("assets/cat.jpg", cv2.IMREAD_COLOR)
print(img.shape) # print the image dimensions

print(img[0, 0]) # print the first pixel

#Note: jab grayscale image tab ek hi number return hoga btw 0 and 255 (0-black and 255-white)
#      jab colour return hoga tab 3 numbers ka array return (BGR)
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
#Note: if you print rgb_img instead of img, to output theek se NAHI aayega...bcs imshow BGR ke hisab se print and regimg me to RGB ke hisab se array me stored hai
# like cvtColor se array change ho gaya acc to RGB but imshow ko to vhi array BGR ki tarah lagega

cv2.waitKey(0) # pause the program until any key is pressed 
# Without this, the image window might close immediately
# 0: Wait indefinitely for a keypress.

# Returns the ASCII value of the key pressed (if a key is pressed).
# Returns -1 if no key is pressed within the given time.

cv2.destroyAllWindows()

'''

use of waitKey(0):

1. Timeout for User Interaction: Give the user a limited time to press a key before continuing:
key = cv2.waitKey(5000)  # Wait for 5 seconds
if key == ord('s'):  # If the user presses 's'    (The ord() function in Python returns the Unicode code point (integer representation) of a given character)
    print("You pressed 's'!")
else:
    print("Timeout or no valid key pressed.")

The program will pause and keep any OpenCV-created windows (e.g., from cv2.imshow) open for exactly 5 seconds.
After the timeout, the program will continue executing the next lines of code, even if no key is pressed.
So 5 seconds ke liye iske neeche ka code stops executing (BUT keypress vaala code chalega)

2. Display an Image Briefly: Automatically close an image window after showing it for a specific duration:
cv2.imshow('Image Window', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

In summary, cv2.waitKey(5000) pauses the program for 5 seconds while waiting for a keypress and then resumes, regardless of whether a key was pressed or not.
'''  
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/1_gray_cat.jpg", gray_img)
# imwrite vaala destroyAllWindows ke baad bhi likh sakte hai
# destoyAllWindows is NOT the end of the program
