# from pynput.mouse import Button, Controller


# mouse = Controller()

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))

import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
# Capture frame-by-frame
    ret, frame = cap.read()
 
# if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
# Our operations on the frame come here
#   gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #cv.COLOR_BGR2GRAY for gray
# Display the resulting frame
    cv.imshow('frame', frame) #gray instead of frame if gray frame is wanted
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


#https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html