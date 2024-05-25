# from pynput.mouse import Button, Controller


# mouse = Controller()

# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))
# --------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import cv2 as cv
from pynput import mouse

 
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


button_pressed_flag = False

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        if button == button.left:
            print(button)
            button_pressed_flag = True
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()



#https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html


##https://stackoverflow.com/questions/43776606/direct-way-to-get-camera-screenshot
# If you want your camera screenshot function to be responsive, you need to initialize the camera capture outside of this function.

#On the following code snippet, the screenshot function is triggered by pressing c:
#----------------------------------------------------------------------------------------------------------
# import cv2

# def screenshot():
#     global cam
#     cv2.imshow("screenshot", cam.read()[1]) # shows the screenshot directly
#     #cv2.imwrite('screenshot.png',cam.read()[1]) # or saves it to disk

# if __name__ == '__main__':

#     cam = cv2.VideoCapture(1) # initializes video capture
#     while True:
#         ret, img = cam.read()
#         cv2.imshow("cameraFeed", img) # a window is needed as a context for key capturing (here, I display the camera feed, but there could be anything in the window)
#         ch = cv2.waitKey(5)
#         if ch == 27:
#             break
# #        if cv2.EVENT_LBUTTONDOWN:  #ord('c'): # calls screenshot function when 'c' is pressed
#         if ch == ord('c'):
#             screenshot()
#             print('here')
#             break

#     cv2.destroyAllWindows()

#--------------------------------------------------------------

# #new attempt
# import cv2

# def mouse(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         return True

# cap = cv2.VideoCapture(0)

# print(cv2.setMouseCallback.__doc__)

# while True:

#     if cv2.setMouseCallback('frame', mouse)==True:
#       print("Left Mouse Button has been clicked")

# cv2.destroyAllWindows

#-----------------------------------------------------------------------------

#pynput mouse listener

# from pynput.mouse import Button, Controller

# mouse = Controller()

# # Press and release
# mouse.press(Button.right)
# mouse.release(Button.right)


# from pynput import mouse

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     if not pressed:
#         # Stop listener
#         if button == button.left:
#             print(button)
#             button_pressed_flag = True
#         return False

# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0} at {1}'.format(
#         'down' if dy < 0 else 'up',
#         (x, y)))

# # Collect events until released
# with mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()