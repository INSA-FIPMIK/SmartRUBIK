import cv2
import numpy as np

def nothing(x):
    pass

def gstreamer_pipeline(
     capture_width=1280,
     capture_height=720,
     display_width=640,
     display_height=480,
     framerate=60,
     flip_method=2,
 ):
     return (
         "nvarguscamerasrc ! "
         "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
         "format=(string)NV12, framerate=(fraction)%d/1 ! "
         "nvvidconv flip-method=%d ! "
         "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
         "videoconvert ! "
         "video/x-raw, format=(string)BGR ! appsink"
         % (
             capture_width,
             capture_height,
             framerate,
             flip_method,
             display_width,
             display_height,
         )
     )


webcam = cv2.VideoCapture(gstreamer_pipeline(flip_method=2), cv2.CAP_GSTREAMER)
webcam = cv2.VideoCapture(0)  #Si webcam

path_i = 'Images/solve.png'
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

while(1):
    imageFrame = cv2.imread(path_i)
    #_, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsvFrame, lower_blue, upper_blue)

    result = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

    cv2.imshow("imageFrame", imageFrame)
    cv2.moveWindow("imageFrame", 0, 0)
    cv2.imshow("mask", mask)
    cv2.moveWindow("mask", 700, 0)
    cv2.imshow("result", result)
    cv2.moveWindow("result", 0, 520)
    cv2.moveWindow("Trackbars", 700, 520)

    if cv2.waitKey(1) == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break