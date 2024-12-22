import cv2
import numpy as np

img = cv2.imread("assets/shapes.png")
#bcs corner detection me colour se farak nai padta and grayscale is easier to work with
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SHI-TOMASI METHOD
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=0.15, minDistance=50)
corners = np.int0(corners)

# qualityLevel=0.15: A threshold parameter that defines the minimum accepted quality of the corners. It is a value between 0 and 1, where a higher value means fewer, but stronger corners will be detected. A value of 0.15 indicates that the quality of the corners must be at least 15% of the best possible corner quality. based on the eigenvalue analysis of the corner strength.
# corners is a list of points (coordinates) where the algorithm detected corners in the image. These points are typically represented as 2D coordinates (x, y), which correspond to locations of strong features in the image.
# The cv2.goodFeaturesToTrack() function returns a NumPy array of shape (N, 1, 2), where N is the number of detected corners (up to the specified maxCorners). Each element is a point represented as a 2D array [x, y], where x and y are the coordinates of a corner.
# Corner detection algorithms return corner coordinates as floating-point numbers, which may include decimal values (e.g., 100.5, 200.5). However, pixel coordinates in an image must be whole numbers (integers), since a pixel cannot be in between two values.

'''
corners = np.array([[[100, 200]], [[150, 250]], [[200, 300]]])
This structure has shape (3, 1, 2)
Here, corner refers to a 2D array (or pair), such as [[100, 200]], and .ravel() flattens it into a 1D array [100, 200]. The ravel() method returns a flattened 1D array, so you can directly unpack it into x and y.

The outermost array has 3 elements (3 detected corners).
Each of those 3 elements contains a single pair of values representing the coordinates [x, y] of the corner.
[x,y] vo array ke 2 elements 
'''

for c in corners:
  # The expression x, y = c.ravel() is used in OpenCV (and more generally in NumPy) to extract the coordinates (or values) from a 2D point or array and assign them to variables x and y
  # if c is a 2D array with shape (1, 2) (i.e., c = np.array([[x, y]])), .ravel() will flatten it into a 1D array: [x, y].
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=20, 
                    color=(0, 0, 255), thickness=-1)

# HARRIS CORNER DETECTION
# because corner detection works on intensity variations, and color information isn't needed for this purpose.
# A typical value for k is between 0.04 and 0.15. A higher value of k results in fewer, but more stable corners, while a smaller value detects more corners, but they may be less stable. Sensitivity factor used in the Harris corner detection algorithm. This affects how sharp the corners detected are.
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=0.01, minDistance=50,
                useHarrisDetector=True, k=0.1)
corners = np.int0(corners)

# yeh code har ek corner pe jaake circle draw kar dega
for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=10, 
                    color=(0, 254, 0), thickness=-1)
  #.circle returns the frame along with the circle

cv2.imshow("Shape", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/5_shape_w_corners.png", img)
