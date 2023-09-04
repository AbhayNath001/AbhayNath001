import cv2
import numpy as np
import time
from datetime import datetime
from Speak import Say, Just_Say
import threading

def check_room_light(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    avg_color_per_row = np.average(gray, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    return avg_color < 110

def run_camera():
    cap = cv2.VideoCapture(0)
    dark_room_message_printed = False
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if (current_time >= "06:00" and current_time < "22:00") and check_room_light(frame):
            if not dark_room_message_printed or time.time() - start_time >= 20:
                Say("Why is the room dark?")
                dark_room_message_printed = True
                start_time = time.time()
        else:
            dark_room_message_printed = False

camera_thread = threading.Thread(target=run_camera)
camera_thread.start()
camera_thread.join()
cv2.destroyAllWindows()
