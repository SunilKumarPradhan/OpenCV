import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(capture, width, height):
    # Only works for live video
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('OpenCV\Images\cat.jpg')
cv.imshow('cat', img)

rescaled_image = rescaleFrame(img)
cv.imshow('Image Resized', rescaled_image)





# Reading Videos
capture = cv.VideoCapture('OpenCV\Videos\CatVid.mp4')
changeRes(capture, 320, 240)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)