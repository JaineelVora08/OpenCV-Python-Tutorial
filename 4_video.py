import cv2 # See video 1 for installation

# Replace "0" with a file path to work with a saved video
# use 0 if you want to use a webcam device
stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No stream :(")
    exit()

fps = stream.get(cv2.CAP_PROP_FPS)
#The get function retrieves the properties of the video stream, and you can use it to fetch attributes like frame width, height, frames per second, etc. The values returned by stream.get() are usually float types, so you convert them to integers using int(). get(3)/4 are standard values
width = int(stream.get(3))
height = int(stream.get(4))

# list of FourCC video codes: https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
#just as imgwrite is used to save image vaise hi videowriter is used to save video webcam vaala
output = cv2.VideoWriter("assets/4_stream.mp4",
            cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
            fps=fps, frameSize=(width, height))
#fourcc is the code jo opencv ko bolega ki its a mp4 file -  if not u wont be able to play video - corrupt video

#infinite while loop jaha hum frame by frame display kar rahe hai

# The read() method reads the next frame from the video capture source.
# It returns two values:
# ret:
# A boolean value indicating if the frame was successfully read.
# True: Frame read successfully.
# False: End of the video or failure to capture a frame (e.g., camera disconnected).
# frame:
# The actual frame of video captured, represented as a NumPy array.
# If ret is False, frame may be None.

# ret checks whether the frame capture was successful.
# frame holds the actual image data of the frame if ret is True.
# this line is used in a loop for continuously capturing frames from a video or camera stream
# Refer SS also

while True:
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("No more stream :(")
        break
    
    frame = cv2.resize(frame, (width, height))
    output.write(frame)
    #displaying the frame
#     output is a VideoWriter object used to write video frames to a file.
#     It is initialized with parameters that define where the video will be saved, what codec to use, the frame rate, and the resolution.
#     You use the output.write(frame) method to write each frame of the video.
    cv2.imshow("Webcam!", frame)

    '''
    OpenCV’s cv2.waitKey() may return a 32-bit integer that includes more information than just the ASCII code of the key. 
    The value 0xFF (which is 255 in decimal) is a mask that isolates the lower 8 bits of the result from cv2.waitKey(). we effectively extract the key press value (from the lower 8 bits) and discard the irrelevant higher bits.
    The lower 8 bits represent the key code (e.g., the ASCII value of the key pressed).
The higher 24 bits may contain other system-specific or irrelevant data that we do not care about when checking the key pressed.
    '''
    #if cv.waitKey(20) & 0xFF == ord('q'): - USE THIS
    # this is essentially if (cv.waitKey(20) & 0xFF) == ord('q'):
    #If you're working with real-time video processing, the second form (cv.waitKey(20) & 0xFF) is typically preferred for maintaining performance. For static or single-frame image displays, the first form (cv.waitKey(0)) is more appropriate.
    if cv2.waitKey(1) == ord('q'): # press "q" to quit - window pe cross dabane se band NAHI hoga
        break

stream.release()
cv2.destroyAllWindows() #!
