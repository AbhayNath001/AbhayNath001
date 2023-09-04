import cv2
import numpy as np
import pyautogui

# set the screen resolution
width, height = 1920, 1080

# set the codec for the video
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# create a video writer object
out = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, (width, height))
print("started")
# start the screen recording
while True:
    img = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break
print("stoped")
# release the video writer and close the window
out.release()
