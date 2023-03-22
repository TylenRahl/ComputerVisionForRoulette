# https://www.thepythoncode.com/article/make-screen-recorder-python
# https://www.thepythoncode.com/article/record-a-specific-window-in-python
#https://stackoverflow.com/questions/59759374/cv2-matchtemplate-finds-wrong-template-in-image/59779209
#https://datatofish.com/latest-file-python/
#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python
#https://stackoverflow.com/questions/39327032/how-to-get-the-latest-file-in-a-folder
'''
This machine vision project was used to record online roulette.
it would record the spining table, then format it into binary colour. Finally labeling the data and saving it'''

import cv2
import numpy as np
import pyautogui
import schedule
from schedule import every, repeat, run_pending
import time
import os
import glob
import csv




resolution = (1680, 1050)

#width and height
SCREEN_SIZE = tuple(pyautogui.size())

# Specify video codec
codec = cv2.VideoWriter_fourcc('m','p','4','v')

number = [0]
while os.path.exists(f'TrainingData\Roulette20Main{number}.mp4v'):
    number[0] += 1

# Specify name of Output file


# Specify frames rate. We can choose any
# value and experiment with it
fps = 20.0

# Creating a VideoWriter object


def Record_Screen(number):

    start = time.time()
    loop_time = time.time()
    while(True):

        # path to training data files
        folder_path = r'C:\Users\Tylen\PycharmProjects\RouletteMaster\TrainingData*'
        file_type = '\*mp4v'
        files = glob.glob(folder_path + file_type)

        ''' Setting up Camera and Recorder'''

        # get an updated image of the game
        screenshot = pyautogui.screenshot()

        screenshot = np.array(screenshot)
        # Convert RGB to BGR
        #screenshot = open_cv_image[:, :, ::-1].copy()
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        filename = f'TrainingData\RouletteCatMain{number}.mp4v'

        out = cv2.VideoWriter(filename, codec, fps, SCREEN_SIZE)

        #if os.path.exists(filename)

        # record video
        out.write(screenshot)
        cv2.imshow('Computer Vision', screenshot)

        ''' Working Out The Elasped Time'''
        # debug the loop rate
        #print('FPS {}'.format(1 / (time.time() - loop_time)))
        time.time() - loop_time
        #if time_list
        end = time.time()
        elapsed = end - start
        print(elapsed)
        loop_time = time.time()

        '''If stateMeant, to Finish Recording and rename file'''
        # press 'q' with the output window focused to exit.
        # uses elapsed to count to three seconds
        if cv2.waitKey(1) == ord('q') or elapsed >= 3:

            out.release()
            cv2.destroyAllWindows()
            number[0] += 1
            print(number)
            break



    print('Done.')

def Edit_Save():
    start = time.time()
    screenshot = pyautogui.screenshot()

    screenshot = np.array(screenshot)
    # Convert RGB to BGR
    # screenshot = open_cv_image[:, :, ::-1].copy()
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    #screenshot = cv2.adaptiveThreshold(screenshot, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
    cv2.imshow('Computer Vision', screenshot)
    print("Showing picture")
    cv2.imwrite("TempSa\TS.png", screenshot)
    print("Taking Picture")

    # Finding the screen shot does not work live so you have to take a picture
    GameScreen = cv2.imread('TempSa\TS.png', cv2.IMREAD_UNCHANGED) 
    Number_Of_Winner = cv2.imread('TempSa/number20.png', cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(GameScreen, Number_Of_Winner, cv2.TM_CCORR_NORMED)  # cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED(This is ok at 70%), cv2.TM_CCORR, TM_SQDIFF,cv2.TM_SQDIFF_NORMED
    # cv2.TM_CCORR_NORMED(current winner at 95%)

    # Gets best location values
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print('Best match up top left position: %s' % str(max_loc))
    print('Best Match Confidence: %s' % max_val)

    threshold = 0.9
    print(max_val)
    end = time.time()
    elapsed = end - start


    # cv2.waitKey()
    if max_val >= threshold:
        # Get dimensions of image
        Number_Of_Winner_Width = Number_Of_Winner.shape[1]
        Number_Of_Winner_Height = Number_Of_Winner.shape[0]

        # This is used to find the size of the rectangle
        top_left = max_loc
        bottom_right = (top_left[0] + Number_Of_Winner_Width, top_left[1] + Number_Of_Winner_Height)

        cv2.rectangle(GameScreen, top_left, bottom_right,
                              color=(0, 0, 225),
                              thickness=2,
                              lineType=cv2.LINE_4)

        cv2.imshow('Result', GameScreen)
        print('matchfound')
        if cv2.waitKey(1) == ord('q') or elapsed <= 1:


            # Finds the folder of the files you want, has to to have the r at the front or it will throw truncated error,
            # * gets all the files, try using double \ or \\
            folder_path = r'C:\\Users\\Tylen\\PycharmProjects\\RouletteMaster\\TrainingData*'
            file_type = '\*mp4v'
            files = glob.glob(folder_path + file_type)

            # Gets the latest file
            old_file_name = max(files, key=os.path.getctime)
            print(old_file_name)

            # Renames file
            time.sleep(2)
            os.rename(old_file_name, old_file_name.replace('Cat', '20'))
            print(old_file_name)

            time.sleep(2)
            cv2.destroyAllWindows()
            return



    else:

        print('not found')
        time.sleep(2)
        cv2.destroyAllWindows()

schedule.every(5).seconds.do(lambda: Record_Screen(number))
schedule.every(5).seconds.do(Edit_Save)
while True:
    schedule.run_pending()
    time.sleep(1)


#Record_Screen()

#while True:
#time.sleep(15)
'''
        for i in range(int(record_seconds * fps)):
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            out.write(frame)
            # show the frame
            cv2.imshow("screenshot", frame)
            # if the user clicks q, it exits
            #This does not work with schedule
            if cv2.waitKey(1) == ord("q"):
                out.release()
                cv2.destroyAllWindows()
                break
                
                start = time.time()
    loop_time = time.time()
    while(True):

        # get an updated image of the game
        screenshot = pyautogui.screenshot()

        screenshot = np.array(screenshot)
        # Convert RGB to BGR
        #screenshot = open_cv_image[:, :, ::-1].copy()
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
        filename = f'TrainingData\Videotestmain{number}.mp4v'
        out = cv2.VideoWriter(filename, codec, fps, SCREEN_SIZE)
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
            number[0] += 1
            print(number)
            break

    print('Done.')

    '''


# schedule.every(10).seconds.do(Record_Screen)

# make sure everything is closed when exited
# schedule.every(5).seconds.do(Record_Screen)
#while True:
    #schedule.run_pending()
    #time.sleep(1)