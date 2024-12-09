import cv2 # See video 1 for installation
import numpy as np

# Replace "0" with a file path to work with a saved video
stream = cv2.VideoCapture("assets/cyclists.mp4")

if not stream.isOpened():
    print("No stream :(")
    exit()

num_frames = stream.get(cv2.CAP_PROP_FRAME_COUNT)
frame_ids = np.random.uniform(size=20) * num_frames
#sirf uniform will give us btw 0 and 1
frames = []
for fid in frame_ids:
    stream.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = stream.read()

# stream.set(cv2.CAP_PROP_POS_FRAMES, fid):
# This sets the position of the video file reader (stream) to the frame number fid.
# cv2.CAP_PROP_POS_FRAMES is a property in OpenCV that allows you to jump to a specific frame in the video.
    
    if not ret: # if no frames are returned
        print("SOMETHING WENT WRONG")
        exit()
    frames.append(frame)

# The median frame here is our background
median = np.median(frames, axis=0).astype(np.uint8)
#Computes the pixel-wise median across all frames in the frames list.
# For each pixel (x, y), it takes the median value of that pixel across all frames in the list.
# The resulting frame (median) represents the median background across the input frames.
# .astype(np.uint8):
# Converts the resulting median frame to uint8 format (required for image processing in OpenCV).

median = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)

fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))

# list of FourCC video codes: https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
output = cv2.VideoWriter("assets/8_no_background.mp4",
            cv2.VideoWriter_fourcc('m', 'p', 'g', '4'),
            fps=fps, frameSize=(width, height))

stream.set(cv2.CAP_PROP_POS_FRAMES, 0)
while True:
    ret, frame = stream.read()
    if not ret: # if no frames are returned
        print("No more stream :(")
        break
    
    # take out any pixel that is similar to our median frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dif_frame = cv2.absdiff(median, frame)
    # Computes the per-element/per pixel absolute difference between two images or matrices.
    threshold, diff = cv2.threshold(dif_frame, 100, 255,
                    cv2.THRESH_BINARY)
    # convert the grayscale image dif_frame into a binary image diff by applying a thresholding operation/binarise image
    # so if diff>threshold = 255 ; else = 0
    # Pixel intensities greater than 100 are set to the maximum value (255).
    # Intensities less than or equal to 100=threshold are set to 0.
#doubt - threshold high to more accurate??
    # cv2.THRESH_BINARY:
    # Specifies the type of thresholding:
    # Converts pixel intensities to either 0 or 255 (binary image)
    
    # frame = cv2.resize(frame, (width, height))
    output.write(diff)
    cv2.imshow("Video!", diff)
    cv2.waitKey(20)
    if cv2.waitKey(1) == ord('q'): # press "q" to quit
        break

stream.release()
cv2.destroyAllWindows() 


# we have a tree that tree never moves it's always in the same spot
# so just imagine those are identical
# trees in the exact same spot
# and then we have Joe
# is standing next to the tree at the
# beginning
# then he walked to the middle
# and finally he walked to the upper right
# hand corner
# a little cut off actually from the video
# if we're looking at this and we want to
# look at what is constant and what is not
# constant AKA what is the background what
# is not the background we know that the
# tree and the white
# that's the background Joe is the
# foreground Joe's not the background and
# we want to remove Joe from this image
# how do we do that
# how we do that is we look at a pixel
# in all three videos
# and we look at what the median value is
# so in this case we got white white and
# then blue the median value is going to
# be white and that's going to be the
# final pixel in that position
# and because we're taking median there
# can be light differences so in one case
# the green isn't shade the other is in
# full light there's going to be some
# variance in there and doing the median
# lets us know that oh it's going to be
# within this green range

rather than looking at every frame of
the video that can get a little
computationally expensive we're just
going to look at a random selection of
30 frames
