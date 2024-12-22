import cv2

img = cv2.imread("assets/cat.jpg", cv2.IMREAD_COLOR)

# BORDER 
img = cv2.copyMakeBorder(img, 
                top=50, bottom=50, left=50, right=50, 
                borderType=cv2.BORDER_CONSTANT,
                value=(100, 0, 0))
#BORDERCONSTANT bezel type banega - usme value is BGR value of bezel
#top=... nahi type karke sirf number bhi chalega

# LINE
img = cv2.line(img, pt1=(700, 675), pt2=(700, 550), color=(0, 200, 0), thickness=20)
#pt1 pt2 is coordinates of points
img = cv2.line(img, (625, 675), (700, 550), color=(0, 200, 0), thickness=20)
img = cv2.line(img, (225, 675), (300, 800), color=(0, 200, 0), thickness=20)
img = cv2.line(img, (225, 675), (400, 750), color=(0, 200, 0), thickness=20)

# ARROW - arrow ka same syntax as line - arrow from pt1 to pt2
img = cv2.arrowedLine(img, pt1=(50, 50), pt2=(450, 600), color=(0, 0, 200),
        thickness=10)


# CIRCLE // center, color, radius, thickness  (thickness = -1 se filled circle and other numbers se actual thickness)
img = cv2.circle(img, center=(1450, 800), color=(100, 100, 0),
                radius=100, thickness=-1)

# ELLIPSE // center, axes=(hori=a,vert=b), angle, startAngle, endAngle, color, thickness
img = cv2.ellipse(img, center=(300, 685), axes=(50, 30), 
                angle=100, startAngle=0, endAngle=270, 
                color=(0, 200, 200), thickness=20)

# startAngle: Starting angle of the ellipse arc (in degrees) measured counterclockwise from the horizontal axis from right of centre.
# endAngle: Ending angle of the ellipse arc (in degrees), also measured counterclockwise.
# Together, they define the portion of the ellipse that will be drawn.
# startAngle = 0, endAngle = 360: Draws full ellipse.
# startAngle = 0, endAngle = 180: Draws the top half of the ellipse.
# startAngle = 90, endAngle = 270: Draws the left half of the ellipse.


# RECTANGLE
img = cv2.rectangle(img, pt1=(50, 1200), pt2=(2000, 1400), 
                    color=(150, 150, 150), thickness=-1)
#here pt1 is top left corner AND pt2 is bottom right corner

# TEXT
img = cv2.putText(img, "ELLA <3", org=(300, 1300), 
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=5, 
                color=(0, 0, 0), thickness=10)
#org is coordinates of bottom left corner of text string in image
#fontscale is base size ko kitne se multiply karna hai

cv2.imshow("ELLA", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/3_cat_drawn.jpg", img)
