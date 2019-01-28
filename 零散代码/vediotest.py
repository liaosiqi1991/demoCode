#下面代码成功播放本地视频文件
import numpy as np
import cv2 as cv
cap = cv.VideoCapture('F:/test.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
