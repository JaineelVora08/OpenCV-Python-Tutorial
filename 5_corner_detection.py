import cv2
import numpy as np

img = cv2.imread("assets/shapes.png")
#bcs corner detection me colour se farak nai padta and grayscale is easier to work with
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# SHI-TOMASI METHOD
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=0.15, minDistance=50)
corners = np.int0(corners)

# qualityLevel=0.15: A threshold parameter that defines the minimum accepted quality of the corners. It is a value between 0 and 1, where a higher value means fewer, but stronger corners will be detected. A value of 0.15 indicates that the quality of the corners must be at least 15% of the best possible corner quality.
# corners is a list of points (coordinates) where the algorithm detected corners in the image. These points are typically represented as 2D coordinates (x, y), which correspond to locations of strong features in the image.
# The cv2.goodFeaturesToTrack() function returns a NumPy array of shape (N, 1, 2), where N is the number of detected corners (up to the specified maxCorners). Each element is a point represented as a 2D array [x, y], where x and y are the coordinates of a corner.

for c in corners:
  # The expression x, y = c.ravel() is used in OpenCV (and more generally in NumPy) to extract the coordinates (or values) from a 2D point or array and assign them to variables x and y
  # if c is a 2D array with shape (1, 2) (i.e., c = np.array([[x, y]])), .ravel() will flatten it into a 1D array: [x, y].
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=20, 
                    color=(0, 0, 255), thickness=-1)

# HARRIS CORNER DETECTION
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                qualityLevel=0.01, minDistance=50,
                useHarrisDetector=True, k=0.1)
corners = np.int0(corners)

for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x, y), radius=10, 
                    color=(0, 254, 0), thickness=-1)

cv2.imshow("Shape", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/5_shape_w_corners.png", img)
