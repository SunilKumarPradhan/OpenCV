import cv2 as cv
img = cv.imread('OpenCV\Images\cat.jpg')

cv.imshow('cat', img) # cat is the name of the window
cv.waitKey(0) # 0 means that the window will be open until we close it

#if dimensions are too big, we can resize the image .

capture = cv.VideoCapture('OpenCV\Videos\CatVid.mp4')
# we can also use 0,1,2,3,4,5,6,7,8,9 for the camera number in the argument of VideoCapture
while True:
    isTrue, frame = capture.read() 
    #capture.read() returns two values, the first one is a boolean value that tells us if the frame is being read or not
    #the second one is the frame itself
    # isTrue is a boolean value that tells us if the frame is being read or not
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    # 0xFF==ord('d') is used to close the window by pressing the 'd' key
    # 20 is the time in milliseconds after which the next frame will be shown

capture.release()
cv.destroyAllWindows() # closes all the windows
#NOTE: if we don't use capture.release() then the camera will not be released and we will not be able to use it again