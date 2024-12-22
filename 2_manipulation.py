import cv2
import numpy as np

img = cv2.imread("assets/cat.jpg", cv2.IMREAD_COLOR)

if img is None:
    raise ValueError("Image not found or unable to load.")

# RESIZE -  3 methods (m3 neeche)
# format is (width, height) and not (height, width)
img = cv2.resize(img, (1000, 2000))
img = cv2.resize(img, (0, 0), fx=1, fy=0.5)
#here, fx and fy are kitne se multiply karne hai previous sizes ko

# CROP
#note: crop ke liye function NAHI hai:
#crop karne ke liye hum numpy array ke yeh element se yeh element (ie slicing) use karte hai   
height, width = img.shape[0], img.shape[1]
# shape gives (rows,columns)
img = img[int(height/3) : , 50 : -50]
# upar se height/3 se start karo and udhar se leke end tak
# image slicing requires integer indices as array indices must be integers

# ROTATE
height, width = img.shape[0], img.shape[1]
# M2 - height, width = img.shape[:2]
img = cv2.rotate(img, cv2.ROTATE_180)

#agar koi non standard angle se image rotate karvana ho to:
#M is rotation matrix
M = cv2.getRotationMatrix2D(center=(width/2, height/2), 
                            angle=150, scale=1)
img = cv2.warpAffine(img, M, (width, height))  
# yaha it is newwidth and newheight - If these dimensions do not account for scaling or rotation, parts of the transformed image may be cropped or have unwanted blank areas.
# new_width = int(width * scale)
# new_height = int(height * scale)

#its source,destination
#note yaha it is (width,height) NOT (height,width)

# Note: method 3 for resizing - Allows scaling around any arbitrary center, not just the image origin.
# M = cv2.getRotationMatrix2D(center=(width/2, height/2), 
#                             angle=0, scale=3)
# img = cv2.warpAffine(img, M, (width, height))  

# TRANSLATE
tx = width / 5
ty = -height / 5
# A negative tx shifts left.
# A negative ty shifts up.

#usi frame me translate (thoda part cut ho sakta hai - like vo khali area black hoga)

# translation matrix
M = np.array([
    [1, 0, tx],
    [0, 1, ty]
])
img = cv2.warpAffine(img, M, (width, height))

cv2.imshow("Cat!", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/2_man_cat.jpg", img)
