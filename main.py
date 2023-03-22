#https://www.thepythoncode.com/article/make-screen-recorder-python

import cv2
import numpy as np
import pyautogui
import time
import schedule
from AutoRecordData import auot_recorder
from PIL import Image, ImageGrab
import win32gui




'''
# Specify resolution
resolution = (1680, 1050)

#width and height
SCREEN_SIZE = tuple(pyautogui.size())

# Specify video codec
codec = cv2.VideoWriter_fourcc('m','p','4','v')




# Specify frames rate. We can choose any
# value and experiment with it
fps = 20.0



def Record_Screen():

    start = time.time()
    loop_time = time.time()
    number = 0
    # Specify name of Output file
    filename = f'TrainingData\Videotestmain{number}.mp4v'
    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, SCREEN_SIZE)
    print(number)
    while(True):





        # get an updated image of the game
        screenshot = pyautogui.screenshot()

        screenshot = np.array(screenshot)
        # Convert RGB to BGR
        #screenshot = open_cv_image[:, :, ::-1].copy()
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        out.write(screenshot)
        cv2.imshow('Computer Vision', screenshot)

        # debug the loop rate
        #print('FPS {}'.format(1 / (time.time() - loop_time)))
        time.time() - loop_time
        #if time_list
        end = time.time()
        elapsed = end - start
        print(elapsed)
        loop_time = time.time()


        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv2.waitKey(1) == ord('q') or elapsed >= 3:

            out.release()
            cv2.destroyAllWindows()
            number += 1
            print(number)
            break

        #return number


schedule.every(4).seconds.do(Record_Screen)

while True:
schedule.run_pending()
time.sleep(1)'''