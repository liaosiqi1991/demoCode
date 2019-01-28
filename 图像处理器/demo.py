import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('F:/test/p1.jpg')

'''
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()


px = img[100,100]
print(px)

blue = img[100,100,1]
print(blue)

img[100,100] = [255,255,255]
print(img[100,100])

'''

plt.imshow(img)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
