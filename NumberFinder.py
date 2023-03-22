import cv2



GameScreen = cv2.imread('Pictures\CheckScreen.png', cv2.IMREAD_UNCHANGED)
Number_Of_Winner = cv2.imread('Pictures/Number20.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(GameScreen, Number_Of_Winner, cv2.TM_CCORR_NORMED )  # cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED(This is ok at 70%), cv2.TM_CCORR, TM_SQDIFF,cv2.TM_SQDIFF_NORMED
# cv2.TM_CCORR_NORMED(current winner at 95%)

#Gets best location values
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print('Best match up top left position: %s' % str(max_loc))
print('Best Match Confidence: %s' % max_val)

threshold = 0.9

#cv2.waitKey()
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
    cv2.waitKey()
    print('matchfound')

    cv2.imwrite('Pictures\Record_Results\Test_save.png', GameScreen)

else:
    print('not found')