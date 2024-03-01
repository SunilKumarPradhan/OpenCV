import cv2 as cv
def changeRes(capture, width, height):
    # Only works for live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('0') # 0 is the camera number

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    
    cv.imshow('Video', frame)
    changeRes(capture, 500, 500)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)