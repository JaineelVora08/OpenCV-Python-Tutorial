import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                    "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                    "haarcascade_smile.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                    "haarcascade_eye.xml")

def detect_features(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  
# You can also specify minSize and maxSize
# detectMultiScale is a method of the cv2.CascadeClassifier class. It scans an image to detect objects (e.g., faces) by analyzing regions at multiple scales.
# Specifies how much the image size is reduced at each scale.
# Specifies how many neighbors each rectangle candidate must have to be considered a valid detection.
# A higher value means stricter detection criteria (fewer false positives).
# A lower value may include more detections, including false positives.
# gray: The input image (in grayscale) in which faces are to be detected.
# scaleFactor: A parameter that compensates for faces appearing smaller the further away they are. It adjusts the image size at each scale of detection. A value of 1.1 is commonly used.A scale factor of 1.3 means the image is scaled down to 1/1.3 of its size at each step
# minNeighbors: This parameter specifies how many neighbors each candidate rectangle should have to retain it. Higher values result in fewer detections but with higher quality. A common value is 5.
# minSize: Specifies the minimum size of the detected faces. In this case, it is set to (30, 30), meaning that faces smaller than 30x30 pixels will be ignored
  
# faces is a list of rectangles returned by face_cascade.detectMultiScale.
# Each rectangle represents a detected face, described by its:
# x,y: Top-left corner of the bounding box.
# w,h: Width and height of the bounding box.
# The function returns a list of rectangles (bounding boxes) for the detected objects.
# Each rectangle is described as (x,y,w,h), where x,y are the coordinates of the top-left corner, and 
# w,h are the width and height of the rectangle.
# opencv me + karne se right aur neeche jaayega
  
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h),
                            color=(0, 255, 0), thickness=5)
      #rectangle - it returns the modified image (when used with assignment)
        face = frame[y : y+h, x : x+w]
        #face detect ho gaya aur x,y,h,w mil gaye to fir we store that region in another variable for further processing
        gray_face = gray[y : y+h, x : x+w]

      #smiles aur eyes me frame NAHI gray_face as input daala hai
        smiles = smile_cascade.detectMultiScale(gray_face, 
                            2.5, minNeighbors=9)
        for (xp, yp, wp, hp) in smiles:
            face = cv2.rectangle(face, (xp, yp), (xp+wp, yp+hp),
                    color=(0, 0, 255), thickness=5)
        
        eyes = eye_cascade.detectMultiScale(gray_face, 
                    2.5, minNeighbors=7)
      #Loops through all detected eyes in eyes
        for (xp, yp, wp, hp) in eyes:
            face = cv2.rectangle(face, (xp, yp), (xp+wp, yp+hp),
                    color=(255, 0, 0), thickness=5)
    
    return frame
  #modified frame is returned

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

# list of FourCC video codes: https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
output = cv2.VideoWriter("assets/6_facial_detection.mp4",
            cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
            fps=fps, frameSize=(width, height))

while(True):
    ret, frame = stream.read()
    if not ret:
        print("No more stream :(")
        break
    
    frame = detect_features(frame)
    output.write(frame)
    cv2.imshow("Webcam!", frame)
    if cv2.waitKey(1) == ord('q'):
        break

stream.release()
cv2.destroyAllWindows() #!
